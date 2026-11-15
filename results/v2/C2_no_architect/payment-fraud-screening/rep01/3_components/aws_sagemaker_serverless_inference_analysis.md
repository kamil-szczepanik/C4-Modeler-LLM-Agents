## Overview
The Real-Time Payment Fraud Screening system screens card-not-present payment authorizations for fraud and manages analyst reviews. It ensures PCI-DSS Level 1 compliance while maintaining sub-50ms P99 latency at 3,000 transactions per second.

## Key Elements
- Fraud Analyst (User)
- External Payment Gateway, GitHub Actions (External Systems)
- API Gateway / Ingress Container (AWS ECS Fargate)
- Scoring Engine Container (AWS ECS Fargate)
- Case Management Container (AWS ECS Fargate)
- Model Inference Runtime (AWS ECS Fargate running ONNX)
- Amazon Aurora Serverless (Amazon Aurora)
- Amazon QLDB / S3 Object Lock (Amazon QLDB / Amazon S3)

## Relationships
- API Gateway -> Scoring Engine Container: Forwards authorization requests [HTTPS / REST]
- Scoring Engine Container -> Model Inference Runtime: Invokes fraud scoring [gRPC / Internal Network]
- Scoring Engine Container -> Amazon Aurora: Queries and stores transaction state [PostgreSQL Protocol / TLS 1.3]
- Fraud Analyst -> Case Management Container: Reviews suspicious payments [HTTPS / TLS 1.3]
- Case Management Container -> Amazon QLDB / S3 Object Lock: Stores tamper-evident audit logs [AWS SDK]

## Technology Stack
- Compute: AWS ECS Fargate for unified, serverless container orchestration within the 3-engineer operational capacity.
- ML Inference: ONNX Runtime for high-performance, low-latency model execution without cold-start penalties.
- Database: Amazon Aurora Serverless for scalable transactional data storage.
- Audit Storage: Amazon QLDB / S3 Object Lock for immutable 7-year audit logging to satisfy compliance (R-06).
- Security: AWS KMS for Customer Managed Keys and TLS 1.3 for data encryption in transit.

## Rationale
This unified AWS ECS Fargate and ONNX architecture avoids serverless cold-start latency to guarantee P99 performance under 50ms at 3,000 TPS. It minimizes operational overhead for a three-engineer team while strictly enforcing PCI-DSS Level 1 compliance and a 25,000 EUR monthly budget constraint.