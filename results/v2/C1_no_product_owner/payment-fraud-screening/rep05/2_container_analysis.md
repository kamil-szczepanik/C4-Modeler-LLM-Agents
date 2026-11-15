## Overview
[The Real-Time Payment Fraud Screening system screens card-not-present payment authorizations for fraud to approve, decline, or route them for analyst review. It maintains strict PCI-DSS compliance while processing 3,000 transactions per second under a 50ms P99 latency SLA.]

## Key Elements
- Payment Gateway / Core Processing System
- AWS API Gateway / ALB (Ingress)
- Fraud Scoring Engine (Go microservice on ECS Fargate)
- ONNX Model Sidecar container
- Case Management App (Node.js/React monolith on ECS Fargate)
- Amazon DynamoDB (Feature store and audit logs)
- Amazon RDS PostgreSQL (Case management data)
- Amazon S3 with Object Lock (7-year tamper-evident audit storage)
- Amazon EventBridge (Asynchronous event bus)

## Relationships
- Payment Gateway calls AWS API Gateway via gRPC over TLS
- Fraud Scoring Engine queries ONNX Model Sidecar via localhost gRPC
- Fraud Scoring Engine reads/writes features to DynamoDB via AWS SDK
- Fraud Scoring Engine emits decision events to Amazon EventBridge
- Fraud Analysts access Case Management App via HTTPS

## Technology Stack
- AWS ECS Fargate: Serverless container orchestration to minimize operational overhead for a 3-engineer team
- Go: Compiled language for the scoring engine to meet the <50ms P99 latency requirement
- ONNX Runtime: Lightweight model serving sidecar for seamless fraud model updates
- Amazon DynamoDB: Low-latency NoSQL data store for real-time feature lookups
- Amazon S3 Object Lock: Immutable storage satisfying 7-year audit retention within budget

## Rationale
[This serverless container architecture meets strict latency, compliance, and budget constraints by leveraging AWS managed services to minimize operational overhead for a three-engineer team. High availability, robust security controls, and immutable audit logging ensure PCI-DSS Level 1 compliance and fault tolerance.]