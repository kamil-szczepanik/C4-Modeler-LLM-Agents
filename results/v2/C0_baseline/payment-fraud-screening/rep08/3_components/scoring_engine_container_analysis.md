## Overview
Real-Time Payment Fraud Screening is a low-latency fraud detection system built to evaluate card-not-present payment authorizations and manage analyst reviews. It ensures strict PCI-DSS compliance and financial auditability while maintaining sub-50ms decision latencies.

## Key Elements
* API Gateway & Routing Layer (AWS API Gateway / ALB)
* Scoring Engine Container (Go or Rust on AWS Fargate)
* Case Management Container (Node.js / React SPA backend with Amazon RDS PostgreSQL)
* Audit & Event Store Container (Amazon DynamoDB & S3)
* Messaging Backbone (Amazon SQS / SNS)
* Model Storage & Management (Amazon S3 & AWS Secrets Manager)
* Internal Scoring Engine Components: Inbound API Handler, Feature Assembler, Execution Core (Wasmtime), Audit Publisher

## Relationships
* API Gateway & Routing Layer -> Scoring Engine Container: Routes scoring requests [gRPC with mTLS]
* Scoring Engine Container -> Model Storage & Management: Retrieves dynamic model weights [HTTPS (S3 API)]
* Scoring Engine Container -> Messaging Backbone: Publishes scoring events [HTTPS (SQS/SNS)]
* Feature Assembler -> Local Cache: Performs profile lookups [Embedded Go ristretto or Rust moka cache]
* Audit Publisher -> Messaging Backbone: Dispatches signed audit payloads [Non-blocking channels / SQS]

## Technology Stack
* Go or Rust: Chosen for memory safety, concurrency, and sub-50ms P99 latency performance.
* AWS Fargate: Selected over Spot instances to guarantee high availability and eliminate cold-start risks.
* Wasmtime (WebAssembly): Executes compiled scoring models securely within a metered runtime sandbox.
* Amazon SQS / SNS: Provides a reliable, decoupled asynchronous messaging backbone.
* AWS KMS: Supplies envelope signatures for tamper-evident audit logging and model verification.
* Amazon RDS (PostgreSQL): Powers the Case Management backend for relational analyst workflows.

## Rationale
This architecture balances ultra-low latency execution constraints with rigorous PCI-DSS Level 1 compliance and 7-year auditability. By utilizing memory-safe languages, isolated execution runtimes, and standard AWS Fargate capacity, the system guarantees high availability, rapid failure recovery, and precise budget control.