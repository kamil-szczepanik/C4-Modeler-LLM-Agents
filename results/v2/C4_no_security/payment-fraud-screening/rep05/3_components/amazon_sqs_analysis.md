## Overview
[System screens card-not-present payment authorizations for fraud in real-time and provides case management for analysts. Core purpose is ensuring sub-50ms fraud scoring while maintaining strict PCI-DSS Level 1 compliance and tamper-evident 7-year audit trails.]

## Key Elements
- Fraud Scoring Engine (Go / Rust container)
- Case Management & Rules Service (Node.js / Go container)
- Audit & Evidence Worker (Go container)
- Amazon SQS Standard (Message queue with DLQ for asynchronous audit events)
- AWS ElastiCache Redis (In-memory cache for rules and models)
- AWS API Gateway (Ingress proxy)
- AWS S3 with Object Lock and Glacier Deep Archive (Tamper-evident long-term storage)

## Relationships
- Fraud Scoring Engine -> Amazon SQS: Publishes decision events asynchronously [AWS SDK]
- Amazon SQS -> Audit & Evidence Worker: Delivers asynchronous audit events [SQS Poll]
- Audit & Evidence Worker -> AWS S3: Stores tamper-evident decision payloads [AWS SDK / HTTPS]
- Fraud Scoring Engine -> AWS ElastiCache Redis: Queries fraud rules and scoring models [RESP Protocol / TCP]
- Amazon SQS (DLQ) -> AWS CloudWatch: Emits metric telemetry via AWS native integration [CloudWatch Metric Stream]

## Technology Stack
- AWS SQS Standard: Chosen over FIFO for high throughput supporting 3,000 TPS without partitioning bottlenecks
- Go / Rust: Selected for Fraud Scoring Engine to guarantee sub-50ms latency (R-04)
- AWS S3 Object Lock: Ensures tamper-evident, immutable storage for the 7-year audit requirement (R-06)
- AWS KMS: Encrypts card data and audit payloads to meet PCI-DSS Level 1 compliance (R-05)

## Rationale
[This architecture decouples heavy audit logging from the critical payment path via Amazon SQS, ensuring sub-50ms latency at 3,000 TPS. Managed AWS services minimize operational overhead, fitting the fixed 25,000 EUR monthly budget and three-engineer team constraints.]