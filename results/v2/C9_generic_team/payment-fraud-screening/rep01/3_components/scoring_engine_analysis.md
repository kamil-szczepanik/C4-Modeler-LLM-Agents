## Overview
The Real-Time Payment Fraud Screening system screens card-not-present payment authorizations for fraud at scale and provides a case management interface for manual reviews. It ensures high availability, strict P99 latency compliance, and tamper-evident auditing within a fixed cloud budget.

## Key Elements
- Fraud Analysts: Human operators reviewing suspicious payments via the Case Management UI.
- External Payment Gateway: Sends payment authorization payloads to the system.
- API Gateway / Ingestion Service: Ingests external HTTP/gRPC requests, validates schemas, and forwards payloads.
- Scoring Engine: Core container evaluating fraud risk via embedded ML runtimes.
- Amazon S3 with Object Lock: Stores immutable, tamper-evident audit logs.
- Amazon SQS: Queues asynchronous failure and audit events.
- AWS ECS with Fargate: Serverless container execution environment.

## Relationships
- External Payment Gateway -> API Gateway / Ingestion Service: Forwards authorization requests [HTTPS/gRPC]
- API Gateway / Ingestion Service -> Scoring Engine: Forwards scoring payloads [gRPC/Protobuf]
- Scoring Engine -> Amazon S3 with Object Lock: Writes tamper-evident audit logs [AWS SDK]
- Scoring Engine -> Amazon SQS: Delegates asynchronous failure events [AWS SDK / Message Queue]

## Technology Stack
- Rust or Go: Selected for the Scoring Engine to eliminate garbage collection pauses and meet the 50 ms P99 latency target at 3,000 TPS.
- Protobuf: Used for efficient, schema-validated binary communication between the API Gateway and Scoring Engine.
- Memory-Mapped Files: Enables zero-downtime model weight hot-reloading.
- AWS ECS with Fargate: Provides scalable, serverless container hosting within budget.
- Prometheus: Powers real-time telemetry, latency histograms, and circuit breaker health metrics.

## Rationale
This architecture uses high-performance compiled languages and serverless AWS infrastructure to meet strict sub-50ms latency and 3,000 TPS throughput constraints within a 25,000 EUR monthly budget. Stateless container design, circuit breakers, and local fail-safes guarantee high availability and PCI-DSS compliance while remaining operable by a three-person engineering team.