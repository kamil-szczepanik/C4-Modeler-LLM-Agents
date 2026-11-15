## Overview
The Real-Time Payment Fraud Screening system screens card-not-present payment authorizations for fraud under strict latency and compliance constraints. It evaluates transactions in real time and provides case management tools for fraud analysts.

## Key Elements
- **API Router & Validator (Go):** Validates incoming gRPC payloads and enforces schema integrity.
- **Feature Assembler (Go):** Queries DynamoDB for user and card velocity features with parallelized execution.
- **Inference & Rules Evaluator (Rust):** Executes compiled machine learning models and dynamic rule sets concurrently.
- **Model Loader Component (Rust):** Handles S3 event notifications, cryptographic signature verification, and atomic in-memory model hot-swapping.
- **Audit Dispatcher (Go):** Asynchronously emits cryptographically signed, tamper-evident audit records.
- **External Dependencies:** AWS API Gateway / ALB, Amazon DynamoDB, Rule & Model Registry (Amazon S3), Amazon Kinesis Data Streams / AWS S3 Firehose, WORM Compliance Storage.

## Relationships
- **AWS API Gateway / ALB -> API Router & Validator:** Routes incoming authorization requests via [mTLS / gRPC].
- **Feature Assembler -> Amazon DynamoDB:** Reads and writes feature stores and transaction data using [AWS SDK].
- **Model Loader Component -> Rule & Model Registry:** Receives S3 event notifications and fetches model artifacts via [HTTPS / AWS SDK].
- **Audit Dispatcher -> Amazon Kinesis Data Streams & AWS S3 Firehose:** Streams audit logs via [AWS SDK].
- **Audit Dispatcher -> WORM Compliance Storage:** Persists immutable compliance logs via [S3 Firehose].

## Technology Stack
- **Go & Rust (AWS ECS Fargate):** Go handles concurrent API routing and I/O tasks, while Rust guarantees zero garbage-collection pauses for sub-50ms P99 latency targets.
- **Amazon DynamoDB:** Stores feature stores and transaction data with AWS KMS encryption for low-latency lookups.
- **Amazon S3 & AWS KMS:** Stores model artifacts and audit data with cryptographic signature verification and KMS encryption.
- **Amazon Kinesis Data Streams & AWS S3 Firehose:** Streams immutable, cryptographically hashed audit logs to WORM storage.
- **OpenTelemetry & AWS CloudWatch:** Provides structured metrics and distributed tracing for operational observability within budget constraints.

## Rationale
This architecture combines Go and Rust on AWS ECS Fargate to predictably meet the strict sub-50ms P99 latency requirement at 3,000 TPS within a fixed 25,000 EUR monthly budget. Furthermore, event-driven cryptographic model loading and tamper-evident audit logging satisfy PCI-DSS Level 1 compliance and 7-year auditability mandates.