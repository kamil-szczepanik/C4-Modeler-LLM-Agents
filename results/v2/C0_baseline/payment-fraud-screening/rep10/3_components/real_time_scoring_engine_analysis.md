## Overview
This system screens card-not-present payment authorizations for fraud in real-time while providing a portal for fraud analysts to review suspicious transactions. It ensures sub-50ms latency, PCI-DSS compliance, and zero-downtime model updates within a fixed cloud budget.

## Key Elements
- Real-Time Scoring Engine (AWS ECS Fargate, Go/Java, ONNX Runtime)
- Rule Evaluation Component (Go + expr-lang/expr)
- ML Inference Component (ONNX Runtime C++ bindings wrapped in Go)
- Decision Orchestrator Component
- Rule Compiler & Validator Component
- API Gateway & Routing Layer (AWS API Gateway / ALB)
- Audit & Event Stream (Amazon SQS / EventBridge + Kinesis Data Firehose)
- Decision Audit Store (AWS S3 Object Lock & AWS KMS)

## Relationships
- API Gateway & Routing Layer -> Real-Time Scoring Engine: Routes authorization payloads for scoring [mTLS / HTTPS]
- Real-Time Scoring Engine -> Audit & Event Stream: Streams scoring decisions and audit events [Amazon SQS / EventBridge]
- Real-Time Scoring Engine -> Third-Party Fraud Intelligence Feeds: Queries external threat intelligence [AWS PrivateLink]
- Rule Evaluation Component & ML Inference Component -> AWS S3: Hot-reloads models and rules atomically via S3 polling/notifications [HTTPS]

## Technology Stack
- AWS ECS Fargate: Container orchestration for cost-effective, serverless scaling within budget
- Go: High-performance language chosen for low memory overhead and sub-50ms latency
- ONNX Runtime: Optimized machine learning inference engine for fast model execution
- expr-lang/expr: Lightweight evaluation engine for fast in-memory fraud rule execution
- AWS S3 & KMS: Encrypted object storage with strict IAM controls for tamper-evident 7-year audit compliance

## Rationale
The architecture combines Go and ONNX Runtime on serverless AWS ECS Fargate to consistently deliver sub-50ms P99 decision latencies at high throughput. In-memory components, atomic S3 hot-reloading, and robust validation ensure continuous availability and seamless PCI-DSS compliance within the 25,000 EUR monthly budget.