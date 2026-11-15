## Overview
The Real-Time Payment Fraud Screening system screens card-not-present payment authorizations in real time to prevent fraud. It processes payments securely while providing a comprehensive case management workflow for analysts.

## Key Elements
- Fraud Analyst (User)
- Payment Gateway / Acquirer (External System)
- API Gateway / Ingestion Container (AWS API Gateway / Envoy proxy)
- High-Performance Scoring Engine (AWS ECS on Fargate)
- Feature Store (Redis)
- Async Event Bus (AWS EventBridge / SQS)
- Case Management Web Application (AWS ECS on Fargate)
- Model & Rule Registry Container (Container Service)
- Audit & Compliance Storage (AWS S3 with Object Lock and Parquet format)
- Configuration & Secrets Management (AWS Secrets Manager / Parameter Store)

## Relationships
- Payment Gateway / Acquirer -> API Gateway / Ingestion Container: Submits authorization requests [HTTPS/JSON]
- API Gateway / Ingestion Container -> High-Performance Scoring Engine: Routes payment requests [gRPC/Protobuf]
- High-Performance Scoring Engine -> Feature Store: Retrieves historical transaction features [Redis RESP protocol]
- High-Performance Scoring Engine -> Async Event Bus: Publishes transaction scoring events [AWS SDK over SQS/EventBridge]
- Async Event Bus -> Case Management Web Application: Dispatches suspicious case events [AWS SQS/SNS]
- Async Event Bus -> Audit & Compliance Storage: Streams decision audit logs [AWS SQS/SNS]
- Fraud Analyst -> Case Management Web Application: Reviews flagged payments [HTTPS]

## Technology Stack
- AWS (Cloud Provider, eu-west-1): Provides fully managed, scalable cloud infrastructure.
- AWS ECS on Fargate: Runs containerized microservices without server management overhead.
- Redis: Delivers ultra-low latency feature retrieval supporting P99 < 50ms performance.
- AWS EventBridge / SQS: Decouples real-time scoring from downstream audit and case workflows.
- AWS S3 (Object Lock / Parquet): Ensures tamper-evident, cost-effective 7-year audit storage.

## Rationale
This architecture uses serverless and managed AWS services to minimize operational overhead for a three-engineer team while easily scaling to handle 3,000 transactions per second. Strict separation of concerns via asynchronous event busing ensures low-latency scoring performance and compliance with PCI-DSS Level 1 within budget constraints.