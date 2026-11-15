## Overview
The Fraud Scoring Engine is a real-time Go-based microservice that evaluates payment authorization requests for fraud under 50ms P99 latency. It provides instantaneous approve, decline, or review decisions while maintaining PCI-DSS Level 1 compliance and 7-year tamper-evident auditability.

## Key Elements
- **API Handler Component**: Go `net/http` server receiving incoming requests, managing timeouts, and stripping raw card data (PANs).
- **Feature Fetcher & Cache Component**: In-memory LRU cache wrapping DynamoDB lookups with a localized circuit breaker.
- **Rule Engine Component**: In-memory deterministic rule evaluator using Go structs and ASTs.
- **Model Scorer Component**: ONNX Runtime Go bindings executing pre-loaded machine learning models.
- **Explanation Builder Component**: Synchronous assembler capturing rule matches, feature weights, and version tags.
- **Audit & Telemetry Dispatcher Component**: Go channels and worker pool flushing logs asynchronously.

## Relationships
- Network Load Balancer -> API Handler: Routes incoming payment authorization requests [mTLS]
- API Handler -> Feature Fetcher & Cache: Queries hot features [In-memory lookup [Sync]]
- API Handler -> Rule Engine & Model Scorer: Evaluates transaction risk [Direct Go Interface [Sync]]
- Rule Engine & Model Scorer -> Explanation Builder: Compiles match traces and importances [In-memory assembly [Sync]]
- Explanation Builder -> Audit & Telemetry Dispatcher: Passes compiled audit payload [Go Channels [Async]]
- Audit & Telemetry Dispatcher -> Audit Log Store (Amazon Aurora PostgreSQL): Writes ledger data [AWS SDK using IAM Roles / KMS Envelope Encryption]
- Audit & Telemetry Dispatcher -> Observability Service (AWS X-Ray / Container Insights): Emits metrics and traces [AWS SDK]

## Technology Stack
- **Go (`net/http`)**: Chosen for high-throughput, low-latency execution and minimal memory footprint.
- **ONNX Runtime Go Bindings**: Enables fast in-memory execution of machine learning models without external scoring latency.
- **Amazon ECS on EC2 (`c6i`)**: Provides predictable high-CPU compute performance within the fixed €25,000 monthly budget.
- **Amazon Aurora PostgreSQL**: Stores tamper-evident decision logs with ledger tables and cryptographic key rotation.

## Rationale
This component architecture achieves sub-50ms P99 latency at 3,000 TPS by offloading all I/O and audit logging to asynchronous Go channels while keeping scoring logic entirely in-memory. Strict container security hardening, IAM least-privilege, and KMS encryption satisfy PCI-DSS Level 1 and 7-year audit requirements without exceeding budget constraints.