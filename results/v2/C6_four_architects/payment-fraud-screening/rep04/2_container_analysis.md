## Overview
[The system is a real-time payment fraud screening platform that evaluates card-not-present transactions for a mid-size payment processor and provides a case management interface for fraud analysts. Its core purpose is to score authorizations in under 50 milliseconds while ensuring PCI-DSS compliance and 7-year tamper-evident auditability.]

## Key Elements
- AWS Application Load Balancer (ALB)
- Fraud Scoring Engine (Java/Spring Boot on AWS ECS Fargate)
- Case Management Service (Node.js/Python on AWS ECS Fargate)
- Feature Store / Cache (Amazon ElastiCache Redis & Amazon DynamoDB)
- Transactional Database (Amazon Aurora PostgreSQL)
- Audit Storage (Amazon S3 with Object Lock)
- Rule/Model Artifact Repository (Amazon S3)
- Asynchronous Messaging (Amazon SQS & Amazon SNS)
- Analyst Frontend (Amazon S3 + Amazon CloudFront SPA)
- Identity Provider (AWS Cognito / OIDC)

## Relationships
- Payment Gateway to AWS ALB via REST/HTTPS (HTTP/2)
- AWS ALB to Fraud Scoring Engine via HTTP/2
- Fraud Scoring Engine to Amazon ElastiCache and DynamoDB via TCP/TLS
- Fraud Scoring Engine to S3 Rule/Model Bucket via HTTPS (TLS 1.3)
- Fraud Scoring Engine to Amazon SQS via AWS SDK (HTTPS/TLS 1.3)
- Amazon SQS to Case Management Service via AWS SDK
- Fraud Analyst to Amazon CloudFront/S3 SPA via HTTPS
- SPA and Case Management Service to AWS ALB via REST/HTTPS (JSON over HTTP/2)
- Case Management Service to Amazon Aurora PostgreSQL via TCP/TLS
- Case Management Service to Amazon S3 Object Lock via AWS SDK (HTTPS/TLS 1.3)
- Case Management Service to Amazon SNS via AWS SDK (HTTPS/TLS 1.3)
- Case Management Service and SPA to Identity Provider via OIDC/OAuth2 over HTTPS

## Technology Stack
- AWS ECS on Fargate: Chosen to eliminate Kubernetes operational overhead for a 3-person team within a €25k budget.
- Java/Spring Boot with embedded ONNX/LightGBM: Selected for the Fraud Scoring Engine to guarantee P99 latency below 50 ms at 3,000 TPS.
- Amazon ElastiCache (Redis) and DynamoDB: Implemented for low-latency feature lookups and session state.
- Amazon S3 with Object Lock: Selected for tamper-evident 7-year audit log storage satisfying PCI-DSS cost-effectively.
- Amazon Aurora PostgreSQL: Utilized for relational case management transactions.

## Rationale
[This architecture leverages serverless AWS containers and in-memory caching to achieve ultra-low latency and high throughput within strict budget and team constraints. It guarantees security, zero-downtime model updates, and immutable audit trails required for PCI-DSS compliance.]