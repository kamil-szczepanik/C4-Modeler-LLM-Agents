## Overview
The Real-Time Payment Fraud Screening system evaluates card-not-present payment authorizations for fraud to protect merchant revenue while complying with PCI-DSS Level 1. It screens transactions in real time, routes suspicious payments for analyst review, and securely audits all decisions.

## Key Elements
- **API Gateway**: AWS API Gateway (HTTP APIs) routing requests.
- **Scoring Engine Container**: Go and ONNX runtime running on Amazon ECS on AWS Fargate.
  - **API Router Component**: Handles gRPC-over-HTTP/2 requests and timeouts.
  - **Feature Enrichment Component**: Fetches velocity features via AWS ElastiCache (Redis `cache.t4g.micro`).
  - **Model Execution Engine**: Evaluates transactions using concurrent double-buffered models.
  - **Fallback & Circuit Breaker Component**: Enforces R-07 availability constraints.
  - **Audit & Telemetry Dispatcher**: Asynchronously flushes tamper-evident audit logs.
- **Storage & Auditing**: Amazon RDS PostgreSQL, Amazon S3 WORM Bucket & Model Bucket, Amazon SQS / EventBridge with DLQ, and Amazon Athena & S3 Data Lake.

## Relationships
- **API Gateway -> Scoring Engine Container**: Routes authorization scoring requests via gRPC over HTTP/2.
- **API Router Component -> Feature Enrichment Component**: Invokes feature lookup via Go interface.
- **Feature Enrichment Component -> Model Execution Engine**: Passes enriched feature vector via Go struct.
- **Model Execution Engine -> Fallback Component**: Intercepts timeouts and errors via Go context.
- **Scoring Engine Container -> Amazon S3 WORM Bucket & Model Bucket**: Loads models and uploads tamper-signed audit payloads via HTTPS with digital signatures.
- **Scoring Engine Container -> Amazon SQS / EventBridge**: Dispatches telemetry and audit records asynchronously.

## Technology Stack
- **Go (`net/http`)**: High-performance backend language chosen to meet the <50ms P99 latency requirement.
- **ONNX Runtime (C-Bindings)**: Executes compiled machine learning models in memory with zero-downtime hot-swapping.
- **Amazon ECS on AWS Fargate**: Container orchestration providing scalable compute within a fixed budget.
- **AWS ElastiCache (Redis `cache.t4g.micro`)**: Low-latency sliding-window feature store fitting the 25,000 EUR monthly budget.
- **Amazon S3 Object Lock**: Ensures 7-year tamper-evident auditability for compliance.

## Rationale
This architecture uses Go and ONNX on AWS Fargate to consistently deliver sub-50ms decision latencies at high throughput. It satisfies strict PCI-DSS Level 1 security, tamper-evident 7-year auditability, and zero-downtime model updates within a 25,000 EUR monthly budget operated by a 3-engineer team.