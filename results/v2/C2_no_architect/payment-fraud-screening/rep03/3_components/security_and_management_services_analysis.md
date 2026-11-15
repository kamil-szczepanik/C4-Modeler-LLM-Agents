## Overview
[The system provides real-time fraud screening for payment authorizations and case management for fraud analysts. It ensures PCI-DSS compliance, explainable auditing, and high-performance decision-making within AWS eu-west-1.]

## Key Elements
- Users: Fraud Analyst, Risk Manager / Data Scientist, Compliance & Audit Officer, System Administrator
- External Systems: Payment Gateway / Processing Engine
- Containers: Amazon API Gateway / ALB, Scoring Engine (AWS ECS Fargate), Case Management UI & Backend (AWS ECS Fargate), Serverless Tasks (AWS Lambda), Storage (Amazon S3, AWS QLDB)
- Security & Management Services: AWS IAM, AWS Secrets Manager, AWS KMS, AWS CodePipeline, AWS CloudWatch, AWS X-Ray, Amazon Inspector, AWS Signer

## Relationships
- Payment Gateway to API Gateway/ALB: Forwards payment authorization requests via HTTPS/TLS 1.3
- API Gateway/ALB to Scoring Engine: Routes screening requests via internal gRPC/HTTP
- Scoring Engine & Case Management to AWS KMS: Encrypts/decrypts cardholder data and audit logs via AWS API
- AWS CodePipeline to ECS Fargate: Deploys zero-downtime model updates using AWS internal deployment protocols

## Technology Stack
- AWS ECS Fargate: Runs containerized microservices for cost-effective serverless compute
- AWS KMS: Handles cryptographic operations with client-side key caching to prevent rate throttling
- AWS QLDB: Provides tamper-evident, immutable 7-year audit logging for regulatory compliance
- AWS CodePipeline: Automates deployments with integrated artifact signing via AWS Signer and vulnerability scanning via Amazon Inspector
- AWS CloudWatch & X-Ray: Monitors system health using tail-based sampling to control infrastructure costs

## Rationale
[This architecture leverages managed serverless and container services on AWS to maintain strict PCI-DSS Level 1 compliance and sub-50ms latencies while respecting the 25,000 EUR monthly budget. Automation via CodePipeline, KMS caching, and QLDB guarantees security, tamper-evident auditability, and operational resilience for a three-engineer team.]