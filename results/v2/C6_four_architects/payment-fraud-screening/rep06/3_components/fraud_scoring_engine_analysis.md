## Overview
The Fraud Scoring Engine is a high-performance Go component that screens 3,000 card-not-present payment authorizations per second for fraud under 50ms P99 latency. It processes real-time evaluations while maintaining PCI-DSS Level 1 compliance and immutable audit trails.

## Key Elements
* gRPC Interface Controller (Go gRPC server)
* Tokenization Filter (Go middleware utility)
* Feature Aggregator (Go goroutines and channels)
* Scoring Evaluator (Go with embedded WebAssembly / Starlark)
* Model Hot-Swapper (Go background worker)
* Audit Event Publisher (Go buffered channel worker pool)

## Relationships
* gRPC Interface Controller -> Tokenization Filter: Sanitizes inbound payment payload [In-process Function Call]
* Tokenization Filter -> Feature Aggregator: Forwards tokenized request context [In-process Function Call]
* gRPC Interface Controller -> Scoring Evaluator: Passes features for scoring [In-process Function Call]
* Feature Aggregator -> Amazon ElastiCache (Redis): Queries feature data [TCP/TLS]
* Model Hot-Swapper -> Scoring Evaluator: Updates active model reference [Thread-safe atomic pointer swap]
* Scoring Evaluator -> Audit Event Publisher: Emits decision payload and metadata [Buffered Go Channel]
* Audit Event Publisher -> Amazon SQS / SNS: Publishes audit events [AWS SDK / HTTPS]

## Technology Stack
* Go: Chosen for superior concurrency primitives (goroutines, channels) and low memory footprint to hit sub-50ms latency.
* gRPC: Provides high-throughput, low-latency inter-service communication.
* Amazon ElastiCache (Redis): Delivers fast in-memory feature data retrieval.
* WebAssembly / Starlark: Enables in-memory execution of scoring rules.
* Amazon SQS / SNS: Handles asynchronous, decoupled audit event publishing.

## Rationale
This architecture uses Go concurrency and in-memory evaluation to meet stringent performance requirements without exceeding the 25,000 EUR monthly AWS budget. Decoupled asynchronous auditing and strict boundary tokenization ensure compliance with PCI-DSS Level 1 and 7-year auditability rules.