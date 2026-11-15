## Overview
The API Gateway / Ingestion Service Container is a Go-based edge service running on Amazon ECS Fargate that ingests, tokenizes, and routes payment authorization requests while enforcing strict latency and security constraints. It securely processes 3,000 requests per second with sub-50ms P99 latency while maintaining PCI-DSS compliance and tenant isolation.

## Key Elements
- Edge Router & TLS Terminator (Go)
- Tokenization & Payload Scrubber (Go)
- Local Rate Limiter & Throttle (Go)
- Ingestion API Handler & Circuit Breaker (Go)
- Usage Metering Emitter (Go)
- AWS Distro for OpenTelemetry (ADOT) Sidecar

## Relationships
- Payment Gateway / Core Processing System -> Edge Router & TLS Terminator: Sends payment authorizations [gRPC/REST over TLS 1.3]
- Edge Router & TLS Terminator -> Tokenization & Payload Scrubber: Forwards raw incoming payloads [In-memory Go channels]
- Tokenization & Payload Scrubber -> Local Rate Limiter & Throttle: Passes scrubbed payloads [In-memory Go channels]
- Local Rate Limiter & Throttle -> Ingestion API Handler & Circuit Breaker: Forwards validated requests [In-memory Go channels]
- Ingestion API Handler & Circuit Breaker -> Real-Time Scoring Engine Container: Dispatches requests for fraud scoring [gRPC over TLS with Circuit Breaker]
- Usage Metering Emitter -> AWS Kinesis Data Firehose: Asynchronously streams usage metadata for billing and SLA tracking [HTTPS]

## Technology Stack
- Go (Golang): Selected for high concurrency, low memory footprint, and minimal GC pauses to meet sub-50ms P99 latency.
- Amazon ECS Fargate: Chosen for serverless container orchestration within a 25,000 EUR monthly budget, operated by a three-engineer team.
- Go `sync.Map`: Implements local per-merchant rate limiting, eliminating external cache infrastructure (Redis) to reduce cost and operational complexity.
- AWS Distro for OpenTelemetry (ADOT): Provides scraper-less metrics and trace export to Amazon CloudWatch.
- AWS Kinesis Data Firehose: Decouples usage metering metrics from the critical request path.

## Rationale
This architecture uses Go on ECS Fargate to achieve high-throughput, low-latency transaction processing within strict budget and team constraints. Local rate limiting, tokenization at the edge, and asynchronous metering ensure PCI-DSS compliance and tenant isolation without adding operational overhead.