## Overview
The Real-Time Payment Fraud Screening system processes card-not-present payment authorizations to detect fraud within a 50 ms P99 latency threshold. It provides fraud analysts with case management workflows while maintaining a 7-year tamper-evident audit trail under strict PCI-DSS Level 1 compliance.

## Key Elements
- Fraud Analysts
- External Payment Gateway
- API Gateway / Ingestion Service (Rust, Go, or Java with OpenAPI)
- Scoring Engine (Rust, Go, or Java with embedded ML runtimes and Protobuf)
- Case Management & Admin UI (Web UI)
- Amazon S3 with Object Lock (AWS)
- Amazon SQS Standard Queues with DLQs and Quarantine Queues (AWS)
- AWS ECS with Fargate (AWS)

## Relationships
- External Payment Gateway -> API Gateway / Ingestion Service: Forwards payment authorizations [HTTPS / REST]
- API Gateway / Ingestion Service -> Scoring Engine: Dispatches authorization requests for evaluation [gRPC]
- Scoring Engine -> Case Management & Admin UI: Routes suspicious payments for analyst review [HTTPS / WebSockets]
- Scoring Engine -> Amazon S3 with Object Lock: Persists audit payloads, model versions, and inputs [AWS SDK / HTTPS]
- Scoring Engine -> Amazon SQS: Delegates asynchronous failure events using Claims Check pattern references [AWS SDK / Message Queue]

## Technology Stack
- AWS ECS with Fargate: Runs containerized services with minimal operational overhead for a three-engineer team.
- Amazon S3 with Object Lock: Provides tamper-evident, immutable storage for 7-year audit compliance.
- Amazon SQS Standard Queues: Delivers high-throughput asynchronous messaging with long polling to fit the 25,000 EUR monthly budget.
- Rust / Go / Java: Powers high-performance ingestion and scoring microservices meeting sub-50ms latency targets.

## Rationale
This architecture uses serverless and managed AWS components to minimize operational toil for a three-engineer team within a fixed 25,000 EUR monthly budget. Asynchronous decoupling via SQS and strict adherence to security and audit patterns guarantee PCI-DSS compliance and high availability.