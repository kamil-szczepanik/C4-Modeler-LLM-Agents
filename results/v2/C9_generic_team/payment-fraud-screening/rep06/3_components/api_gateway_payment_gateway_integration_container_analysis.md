## Overview
[The system screens card-not-present payment authorizations for real-time fraud detection and provides case management for human analysts. It ensures sub-50ms P99 decision latency at 3,000 TPS while maintaining PCI-DSS Level 1 compliance and 7-year auditability.]

## Key Elements
- Payment Gateway (External System)
- Fraud Analysts (Users)
- API Gateway / Payment Gateway Integration Container (AWS ECS with Fargate)
- Tokenization/Masking Proxy Container (AWS ECS with Fargate)
- Real-Time Scoring Engine Container (AWS ECS with Fargate)
- Case Management Container (AWS ECS with Fargate)
- Model & Rule Registry Service Container (AWS ECS with Fargate)
- Audit & Compliance Container (AWS ECS with Fargate)
- Amazon ElastiCache (Redis)
- Amazon Aurora
- Amazon SQS / SNS
- Amazon S3 Object Lock

## Relationships
- Payment Gateway -> API Gateway / Payment Gateway Integration Container: Sends authorization requests [HTTPS/TLS 1.3]
- API Gateway / Payment Gateway Integration Container -> Tokenization/Masking Proxy Container: Forwards requests for PAN scrubbing [Internal API]
- API Gateway / Payment Gateway Integration Container -> Real-Time Scoring Engine Container: Queries fraud scores [gRPC/REST]
- Fraud Analysts -> Case Management Container: Reviews suspicious payments [HTTPS/TLS 1.3]

## Technology Stack
- AWS ECS with Fargate: Minimizes infrastructure management for a 3-engineer team within budget.
- Amazon ElastiCache (Redis): Provides edge-level request deduplication and low-latency caching.
- Amazon Aurora: Stores transactional case data and audit records securely.
- Amazon S3 Object Lock: Ensures tamper-evident, 7-year audit storage (R-06).

## Rationale
- The architecture uses serverless containers and managed AWS services to remain within the 25,000 EUR monthly budget.
- Stateless edge routing, local fallbacks, and Redis caching guarantee sub-50ms latency and high availability under 3,000 TPS.