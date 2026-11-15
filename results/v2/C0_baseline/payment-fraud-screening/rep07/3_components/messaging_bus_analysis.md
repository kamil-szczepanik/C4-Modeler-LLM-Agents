## Overview
[The system is a real-time payment fraud screening platform that evaluates card-not-present transactions for a mid-size payment processor and provides a case management interface for fraud analysts.]

## Key Elements
* AWS API Gateway / ALB
* Real-Time Scoring Engine (Go/Rust on Amazon EC2)
* Case Management Backend (Node.js, TypeScript on Amazon ECS Fargate)
* Case Management UI (React on Amazon S3 and Amazon CloudFront)
* Redis Cache (Amazon ElastiCache)
* PostgreSQL Database (Amazon RDS)
* Audit Storage (Amazon S3 with KMS and Object Lock)
* Messaging Bus (Amazon SQS Standard, SQS FIFO, and Dead-Letter Queues)
* Audit Storage Worker (AWS Lambda)

## Relationships
* Real-Time Scoring Engine -> Scoring Event Queue: Publishes decision payloads via AWS SDK (HTTPS)
* Case Management Backend -> Audit Event Queue: Publishes analyst overrides via AWS SDK (HTTPS)
* Audit Event Queue -> Audit Storage Worker: Consumes message batches via Event Source Mapping (HTTPS)
* Audit Storage Worker -> Audit Storage: Writes tamper-evident logs via Amazon S3 API (HTTPS)
* Scoring Event Queue -> Analytics/Monitoring Consumer: Streams telemetry via AWS SDK (HTTPS)

## Technology Stack
* AWS SQS Standard & SQS FIFO: Selected for high-throughput messaging, guaranteed ordering, and at-least-once delivery.
* AWS Lambda: Chosen for serverless, event-driven consumption of SQS queues within a 3-engineer team capacity.
* AWS KMS: Utilized with customer-managed keys (CMKs) to encrypt SQS queues and satisfy PCI-DSS Level 1 compliance.
* Amazon S3 Object Lock: Implemented to provide tamper-evident storage for 7-year audit requirements.
* AWS VPC Endpoints (PrivateLink): Enforced for secure internal communication, bypassing the public internet.

## Rationale
[This architecture guarantees high-throughput and sub-50ms P99 latency while maintaining PCI-DSS Level 1 compliance and a 7-year tamper-evident audit trail. Furthermore, fully managed serverless AWS components keep operational overhead minimal for a three-engineer team within the 25,000 EUR monthly budget.]