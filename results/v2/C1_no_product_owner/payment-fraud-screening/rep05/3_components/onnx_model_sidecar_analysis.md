## Overview
The Real-Time Payment Fraud Screening system evaluates card-not-present payment authorizations to detect fraud and manage reviews. It ensures high-performance scoring and tamper-evident auditability within PCI-DSS and budget constraints.

## Key Elements
- Fraud Analysts and ML Engineers
- Payment Gateway / Core Processing System
- Card Schemes / Tokenization Service
- AWS API Gateway / ALB
- Fraud Scoring Engine (Go microservice on Amazon ECS Fargate)
- ONNX Model Sidecar (ONNX Runtime C++ API)
- Case Management App (Node.js/React monolith on ECS Fargate)
- Amazon DynamoDB and Amazon RDS PostgreSQL
- Amazon S3 with Object Lock
- Amazon EventBridge

## Relationships
- Fraud Scoring Engine -> ONNX Model Sidecar: Sends feature tensors for scoring [`Unix Domain Sockets (UDS) gRPC`]
- Model Hot-Loader Component -> Amazon S3: Downloads `.onnx` model and signature manifest [`HTTPS / TLS 1.3`]
- Ingress -> AWS API Gateway / ALB: Routes incoming authorization traffic [`HTTPS`]

## Technology Stack
- AWS ECS Fargate: Container orchestration within the 25,000 EUR monthly budget constraint.
- ONNX Runtime (C++ API): High-performance execution runtime avoiding garbage collection pauses to meet P99 < 50ms latency.
- Amazon DynamoDB & RDS PostgreSQL: Scalable persistence for case management and immutable audit trails.
- Amazon S3 with Object Lock: Tamper-evident 7-year retention storage for decisions and models.

## Rationale
This architecture leverages lightweight sidecar patterns and Unix Domain Sockets to achieve sub-50ms fraud scoring latency on AWS Fargate. Strict security hardening, scoped IAM roles, and cryptographic model verification ensure full PCI-DSS compliance and robust auditability.