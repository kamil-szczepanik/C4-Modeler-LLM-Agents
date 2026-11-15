## Overview
The Scoring Engine is a low-latency real-time fraud screening component that evaluates card-not-present payment authorizations to return approve, decline, or review decisions. It processes high-throughput traffic in AWS eu-west-1 while ensuring sub-50ms P99 latency and zero-downtime model updates.

## Key Elements
- **API Router**: Go service handling incoming gRPC requests.
- **Feature Aggregator**: Go concurrent routine orchestrator for feature store lookups and local caching.
- **Model Evaluator**: Go execution engine processing compiled rules and lightweight machine learning models.
- **In-Memory Model Registry**: Component managing zero-downtime hot-swapping of compiled WebAssembly models.
- **Audit Payload Builder**: Go component constructing tamper-evident decision records.
- **Feature Store**: Amazon DynamoDB storing real-time user and card velocity vectors.
- **Audit & Event Bus**: Amazon MSK (Apache Kafka) for asynchronous event publishing.

## Relationships
- *API Router* -> *Feature Aggregator*: Delegates feature retrieval [Go internal function call]
- *Feature Aggregator* -> *Feature Store*: Fetches velocity vectors [DynamoDB API, <10ms]
- *Model Evaluator* -> *In-Memory Model Registry*: Reads active scoring models [In-memory pointer reference, zero-allocation]
- *Model Evaluator* -> *Audit Payload Builder*: Passes decision context [Go internal channel]
- *Audit Payload Builder* -> *Audit & Event Bus*: Publishes tamper-evident payloads [Kafka Protocol, asynchronous batching]

## Technology Stack
- **Go**: Chosen for high concurrency, minimal garbage collection pause times, and sub-50ms P99 latency execution.
- **WebAssembly (WASM)**: Enables safe, dynamic, zero-downtime model and rule hot-reloads.
- **Amazon DynamoDB**: Provides single-digit millisecond latency for real-time feature lookups.
- **Amazon MSK (Kafka)**: Ensures reliable, asynchronous, decoupled event streaming for tamper-evident audit logs.

## Rationale
This architecture uses Go and in-memory caching to strictly satisfy the sub-50ms P99 latency requirement under high throughput. Decoupled asynchronous audit logging and WASM-based model hot-swapping guarantee zero downtime, 7-year auditability, and operational compliance within fixed resource budgets.