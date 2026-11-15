## Overview
The Real-Time Payment Fraud Screening system screens card-not-present payment authorizations to approve, decline, or route them for review. It ensures 7-year tamper-evident auditability while adhering to PCI-DSS Level 1 compliance and a strict budget.

## Key Elements
- Cardholders / Merchants
- Fraud Analysts & Risk Managers
- Payment Gateway / Acquirer
- AWS Application Load Balancer (ALB)
- Scoring Engine (Java (Spring Boot / gRPC) on AWS ECS on Fargate)
- Case Management Service (Node.js / React on AWS ECS on Fargate)
- Amazon DynamoDB
- AWS S3 Object Lock
- AWS Cognito

## Relationships
- Payment Gateway / Acquirer -> AWS Application Load Balancer (ALB) (gRPC/HTTPS over mTLS)
- Fraud Analysts & Risk Managers -> AWS Cognito (OAuth2/OIDC)
- Fraud Analysts & Risk Managers -> Case Management Service (HTTPS, TLS 1.3)
- AWS Application Load Balancer (ALB) -> Scoring Engine (gRPC/HTTPS)
- AWS Application Load Balancer (ALB) -> Case Management Service (HTTPS)
- Scoring Engine -> Amazon DynamoDB (TCP)
- Scoring Engine -> AWS S3 Object Lock (AWS API)

## Technology Stack
- AWS ECS on Fargate: Provides container orchestration without server management overhead.
- Java (Spring Boot / gRPC): Delivers low-latency performance for the high-throughput scoring engine.
- Amazon DynamoDB: Acts as a low-latency feature store for transaction evaluation.
- AWS S3 Object Lock: Ensures tamper-evident, 7-year audit retention in Compliance Mode.
- AWS Cognito: Manages identity verification via OAuth2/OIDC and MFA.

## Rationale
This architecture leverages managed cloud services to minimize operational overhead for a three-engineer team. It guarantees high performance, strict security, and regulatory compliance within a fixed budget.