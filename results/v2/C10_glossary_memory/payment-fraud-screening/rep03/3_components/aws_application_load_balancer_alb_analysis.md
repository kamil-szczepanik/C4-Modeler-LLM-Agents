## Overview
- System: Real-Time Payment Fraud Screening System for processing card-not-present payment authorizations.
- Purpose: Screens transactions for fraud before approval and provides case management for fraud analysts within strict compliance and latency constraints.

## Key Elements
- Cardholders / Merchants
- Fraud Analysts & Risk Managers
- Payment Gateway / Acquirer
- AWS Application Load Balancer (ALB)
- Scoring Engine
- Case Management Service
- Amazon DynamoDB
- AWS S3 Object Lock
- AWS Cognito
- AWS ECS on Fargate

## Relationships
- Payment Gateway / Acquirer -> AWS Application Load Balancer (ALB) [gRPC/HTTPS over mTLS]
- Fraud Analysts & Risk Managers -> AWS Cognito [OAuth2/OIDC]
- Fraud Analysts & Risk Managers -> Case Management Service [HTTPS, TLS 1.3]
- AWS Application Load Balancer (ALB) -> Scoring Engine [gRPC/HTTPS over TLS]
- AWS Application Load Balancer (ALB) -> Case Management Service [HTTPS]
- Scoring Engine -> Amazon DynamoDB [TCP]
- Scoring Engine -> AWS S3 Object Lock [AWS API]
- Real-Time Payment Fraud Screening System -> AWS S3 Object Lock [AWS QLDB / S3 API]

## Technology Stack
- AWS Application Load Balancer (ALB): Ingress routing with TLS 1.3 and WAF to eliminate API Gateway latency overhead.
- Java (Spring Boot / gRPC) on AWS ECS on Fargate: High-performance hot-path scoring engine meeting <50ms P99 latency.
- Node.js / React on AWS ECS on Fargate: Case management UI ensuring analysts never access raw card data.
- Amazon DynamoDB: Low-latency feature store for transaction evaluation.
- AWS S3 Object Lock: Tamper-evident 7-year audit storage with S3 Lifecycle policies for cost efficiency.
- AWS Cognito: Identity provider handling OAuth2/OIDC and MFA.

## Rationale
- The architecture uses serverless container infrastructure on AWS to meet strict P99 latency (<50 ms at 3,000 TPS) and PCI-DSS Level 1 compliance requirements. 
- It balances high availability and tamper-evident 7-year auditability within a fixed 25,000 EUR monthly budget operated by a three-engineer team.