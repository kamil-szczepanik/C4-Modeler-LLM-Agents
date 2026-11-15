## Overview
The Real-Time Payment Fraud Screening system processes card-not-present payment authorizations for a mid-size payment processor. It screens transactions for fraud before approval and provides case management for analysts reviewing suspicious payments.

## Key Elements
- Rule Evaluation Bus (Amazon EventBridge custom event bus)
- Event Archive & Replay Component (EventBridge Archive)
- Dead Letter Queue Handler (SQS + EventBridge DLQ)
- Event Schema Registry (EventBridge Schema Registry)

## Relationships
- Fraud Scoring Engine -> Rule Evaluation Bus: Publishes payment decision events via `PutEvents` [HTTPS / JSON]
- Rule Evaluation Bus -> Case Management App: Routes review decisions [HTTPS / EventBridge Target]
- Rule Evaluation Bus -> Amazon S3 with Object Lock: Forwards audit events [Firehose / HTTPS]
- Rule Evaluation Bus -> Event Schema Registry: Enforces payload validation [EventBridge API / JSON Schema]

## Technology Stack
- Amazon EventBridge: Provides managed event routing within a €25k/month budget
- AWS IAM & KMS: Enforces least-privilege access and data encryption at rest for PCI-DSS Level 1 compliance
- AWS CloudWatch & X-Ray: Delivers observability, distributed tracing, and automated alerting

## Rationale
This architecture meets PCI-DSS Level 1 compliance and a 50 ms P99 latency constraint while remaining manageable for a three-engineer team. It guarantees tamper-evident 7-year auditability and high availability via native AWS serverless components.