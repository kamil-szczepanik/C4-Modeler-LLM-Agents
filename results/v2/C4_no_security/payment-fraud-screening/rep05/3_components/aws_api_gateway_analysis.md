## Overview
This system provides real-time card-not-present payment fraud screening and case management for a mid-size payment processor. It securely evaluates high-volume authorization requests while maintaining compliance and auditability.

## Key Elements
* Payment Gateway / Merchants
* AWS API Gateway
* Fraud Scoring Engine (Go / Rust)
* Case Management & Rules Service (Node.js / Go)
* Audit & Evidence Worker (Go)
* AWS ElastiCache (Redis)
* Amazon SQS
* AWS S3 with Object Lock and Glacier Deep Archive

## Relationships
* Payment Gateway / Merchants -> AWS API Gateway: Sends payment authorization requests [HTTPS/JSON]
* AWS API Gateway -> Fraud Scoring Engine: Routes validated payloads with a 35ms integration timeout [gRPC/HTTP/2, mTLS]

## Technology Stack
* AWS API Gateway: Handles ingress traffic, native JWT authorizer validation, and AWS WAF rate-limiting to protect against DDoS.
* Go and Rust: Used for the Fraud Scoring Engine and Audit Worker to guarantee sub-50ms P99 latency and high throughput.
* Node.js / Go: Powers the Case Management & Rules Service for analyst workflows.
* AWS ElastiCache (Redis): Provides sub-millisecond rule and state caching.
* Amazon S3 with Object Lock: Ensures tamper-evident, 7-year audit retention within budget.

## Rationale
This architecture uses managed AWS services to minimize operational burden for a three-engineer team while meeting strict latency, PCI-DSS, and budgetary constraints. Native API Gateway capabilities ensure high throughput and security without custom infrastructure overhead.