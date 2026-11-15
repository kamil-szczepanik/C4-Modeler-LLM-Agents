## Overview
The Fraud Scoring Engine evaluates real-time payment authorization requests for fraud using a high-performance Go microservice deployed on AWS. It delivers sub-50ms decisions at 3,000 TPS while ensuring PCI-DSS Level 1 compliance and 7-year tamper-evident auditing.

## Key Elements
* API Handler (Go): Manages ingress validation, sanitization, and mTLS termination.
* Feature Assembler (Go): Fetches real-time behavioral features concurrently with built-in circuit breakers.
* Rule Engine (Go): Evaluates deterministic business rules in-memory to bypass ML inference.
* Inference Client (Go): Interfaces with the ONNX Model Sidecar via localhost gRPC.
* Audit Logger (Go): Asynchronously signs and records decision payloads via AWS KMS.
* ONNX Model Sidecar (ONNX Runtime): Executes machine learning model scoring.

## Relationships
* AWS API Gateway / ALB -> API Handler: Routes incoming payment requests [HTTPS/mTLS]
* API Handler -> Rule Engine / Feature Assembler: Passes sanitized transaction data [In-memory function calls]
* Feature Assembler -> Amazon DynamoDB: Queries behavioral features and audit logs [AWS SDK / TLS]
* Inference Client -> ONNX Model Sidecar: Executes model inference queries [localhost gRPC]
* Audit Logger -> Amazon S3 with Object Lock: Persists signed audit trails [AWS SDK / TLS]
* Fraud Scoring Engine -> Amazon EventBridge: Emits decision events [API / Event Bus]

## Technology Stack
* Go: Chosen for concurrency model (goroutines) and low memory footprint to hit sub-50ms latency targets.
* ONNX Runtime: Provides lightweight, high-performance machine learning model execution.
* Amazon ECS Fargate: Runs containers without server management to fit the 3-engineer operational capacity.
* Amazon DynamoDB: Delivers predictable single-digit millisecond latency for feature retrieval.
* Amazon S3 with Object Lock & AWS KMS: Ensures tamper-evident, encrypted 7-year audit storage.
* AWS Application Auto Scaling: Manages traffic spikes dynamically to maintain performance under budget constraints.

## Rationale
This architecture uses Go and containerized services on AWS Fargate to meet strict sub-50ms P99 latency and high-throughput requirements within a 25,000 EUR monthly budget. Security and compliance controls—including tokenization, mTLS, and AWS KMS-signed audit logs—satisfy PCI-DSS Level 1 and 7-year audit retention mandates.