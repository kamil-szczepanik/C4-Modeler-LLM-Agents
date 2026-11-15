## Overview
The Real-Time Payment Fraud Screening system processes card-not-present payment authorizations to detect and prevent fraud before approval while supporting real-time case management for analysts. It operates on AWS to meet strict performance, compliance, and budget requirements.

## Key Elements
- Cardholders / Merchants
- Fraud Analysts & Risk Managers
- Payment Gateway / Acquirer
- AWS Application Load Balancer (ALB)
- Scoring Engine (Java (Spring Boot / gRPC) on AWS ECS on Fargate)
  - gRPC Ingress Handler
  - Feature Evaluator Component
  - ML Inference & Rule Engine Component (with Shadow Evaluation Router)
  - Audit Dispatcher Component
- Case Management Service (Node.js / React on AWS ECS on Fargate)
- Amazon DynamoDB
- AWS S3 Object Lock
- AWS Cognito

## Relationships
- Payment Gateway / Acquirer -> AWS Application Load Balancer (ALB) via gRPC/HTTPS over mTLS
- Fraud Analysts & Risk Managers -> AWS Cognito via OAuth2/OIDC
- Fraud Analysts & Risk Managers -> Case Management Service via HTTPS (TLS 1.3)
- AWS Application Load Balancer (ALB) -> Scoring Engine via gRPC/HTTPS
- AWS Application Load Balancer (ALB) -> Case Management Service via HTTPS
- Scoring Engine -> Amazon DynamoDB via TCP
- Scoring Engine -> AWS S3 Object Lock via AWS API

## Technology Stack
- AWS ECS on Graviton2 Fargate: Minimizes OS patch management overhead while delivering predictable performance.
- Java (Spring Boot / gRPC) & ONNX Runtime: Provides high-throughput, low-latency transaction scoring and model inference.
- Amazon DynamoDB: Acts as a low-latency feature store for transaction evaluation.
- AWS S3 Object Lock: Ensures tamper-evident, 7-year audit storage.
- AWS Cognito: Handles secure identity management and authentication.

## Rationale
This architecture uses serverless containers on Graviton2 Fargate and managed AWS services to achieve <50ms P99 latency at 3,000 TPS within a 25,000 EUR monthly budget. It enforces PCI-DSS Level 1 compliance and 7-year tamper-evident auditability using isolated security controls and tokenized data flows.