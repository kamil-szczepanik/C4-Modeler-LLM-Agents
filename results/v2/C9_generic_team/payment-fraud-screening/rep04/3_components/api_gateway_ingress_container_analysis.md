## Overview
The Real-Time Payment Fraud Screening system screens card-not-present payment authorizations for fraud and manages suspicious reviews. It operates within AWS (eu-west-1) to ensure PCI-DSS Level 1 compliance and 7-year auditability.

## Key Elements
* Payment Gateway (External System)
* API Gateway / Ingress Container
* Real-Time Scoring Container
* Audit Logging Container
* Case Management Container
* Amazon S3 (with Object Lock)
* AWS SQS / Kinesis
* AWS Secrets Manager / Parameter Store
* Amazon ElastiCache (Redis)

## Relationships
* Payment Gateway -> API Gateway / Ingress Container: Submits authorization requests via REST APIs [HTTPS / REST]
* API Gateway / Ingress Container -> Real-Time Scoring Container: Sends scoring requests synchronously [gRPC / REST]
* Real-Time Scoring Container -> Audit Logging Container: Streams decision logs and inputs [AWS SQS / Kinesis]
* Audit Logging Container -> Amazon S3: Persists tamper-evident audit trails [AWS S3 API]
* API Gateway / Ingress Container -> Amazon ElastiCache: Validates idempotency keys and tracks rate limits [Redis Protocol]

## Technology Stack
* AWS API Gateway / Envoy / Nginx: Managed ingress routing and rate-limiting to fit the 3-engineer team constraint and 25,000 EUR budget.
* OpenAPI / JSON Schema: Strict boundary validation and automated schema-to-code generation in CI/CD.
* gRPC / REST: Low-latency inter-container communication supporting 3,000 requests/sec at P99 under 50ms.
* AWS S3 Object Lock: Tamper-evident, 7-year immutable storage for regulatory auditability.
* Amazon ElastiCache (Redis): Low-latency distributed cache for idempotency validation and deduplication.

## Rationale
Managed AWS services and stateless ingress design minimize operational overhead for the three-engineer team while respecting the 25,000 EUR monthly budget. Strict payload validation, connection pooling, and circuit-breaking patterns ensure high availability, PCI-DSS compliance, and sub-50ms P99 latency.