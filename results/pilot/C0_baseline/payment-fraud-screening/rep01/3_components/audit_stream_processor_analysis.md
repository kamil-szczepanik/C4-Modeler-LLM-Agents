## Overview
[The system is a real-time payment fraud screening platform that processes card-not-present authorizations for a mid-size payment processor. Its core purpose is to score transactions for fraud, manage suspicious cases, and maintain secure, auditable records.]

## Key Elements
- Fraud Analysts
- Merchant Integration Systems
- Identity Provider
- API Gateway / Network Load Balancer (NLB)
- Scoring Engine (Go, AWS ECS Fargate)
- Case Management Portal (Node.js, TypeScript, PostgreSQL)
- Feature Store (Redis Cluster)
- Audit Queue (Amazon SQS)
- Audit Stream Processor (Amazon Kinesis Data Firehose)
- Audit Storage (Amazon S3, S3 Object Lock)

## Relationships
- Merchant Integration Systems -> API Gateway / Network Load Balancer: Submit payment authorizations [HTTPS/TLS 1.3]
- API Gateway / Network Load Balancer -> Scoring Engine: Route authorization requests [gRPC / HTTPS]
- Scoring Engine -> Feature Store: Fetch user features and model weights [Redis Protocol]
- Scoring Engine -> Case Management Portal: Forward suspicious transactions for analyst review [REST / HTTPS]
- Scoring Engine -> Audit Queue: Publish decision inputs, model versions, and explanations [Amazon SQS API / HTTPS]
- Audit Queue -> Audit Stream Processor: Ingest raw decision payloads [AWS SDK / HTTPS]
- Audit Stream Processor -> Audit Storage: Write immutable audit records for WORM storage [HTTPS / S3 API]

## Technology Stack
- Cloud Provider: AWS (Region: eu-west-1) for scalable, compliant infrastructure within budget constraints
- Container Runtime: AWS ECS Fargate for lightweight, serverless container orchestration
- Core Services: Go for high-performance scoring and Node.js with TypeScript for case management
- Data Storage: PostgreSQL for case management, Redis Cluster for low-latency feature lookups, and Amazon S3 with S3 Object Lock for tamper-evident audit storage
- Streaming & Security: Amazon Kinesis Data Firehose with AWS KMS encryption and TLS 1.3 for secure audit pipelines

## Rationale
[This architecture satisfies PCI-DSS Level 1 compliance and a 7-year audit requirement while adhering to a strict 25,000 EUR monthly budget and operating constraints of a 3-engineer team. Serverless and managed AWS components minimize operational overhead while guaranteeing sub-50ms P99 latency and high availability.]