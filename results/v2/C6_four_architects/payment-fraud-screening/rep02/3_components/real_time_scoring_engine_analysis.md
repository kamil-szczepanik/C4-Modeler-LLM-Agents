## Overview
The Real-Time Payment Fraud Screening system evaluates card-not-present payment authorizations to detect fraud and manage analyst reviews. It ensures sub-50ms P99 latency while maintaining PCI-DSS Level 1 compliance and 7-year auditability.

## Key Elements
- Scoring API Controller (`Java / Spring MVC`)
- Feature Aggregator (`Java / Spring Data`)
- Inference Engine (`Java + ONNX Runtime`)
- Decision Evaluator
- Model Hot-Swapper (`Java`)
- Audit Event Publisher (`Java / AWS SDK`)
- Circuit Breaker & Fallback Handler (`Resilience4j`)
- Amazon ElastiCache (Redis)
- Amazon Kinesis Data Streams

## Relationships
- API Gateway & Ingress -> Scoring API Controller: Ingests requests [gRPC over HTTP/2]
- Scoring API Controller -> Feature Aggregator: Fetches features [Direct Method Call]
- Feature Aggregator -> Amazon ElastiCache: Fetches user velocity profiles [RESP over TCP]
- Scoring API Controller -> Inference Engine: Invokes model inference [In-memory ONNX Runtime API]
- Inference Engine -> Decision Evaluator: Passes raw scores [Direct Method Call]
- Model & Rule Management Service -> Model Hot-Swapper: Pushes model binaries [gRPC / HTTPS]
- Model Hot-Swapper -> Inference Engine: Updates model reference [In-memory pointer swap]
- Decision Evaluator -> Audit Event Publisher: Enqueues logs [ConcurrentQueue]
- Audit Event Publisher -> Amazon Kinesis Data Streams: Publishes batched events [AWS SDK over HTTPS]
- Circuit Breaker & Fallback Handler -> Scoring API Controller: Wraps execution [AOP Interceptor]

## Technology Stack
- Java / Spring Boot: Core container framework matching the engineering team's expertise.
- ONNX Runtime: Executes machine learning models in-process via JNI for ultra-low latency.
- Resilience4j: Enforces circuit breaking and fallbacks to prevent upstream payment blocking.
- Amazon ElastiCache (Redis): Provides high-performance sub-10ms feature lookups.
- Amazon Kinesis Data Streams: Handles asynchronous, tamper-evident audit logging.

## Rationale
This architecture uses in-process ML inference and non-indirection caching to achieve sub-50ms latency without expensive remote scoring hardware. It respects the 3-person team limit and €25k monthly budget while meeting strict auditability and availability mandates.