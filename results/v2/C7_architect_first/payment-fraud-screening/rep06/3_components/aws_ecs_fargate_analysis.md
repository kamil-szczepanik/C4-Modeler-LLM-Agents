## Overview
Real-Time Payment Fraud Screening screens card-not-present payment authorizations for fraud prior to approval and provides case management for suspicious transactions. The system is operated by a three-engineer team within a strict monthly budget of 25,000 EUR in AWS `eu-west-1`.

## Key Elements
- **Users**: Fraud Analysts, Data Scientists, Compliance Auditors
- **External Systems**: Payment Gateway / Acquirer Systems, Card Networks / Tokenization Providers
- **API Gateway**: Nginx / AWS ALB
- **Scoring Engine**: Go service with embedded ONNX runtime on AWS ECS Fargate
- **Case Management**: Node.js / Express service on AWS ECS Fargate
- **Model/Rule Manager**: Python / FastAPI service on AWS ECS Fargate
- **Data & Messaging**: Amazon ElastiCache for Redis, Amazon Aurora Serverless v2, Amazon S3, Amazon MSK Serverless
- **Infrastructure**: AWS ECS Fargate, AWS VPC, AWS Secrets Manager, Amazon ECR, Amazon CloudWatch

## Relationships
- **API Gateway to Scoring Engine**: Direct internal routing using gRPC over AWS Cloud Map and internal ALB target groups for <50ms P99 latency.
- **Scoring Engine to Caching/Database**: Reads rules/models from Amazon ElastiCache for Redis and Amazon Aurora Serverless v2.
- **Scoring Engine to Event Stream**: Publishes decision inputs, model versions, and explanations to Amazon MSK Serverless.
- **Case Management to Database**: Queries persistent fraud cases and audit records via Amazon Aurora Serverless v2.
- **Management Services to Storage**: Pulls rules and model artifacts from Amazon S3.

## Technology Stack
- **AWS ECS Fargate**: Serverless container orchestration for rapid scaling and low maintenance by a 3-engineer team.
- **Go with ONNX Runtime**: High-performance compiled language and runtime for deterministic <50ms P99 latency scoring.
- **Node.js & Python FastAPI**: Lightweight frameworks for case management and rule administration workloads.
- **Amazon Aurora Serverless v2 & ElastiCache**: Scalable persistence and sub-millisecond caching staying within the 25,000 EUR budget.
- **AWS Secrets Manager & KMS**: Secure credential injection and encrypted log/storage groups for PCI-DSS Level 1 compliance.

## Rationale
The architecture combines serverless containers and managed AWS services to minimize operational overhead for a three-engineer team while meeting PCI-DSS Level 1 security standards. Compute-optimized Fargate configurations and gRPC protocols ensure the strict <50ms latency performance requirement is met within the 25,000 EUR monthly budget.