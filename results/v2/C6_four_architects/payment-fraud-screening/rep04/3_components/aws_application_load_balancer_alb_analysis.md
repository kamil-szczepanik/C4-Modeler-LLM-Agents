## Overview
The system is a real-time payment fraud screening platform that evaluates card-not-present payment authorizations in under 50 milliseconds and provides case management tools for fraud analysts. It is designed to process 3,000 transactions per second while maintaining strict PCI-DSS Level 1 compliance and 7-year auditability.

## Key Elements
- Payment Gateway / Acquirer
- Fraud Analyst
- AWS Application Load Balancer (ALB) with AWS WAF
- Fraud Scoring Engine (Java / Spring Boot, AWS ECS Fargate)
- Case Management Service (Node.js / Python, AWS ECS Fargate)
- Feature Store / Cache (Amazon ElastiCache Redis & Amazon DynamoDB)
- Transactional Database (Amazon Aurora PostgreSQL)
- Audit Storage (Amazon S3 with Object Lock)
- Rule/Model Artifact Repository (Amazon S3)

## Relationships
- Payment Gateway / Acquirer -> AWS Application Load Balancer (ALB): Sends synchronous authorization requests [HTTPS/2 with TLS 1.3]
- AWS Application Load Balancer (ALB) -> Fraud Scoring Engine: Routes scoring requests [HTTP/2 over internal VPC via AWS Cloud Map]
- Fraud Scoring Engine -> Feature Store: Fetches real-time features [Redis RESP protocol / DynamoDB API]
- Fraud Scoring Engine -> Audit Storage: Stores tamper-evident decision logs [AWS SDK / HTTPS]
- Fraud Analyst -> Analyst Frontend (Amazon CloudFront + S3): Accesses case management UI [HTTPS]

## Technology Stack
- Cloud Provider: AWS (eu-west-1 region) for managed infrastructure within budget
- Compute: AWS ECS Fargate for serverless container execution
- Load Balancing & Security: AWS Application Load Balancer (ALB) and AWS WAF with TLS 1.3 via AWS Certificate Manager (ACM)
- Scoring & Runtime: Java / Spring Boot with embedded ONNX Runtime and LightGBM models for low-latency inference
- Data Storage: Amazon ElastiCache Redis and Amazon DynamoDB for low-latency feature caching, Amazon Aurora PostgreSQL for transactional data, and Amazon S3 with Object Lock for tamper-evident audit logs

## Rationale
The architecture leverages fully managed AWS services to minimize operational overhead for a three-engineer team while easily scaling to meet the 3,000 TPS and 50ms P99 latency requirements. Embedded ONNX scoring and in-memory Redis caching eliminate network hops to achieve real-time fraud decisions within a fixed 25,000 EUR monthly budget.