## Overview
The system provides real-time fraud screening for card-not-present payment authorizations, combined with tamper-evident audit logging for compliance. It ensures secure processing and case management while maintaining a fixed infrastructure budget and strict regulatory adherence.

## Key Elements
- Real-Time Scoring Engine (Go, AWS ECS Fargate, ONNX)
- Audit Buffer Component (Amazon SQS)
- Audit Ingestion Component (AWS Lambda)
- Tamper-Evident Vault Component (Amazon S3 with Object Lock and Lifecycle Rules)
- Query & Access Component (Amazon Athena)
- Compliance Auditor / External Regulators

## Relationships
- Real-Time Scoring Engine -> Audit Buffer: Enqueue payloads via SQS API (HTTPS)
- Audit Buffer -> Audit Ingestion Component: Consume log events via AWS internal polling
- Audit Ingestion Component -> Tamper-Evident Vault Component: Persist partitioned immutable logs via S3 API
- Compliance Auditor -> Query & Access Component: Run compliance queries via AWS Console / JDBC via Athena

## Technology Stack
- Amazon SQS: Decouples the scoring engine from storage spikes to protect P99 latency
- AWS Lambda: Serverless ingestion ensuring cost efficiency for a 3-engineer team
- Amazon S3 Object Lock: Enforces WORM compliance mode for 7-year tamper-evident audit retention
- Amazon Athena: Serverless SQL querying over partitioned data for rapid auditor reporting
- Amazon S3 Lifecycle Rules: Transitions data to Glacier Flexible Archive to maintain budget limits

## Rationale
This serverless-first audit architecture guarantees 7-year tamper-evident PCI-DSS compliance without human intervention or excessive operational overhead. Decoupling storage via SQS and S3 lifecycle tiering strictly protects the 50ms latency SLA while remaining well under the €25,000 monthly budget limit.