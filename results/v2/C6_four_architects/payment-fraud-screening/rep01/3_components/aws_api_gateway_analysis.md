## Overview
The system is a real-time payment fraud screening platform that evaluates card-not-present payment authorizations and manages suspicious payment reviews for a mid-size payment processor. It uses an AWS-based cloud architecture to provide low-latency scoring, strict security, and tamper-evident auditing.

## Key Elements
- **AWS WAF**: Edge security filter for IP reputation and geo-fencing.
- **AWS API Gateway HTTP API**: Public-facing ingress router for incoming payment requests.
- **Authentication & mTLS Validator**: Enforces transport security via Mutual TLS.
- **Payload Validator & Schema Enforcer**: Validates incoming request structures using JSON Schema.
- **Rate Limiter & Throttling Controller**: Protects downstream services from traffic spikes and DDoS attacks.
- **Internal Service Registry**: AWS Cloud Map for dynamic container endpoint resolution.
- **Audit Log Redactor / Sanitizer**: Strips cleartext card data from logs for PCI-DSS compliance.
- **Metrics & Telemetry Emitter**: Amazon CloudWatch and AWS X-Ray for tracing and monitoring.

## Relationships
- **Payment Gateway / Acquirer Systems -> AWS WAF**: Inspects inbound requests via `HTTPS`.
- **AWS WAF -> Authentication & mTLS Validator**: Forwards filtered traffic via `HTTPS`.
- **Authentication & mTLS Validator -> Payload Validator**: Passes authenticated traffic internally via `HTTP/2`.
- **Payload Validator -> Real-Time Scoring Engine**: Routes validated payloads using `gRPC via AWS VPC Link`.
- **API Gateway Components -> Metrics & Telemetry Emitter**: Collects telemetry asynchronously via `AWS internal telemetry bus`.
- **API Gateway Access Logs -> Amazon S3 Object Lock**: Streams sanitized logs via `AWS Kinesis Data Firehose`.
- **Real-Time Scoring Engine -> AWS API Gateway**: Returns decisions via `gRPC`.
- **AWS API Gateway -> Payment Gateway / Acquirer Systems**: Returns final responses via `HTTPS`.

## Technology Stack
- **AWS API Gateway HTTP API**: Chosen for low latency and cost-efficiency to meet the 50ms P99 budget.
- **AWS WAF**: Native edge security to satisfy PCI-DSS perimeter defense without custom code.
- **gRPC over HTTP/2**: High-performance binary protocol used for internal service communication to minimize serialization overhead.
- **AWS Kinesis Data Firehose & Amazon S3 Object Lock**: Provides tamper-evident, 7-year audit retention for regulatory compliance.
- **AWS Cloud Map**: Lightweight service discovery mechanism suited for a 3-engineer team.

## Rationale
This architecture uses fully managed AWS services to minimize operational overhead for a three-engineer team while staying within a 25,000 EUR monthly budget. It strictly enforces PCI-DSS Level 1 compliance, tamper-evident 7-year auditability, and sub-50ms P99 latency via edge filtering and gRPC communication.