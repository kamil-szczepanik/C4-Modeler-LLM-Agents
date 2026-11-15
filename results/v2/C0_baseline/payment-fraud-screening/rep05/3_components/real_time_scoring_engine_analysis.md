## Overview
The Real-Time Payment Fraud Screening system screens card-not-present payment authorizations for fraud under strict latency and compliance constraints. It evaluates transactions before approval and routes suspicious payments to fraud analysts for case management.

## Key Elements
- Real-Time Scoring Engine (Go on Amazon ECS Fargate)
- Case Management App (Node.js/TypeScript on Amazon ECS Fargate)
- Feature Store & Cache (Amazon ElastiCache Redis)
- Database (Amazon Aurora PostgreSQL Serverless v2)
- Model Registry (Amazon SageMaker Model Registry)
- Messaging & Audit Pipeline (Amazon SQS/SNS and Amazon S3 with Object Lock)
- Network & Security (AWS WAF, Amazon API Gateway, AWS Secrets Manager, AWS KMS, AWS X-Ray)

## Relationships
- Payment Gateway / Merchants -> Real-Time Scoring Engine: Invokes authorization scoring requests via HTTPS/REST with mTLS [Amazon API Gateway]
- Real-Time Scoring Engine -> Feature Store & Cache: Reads low-latency features [Amazon ElastiCache Redis]
- Real-Time Scoring Engine -> Messaging & Audit Pipeline: Publishes compliance audit events [Amazon SQS/SNS and Amazon S3]
- Real-Time Scoring Engine -> Model Registry: Retrieves cryptographically signed models [Amazon SageMaker]

## Technology Stack
- Go (net/http, ONNX Runtime): Delivers sub-50ms P99 latency and high throughput for the scoring engine
- Amazon ECS Fargate: Provides serverless container orchestration manageable by a 3-engineer team
- Amazon ElastiCache Redis: Delivers ultra-low latency feature retrieval
- Amazon S3 with Object Lock: Ensures tamper-evident, 7-year auditable storage for PCI-DSS compliance

## Rationale
This architecture combines Go and ECS Fargate to easily meet the 3,000 TPS and <50ms P99 latency requirements within the 25,000 EUR monthly budget. It strictly isolates sensitive payment data to maintain PCI-DSS Level 1 compliance while providing zero-downtime model updates.