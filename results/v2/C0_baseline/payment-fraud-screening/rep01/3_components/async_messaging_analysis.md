## Overview
[The system is a real-time payment fraud screening platform that evaluates card-not-present authorizations and manages analyst reviews to ensure PCI-DSS compliance. Its core purpose is to score transactions in under 50 ms while maintaining an immutable, tamper-evident 7-year audit trail.]

## Key Elements
- Scoring Engine (AWS Lambda with Provisioned Concurrency, Go runtime)
- Async Messaging (Amazon SQS FIFO Queue and Dead-Letter Queue via AWS VPC Interface Endpoint)
- Data Layer (Amazon Aurora Serverless v2 PostgreSQL)
- Case Management (Node.js / React on AWS ECS Fargate)
- Observability (Amazon CloudWatch, AWS X-Ray)
- Security (AWS KMS Customer Managed Key)

## Relationships
- Scoring Engine -> Audit Event FIFO Queue: Enqueues decision telemetry [HTTPS/TLS 1.3 via SQS API]
- Audit Event FIFO Queue -> Data Layer Worker: Persists immutable logs [AWS SDK internal polling / Internal TCP]
- Scoring Engine -> Data Layer: Queries rules and stores operational state [PostgreSQL wire protocol over TLS 1.3]
- Case Management -> Data Layer: Manages review cases [PostgreSQL wire protocol over TLS 1.3]
- CloudWatch -> PagerDuty: Alerts on queue age and DLQ depth [HTTPS webhooks]

## Technology Stack
- AWS SQS FIFO: High-throughput mode with message group IDs for ordered, exactly-once audit event processing
- AWS Lambda: Serverless compute for low-latency scoring and batched audit log ingestion
- Amazon Aurora Serverless v2 PostgreSQL: Relational storage for transactions and case management
- AWS KMS: Customer Managed Keys with encryption context for data protection
- Node.js & Go: Runtime environments optimized for microservices and performance

## Rationale
[This architecture utilizes serverless and managed AWS services to scale dynamically and meet the strict 3,000 req/sec performance requirement within a 25,000 EUR monthly budget. It empowers a three-engineer team to maintain high availability, PCI-DSS compliance, and tamper-evident auditability without managing underlying infrastructure.]