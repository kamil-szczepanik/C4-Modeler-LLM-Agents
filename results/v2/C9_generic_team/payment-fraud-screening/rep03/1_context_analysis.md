## Overview
The system screens card-not-present payment authorizations for fraud in real-time and provides case management for fraud analysts. It is designed for a mid-size payment processor operating under strict compliance and budget constraints.

## Key Elements
- Payment Gateway (External source of authorization requests)
- Fraud Analysts (Internal users performing case reviews)
- ML Training Environment (External system for model updates)
- Ingress API Gateway (Traffic shaping and rate limiting)
- Real-Time Scoring Container (Stateless in-memory evaluation engine)
- Case Management Service (Analyst review backend)
- WORM Audit Store (Tamper-evident 7-year audit logging)
- Message Bus (Asynchronous decoupling pipeline)

## Relationships
- Payment Gateway to Ingress API Gateway via HTTPS/TLS 1.3
- Ingress API Gateway to Real-Time Scoring Container via gRPC
- Real-Time Scoring Container to Message Bus via AWS SQS
- Message Bus to WORM Audit Store via AWS S3 API (Object Lock)
- Analysts to Case Management Service via HTTPS/TLS 1.3

## Technology Stack
- AWS (Primary cloud provider in region eu-west-1)
- AWS ECS Fargate (Provisioned container compute for predictable latency without cold starts)
- AWS S3 Object Lock (Write-Once-Read-Many storage for 7-year tamper-evident audit trails)
- AWS SQS (Asynchronous message bus for decoupling scoring from audit logs)
- In-memory embedded ML runtime (For low-latency model evaluation)

## Rationale
The architecture prioritizes sub-50ms P99 latency at 3,000 TPS by using stateless, in-memory containerized scoring and asynchronous decoupling. It satisfies strict PCI-DSS Level 1 and 7-year auditability constraints within a €25,000 monthly budget while remaining maintainable for a three-engineer team.