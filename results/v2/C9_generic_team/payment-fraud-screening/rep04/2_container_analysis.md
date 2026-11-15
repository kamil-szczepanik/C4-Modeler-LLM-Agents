## Overview
[The system is a Real-Time Payment Fraud Screening platform that screens card-not-present payment authorizations for a mid-size payment processor and manages fraud analyst reviews.]
[Its core purpose is to provide sub-50ms fraud scoring while ensuring strict PCI-DSS Level 1 compliance and 7-year tamper-evident auditability within a fixed monthly budget.]

## Key Elements
- Fraud Analysts
- Payment Gateway
- API Gateway / Ingress Container
- Real-Time Scoring Container
- Audit Logging Container
- Case Management Container
- Amazon S3 (Model storage and Audit logs with Object Lock)
- AWS SQS / Kinesis (Asynchronous event bus)
- AWS Secrets Manager / Parameter Store

## Relationships
- Payment Gateway interacts with API Gateway via HTTPS / REST using OpenAPI contracts.
- API Gateway interacts with Real-Time Scoring Container synchronously via gRPC/REST.
- Scoring Container asynchronously dispatches decision events to Audit Logging Container via AWS SQS/Kinesis.
- Scoring Container hot-reloads machine learning models from Amazon S3.
- Audit Logging Container writes tamper-evident audit logs to Amazon S3 with Object Lock enabled in compliance mode.

## Technology Stack
- AWS (eu-west-1): Single-region deployment chosen to minimize operational complexity and fit the 25,000 EUR monthly budget.
- Terraform / AWS CDK: Infrastructure as Code for reproducible environments and automated compliance auditing.
- AWS S3 Object Lock: Ensures 7-year tamper-evident log retention for PCI-DSS compliance.
- AWS Secrets Manager: Injects credentials securely at container startup.
- OpenAPI / JSON Schema: Enforces strict ingress payload validation to maintain audit data integrity.

## Rationale
- The event-driven, decoupled audit path ensures P99 latency remains below 50 ms at 3,000 RPS without database bottlenecks.
- Stateless containers, S3 model hot-reloading, and Infrastructure as Code enable a three-engineer team to operate the platform securely and reliably within budget.