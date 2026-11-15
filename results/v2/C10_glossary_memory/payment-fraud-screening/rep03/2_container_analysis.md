## Overview
The Real-Time Payment Fraud Screening system evaluates card-not-present payment authorizations for fraud, returning approve, decline, or review decisions while providing case management for fraud analysts. It runs on AWS in the eu-west-1 region, meeting PCI-DSS Level 1 compliance within a 25,000 EUR monthly budget.

## Key Elements
- Cardholders / Merchants
- Fraud Analysts & Risk Managers
- Payment Gateway / Acquirer
- AWS Application Load Balancer (ALB)
- AWS ECS on Fargate (Scoring Engine and Case Management Service containers)
- Amazon DynamoDB
- AWS S3 Object Lock
- AWS Cognito

## Relationships
- Payment Gateway / Acquirer -> AWS Application Load Balancer (gRPC/HTTPS over mTLS)
- Fraud Analysts & Risk Managers -> Case Management Service (HTTPS, TLS 1.3 via AWS Cognito OAuth2/MFA)
- Scoring Engine -> Amazon DynamoDB (TCP for sub-10ms feature retrieval)
- Scoring Engine -> AWS S3 Object Lock (AWS API for asynchronous tamper-evident audit logging)

## Technology Stack
- AWS Application Load Balancer: Ingress layer providing low-latency routing without API Gateway overhead.
- Java (Spring Boot / gRPC) on AWS ECS on Fargate: Stateless scoring engine meeting <50ms P99 latency at 3,000 TPS.
- Node.js / React on AWS ECS on Fargate: Case management UI ensuring analysts never access raw card data.
- Amazon DynamoDB: Low-latency feature store for transaction evaluation.
- AWS S3 Object Lock: Tamper-evident 7-year audit storage replacing QLDB to minimize operational overhead.
- AWS Cognito: Identity provider handling OAuth2/OIDC and MFA for internal users.

## Rationale
This architecture achieves sub-50ms latency at 3,000 TPS within a fixed 25,000 EUR monthly budget by using stateless Fargate containers and direct ALB routing. It satisfies strict compliance, security, and 7-year auditability requirements via tokenization, S3 Object Lock, and an operational footprint manageable by a three-engineer team.