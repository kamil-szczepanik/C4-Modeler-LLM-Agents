## Overview
The system screens card-not-present payment authorizations in real time to prevent fraud while enabling analysts to review suspicious transactions. It ensures strict regulatory compliance, low-latency processing, and automated auditability within fixed cost constraints.

## Key Elements
- Fraud Analyst & Risk Manager
- Payment Gateway / Acquirer & Merchant Platforms
- Identity Provider (IdP)
- API Gateway (AWS API Gateway / ALB)
- Scoring Engine Container (Go/Rust on Amazon ECS)
- Case Management Container (Node.js/Python Monolith on Amazon ECS)
- Data Layer (Amazon DynamoDB & Amazon ElastiCache Redis)
- Event & Compliance Infrastructure (AWS SQS/SNS, AWS CloudTrail, and AWS Backup)

## Relationships
- Fraud Analyst / Risk Manager -> API Gateway / ALB: Reviews suspicious payments via data-masked UI [HTTPS with RBAC via IdP]
- API Gateway / ALB -> Case Management Container: Routes analyst and reporting traffic [HTTP/REST]
- Case Management Container -> Data Layer: Reads/writes case data, audit logs, and model metadata [Amazon DynamoDB via AWS SDK]
- Workflow & Queue Engine -> Data Layer: Consumes asynchronous event updates [Amazon DynamoDB Streams]
- Case Management Container -> AWS SQS: Handles dead-letter queues for failed asynchronous events [AWS SDK]

## Technology Stack
- AWS ECS (Elastic Container Service): Hosts microservices and monoliths with rolling updates to maintain a 3-engineer operational model
- Node.js / Python (FastAPI): Powers the Case Management Container components for rapid feature delivery
- Amazon DynamoDB: Provides low-latency NoSQL storage for active cases and decision audit trails
- Amazon ElastiCache (Redis): Caches active session and rule data to support sub-50ms latency
- AWS SQS/SNS & DynamoDB Streams: Enables asynchronous event processing and work queue indexing
- AWS Backup & S3 Glacier: Manages 7-year tamper-evident audit log retention within budget

## Rationale
This architecture uses serverless and fully managed AWS services to minimize operational overhead for a three-engineer team while easily scaling to meet strict performance targets. Separating the scoring engine from the asynchronous case management container ensures sub-50ms decision latency and PCI-DSS scope reduction without exceeding the €25k monthly budget.