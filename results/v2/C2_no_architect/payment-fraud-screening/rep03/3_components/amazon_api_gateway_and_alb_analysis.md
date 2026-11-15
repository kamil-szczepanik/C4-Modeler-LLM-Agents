## Overview
[The Real-Time Payment Fraud Screening system processes card-not-present payment authorizations to detect fraud and manage analyst reviews.]
[It provides sub-50ms fraud scoring while ensuring PCI-DSS Level 1 compliance and 7-year auditability on AWS.]

## Key Elements
- Payment Gateway / Processing Engine
- Amazon API Gateway with VPC Link
- AWS WAF and AWS ACM Private CA
- Scoring Engine (AWS ECS Fargate)
- Case Management UI & Backend (AWS ECS Fargate)
- AWS Lambda Authorizers
- Amazon S3 and AWS QLDB
- AWS CloudWatch, X-Ray, Secrets Manager, and CodePipeline

## Relationships
- Payment Gateway / Processing Engine -> Amazon API Gateway: Forwards payment authorization requests [HTTPS / TLS 1.3 and mTLS]
- Amazon API Gateway -> Scoring Engine: Routes traffic internally over VPC Link [Internal VPC protocols, mTLS]
- Case Management UI -> Amazon API Gateway: Accesses case management backend [HTTPS with OAuth 2.0 / JWT]
- Scoring Engine -> Amazon S3 & AWS QLDB: Stores model artifacts, inputs, and immutable audit logs [AWS SDK / Internal VPC]

## Technology Stack
- Amazon API Gateway: Chosen for low-latency edge routing, built-in rate limiting, and VPC Link integration without redundant ALB overhead.
- AWS ECS Fargate: Selected for containerized compute to handle 3,000 TPS within a lean three-engineer team budget.
- AWS QLDB: Utilized for tamper-evident, immutable audit logging to meet 7-year compliance requirements.
- AWS WAF & ACM Private CA: Deployed for stringent security, OWASP protection, and mandatory mTLS enforcement.
- AWS CodePipeline: Implemented for zero-downtime canary deployments of scoring models.

## Rationale
[This serverless and container-hybrid architecture minimizes operational overhead for a three-engineer team while strictly enforcing PCI-DSS Level 1 security.]
[It guarantees P99 latency under 50ms at 3,000 TPS within the 25,000 EUR monthly budget through efficient edge routing and scalable Fargate compute.]