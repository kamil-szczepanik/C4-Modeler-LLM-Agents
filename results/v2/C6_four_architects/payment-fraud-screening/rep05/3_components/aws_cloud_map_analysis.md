## Overview
The system provides real-time fraud screening for card-not-present payment authorizations and case management for fraud analysts. It ensures sub-50 ms P99 decision latency while maintaining PCI-DSS Level 1 compliance and 7-year tamper-evident auditability.

## Key Elements
- Fraud Analyst (Human User)
- AWS Application Load Balancer (ALB) and Amazon API Gateway
- Fraud Scoring Service (Python, FastAPI, ONNX Runtime, Amazon ECS Fargate)
- Case Management API (Amazon ECS Fargate)
- CloudFront / React SPA (Amazon CloudFront, React)
- Amazon ElastiCache (Redis)
- Amazon S3 Model Registry and Amazon S3 Object Lock
- Amazon Aurora PostgreSQL
- AWS Cloud Map (Registry Manager, Health Check Prober, Discovery API & DNS Resolver)
- Amazon SQS and AWS Lambda
- External Systems: Payment Gateway / Core Ledger, Card Schemes / Tokenization Provider, Identity Provider (IdP), Notification Service

## Relationships
- Payment Gateway calls AWS ALB / API Gateway via HTTPS to submit transaction scoring requests.
- Fraud Scoring Service resolves internal endpoints via Amazon Route 53 Private DNS (UDP/TCP Port 53) using AWS Cloud Map.
- ECS Fargate tasks interact with the Registry Manager via AWS SDK for automatic service registration.
- Fraud Analysts access the React SPA via Amazon CloudFront (HTTPS) communicating with the Case Management API.
- Fraud Scoring and Case Management persist transactional data and audit trails in Amazon Aurora PostgreSQL and Amazon S3 Object Lock.

## Technology Stack
- AWS (eu-west-1): Target cloud provider ensuring regional isolation and compliance.
- Python & FastAPI: Powers microservices for rapid synchronous scoring.
- ONNX Runtime: Executes machine learning models with minimal latency.
- Amazon ECS Fargate: Runs containerized services without server management to fit the 3-engineer constraint.
- Amazon Route 53 Private DNS & AWS Cloud Map: Delivers sub-millisecond internal service discovery.
- Amazon Aurora PostgreSQL & S3 Object Lock: Guarantees relational persistence and tamper-evident 7-year audit logs.

## Rationale
The serverless-container architecture (ECS Fargate) minimizes operational overhead for a three-engineer team while easily scaling to meet throughput demands. Native AWS integrations like Route 53 Private DNS and ONNX Runtime guarantee sub-50 ms latencies and strict PCI-DSS compliance within the 25,000 EUR monthly budget.