## Overview
The Real-Time Payment Fraud Screening system screens card-not-present payment authorizations for fraud prior to approval and provides a case management portal for fraud analysts. It is built to maintain PCI-DSS Level 1 compliance and a 50 ms P99 latency threshold under high transaction volumes.

## Key Elements
- Decision API Container (Go, AWS Fargate)
- Scoring Engine Container (Python, FastAPI, AWS Fargate)
- Case Management Portal Container (AWS Fargate)
- Amazon Aurora PostgreSQL
- Inference API Controller (Python, FastAPI)
- Model Registry Sync Agent (Python)
- Model Execution Engine (Python, ONNX Runtime / Triton Inference Server)
- Feature Extraction Component (Python)
- Explanation Generation Component (Python)
- AWS Audit & Compliance Store
- CI/CD & Model Registry Pipeline

## Relationships
- Decision API Container -> Scoring Engine Container [Internal VPC gRPC / mTLS]
- Inference API Controller -> Feature Extraction Component [In-Memory Function Call]
- Inference API Controller -> Model Execution Engine [In-Memory Function Call / ONNX Runtime C-API]
- Model Execution Engine -> Explanation Generation Component [In-Memory Function Call]
- Model Registry Sync Agent -> CI/CD & Model Registry Pipeline [HTTPS / S3 API]
- Scoring Engine Container -> AWS Audit & Compliance Store [HTTPS / S3 API]

## Technology Stack
- AWS Fargate with Graviton2 (ARM64): Optimizes price-performance for containerized workloads within budget.
- Python, FastAPI, and ONNX Runtime / Triton Inference Server: Ensures high-throughput, low-latency machine learning model inference.
- Go: Powers the Decision API Container for high-performance authorization handling.
- Amazon Aurora PostgreSQL: Provides reliable transactional storage for case management.
- AWS KMS: Secures private keys for cryptographic audit signing.

## Rationale
This architecture uses ONNX Runtime on ARM64 AWS Fargate to meet the stringent 50 ms P99 latency requirement at high throughput. Asynchronous explanation offloading and strict memory zeroization ensure compliance with PCI-DSS Level 1 and 7-year tamper-evident audit mandates.