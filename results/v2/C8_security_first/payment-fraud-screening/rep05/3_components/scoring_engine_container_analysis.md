## Overview
[The Scoring Engine Container provides automated, sub-50ms real-time fraud scoring for card-not-present payment authorizations using high-performance Rust components. It ensures PCI-DSS Level 1 compliance, secure in-memory data processing, and tamper-evident audit logging within a fixed AWS infrastructure budget.]

## Key Elements
* **API Listener Component**: Tonic gRPC server handling inbound TLS/mTLS traffic and zero-copy parsing.
* **Rule Engine Component**: In-memory WebAssembly (Wasm) evaluation engine for low-latency fraud scoring.
* **Fallback Heuristics Component**: Embedded static ruleset executing securely upon primary engine failure.
* **Model Manager Component**: Background worker handling zero-downtime model hot-reloads from AWS S3.
* **Telemetry & Version Injector Component**: Injects model version metadata and OpenTelemetry traces.
* **Audit Dispatcher Component**: Non-blocking, buffered channel pushing events to Amazon SQS.
* **AWS ECS Fargate**: Compute environment running containers with AWS Application Auto Scaling and Fargate Spot.

## Relationships
* **API Listener** -> **Rule Engine / Fallback Heuristics**: Evaluates requests via In-memory function call [Rust/gRPC]
* **Rule Engine & Fallback Heuristics** -> **Telemetry & Version Injector**: Passes scoring results and metadata [In-memory]
* **Scoring Engine Container** -> **Amazon SQS**: Pushes audit events asynchronously [AWS SDK / SQS]
* **Model Manager** -> **S3 Model Registry & S3 Object Lock**: Retrieves fraud scoring models [AWS S3 API]
* **Scoring Engine Container** -> **AWS KMS & AWS Secrets Manager**: Retrieves secrets and encryption config [AWS IAM / TLS]
* **Scoring Engine Container** -> **AWS X-Ray**: Exports OpenTelemetry traces [gRPC]

## Technology Stack
* **Rust**: Chosen for extreme performance, memory safety, and minimal resource footprint under the €25k budget.
* **WebAssembly (Wasm)**: Enables lightning-fast, sandboxed fraud rule evaluation under the 50ms latency threshold.
* **AWS ECS Fargate**: Provides serverless container orchestration with predictive autoscaling and cost control.
* **Amazon SQS**: Handles reliable, asynchronous audit event decoupling.
* **AWS S3 Object Lock**: Ensures tamper-evident, 7-year compliant audit storage.
* **OpenTelemetry & AWS X-Ray**: Delivers end-to-end distributed tracing and observability.

## Rationale
[This architecture strictly satisfies performance and compliance requirements by utilizing a memory-safe Rust runtime and Wasm rules for sub-50ms latency at scale. Security controls, zero-copy processing, and local fallback heuristics maintain PCI-DSS Level 1 compliance and fault tolerance without breaching the €25,000 monthly budget.]