## Overview
The architecture defines a real-time payment fraud screening system for a payment processor on AWS eu-west-1. It screens card-not-present transactions, enforces sub-50ms P99 latency, and supports analyst reviews.

## Key Elements
- ML Inference Service (Python with ONNX Runtime on AWS ECS Fargate)
- gRPC API Handler (Python gRPC/Protobuf)
- Model Execution Engine (Python with ONNX Runtime)
- Feature Preprocessor (Python NumPy/Pandas)
- Model Loader (Python Boto3)
- Explainability Component (ONNX-native TreeEnsemble Explainers)
- Telemetry & Audit Emitter (Python AWS SDK)
- Case Management Backend (Go on AWS ECS Fargate)
- Case API Handler, Case Orchestrator, Audit & Notification Publisher (Go)
- Supporting AWS Services: Amazon API Gateway, Amazon ECS Fargate, Amazon ElastiCache Redis, Amazon DynamoDB, Amazon S3 Object Lock, Amazon EventBridge, Amazon CloudFront and S3

## Relationships
- Real-Time Scoring Engine -> ML Inference Service: Requests ML model inference [Internal gRPC]
- Real-Time Scoring Engine -> gRPC API Handler: Sends feature vectors [gRPC]
- Model Loader -> ML Model / Rule Registry: Fetches updated model binaries [HTTPS]
- Model Execution Engine -> Explainability Component: Calculates lightweight tree path attributions [In-memory Python call]
- Model Execution Engine -> Telemetry & Audit Emitter: Dispatches audit payload [Async queue]
- Fraud Analyst Frontend -> Case API Handler: Manages suspicious cases [HTTPS/REST]
- Case Orchestrator -> Amazon DynamoDB: Persists case updates and decisions [AWS SDK]

## Technology Stack
- AWS ECS Fargate: Provides scalable, serverless container execution within the 25,000 EUR monthly budget.
- Python with ONNX Runtime: Delivers C++ level execution speed and low memory footprint for sub-50ms inference.
- Go: Powers high-performance backend case management services.
- Amazon DynamoDB: Stores case data and audit trails with high availability and low latency.
- Amazon S3 Object Lock: Ensures tamper-evident, 7-year compliance audit logging.

## Rationale
The architecture strictly enforces PCI-DSS Level 1 compliance and sub-50ms P99 latency via asynchronous telemetry and optimized ONNX runtime execution. It operates reliably within a fixed 25,000 EUR monthly budget managed by a three-engineer team.