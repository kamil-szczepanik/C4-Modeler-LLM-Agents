## Overview
The Real-Time Payment Fraud Screening Platform evaluates card-not-present payment authorizations to protect merchant revenue while ensuring strict PCI-DSS Level 1 compliance. It provides sub-50ms fraud scoring alongside case management and 7-year tamper-evident audit logging.

## Key Elements
- Payment Gateway / Processor Core
- Fraud Scoring API (Go, Embedded ONNX Runtime)
- API Router & Validator (Go)
- Feature Assembler (Go)
- Inference Engine (Go, Embedded ONNX Runtime)
- Audit Dispatcher (Go)
- Amazon SQS FIFO Queue
- Amazon S3 Object Lock
- Case Management Backend (Node.js) & Case Management UI (React)
- Audit & Event Store (AWS Aurora PostgreSQL)
- AWS ECS on AWS Fargate & AWS Network Load Balancer (NLB)

## Relationships
- Payment Gateway / Processor Core -> Fraud Scoring API: Routes authorization requests [gRPC / mTLS]
- API Router & Validator -> Feature Assembler: Passes sanitized request and correlation ID [Go method call]
- Feature Assembler -> Inference Engine: Passes assembled feature vector [Go method call]
- Inference Engine -> Audit Dispatcher: Emits scoring result, explanation, and model version [Go channel / async]
- Audit Dispatcher -> Amazon SQS FIFO: Offloads signed audit payloads [AWS SDK / HTTPS]
- Amazon SQS FIFO -> Amazon S3 Object Lock: Batches immutable audit logs [AWS SDK / HTTPS]
- Fraud Scoring Audit -> Audit & Event Store: Persists structured relational case data [TCP/TLS]

## Technology Stack
- Go: Chosen for high-throughput, low-latency performance and minimal memory footprint.
- Embedded ONNX Runtime: Executes machine learning models locally in-process to maintain P99 decision latency below 50 ms.
- AWS ECS on AWS Fargate: Provides container orchestration within the 25k EUR budget without managing underlying servers.
- Amazon S3 Object Lock (Compliance Mode): Delivers cost-effective, cryptographically secure WORM storage satisfying 7-year auditability.
- AWS KMS: Handles envelope encryption for audit payloads and model integrity.

## Rationale
This architecture decouples the high-throughput, low-latency scoring hot path from analytical storage using asynchronous queues and in-process execution, ensuring the system meets strict performance and budget constraints. Cryptographic signing and S3 Object Lock guarantee uncompromised 7-year auditability and PCI-DSS compliance.