## Overview
The Fraud Scoring Engine is a low-latency microservice that screens card-not-present payment authorizations for fraud, providing real-time approve, decline, or review decisions. It ensures PCI-DSS compliance, explainable auditability, and business continuity for payment processing operations.

## Key Elements
- API Handler Component (Spring WebFlux / Netty)
- Feature Enriched Component (Embedded Caffeine cache and Redis client)
- Inference Engine Component (Embedded ONNX Runtime with Java bindings)
- Explainability Formatter Component
- Circuit Breaker & Fallback Component (Resilience4j)
- Audit Logger Component (SHA-256 hashing)

## Relationships
- API Handler -> Circuit Breaker Component: Manages execution flow [Direct method call]
- Feature Enriched Component -> Inference Engine Component: Passes tensor features [Direct memory transfer]
- Inference Engine Component -> Explainability Formatter Component: Passes raw tensors [Direct memory transfer]
- Inference Engine Component -> Audit Logger Component: Emits decision record [Blocking queue]

## Technology Stack
- Java / Spring Boot: Chosen for high-throughput, low-latency microservice execution on AWS ECS Fargate.
- ONNX Runtime: Provides embedded machine learning model inference to meet the sub-50ms latency constraint.
- Caffeine & Redis: Delivers high-performance in-memory feature caching and velocity counting.
- Resilience4j: Implements circuit breaking for fault tolerance and R-07 fail-open compliance.
- SHA-256: Generates cryptographic hashing for tamper-evident audit logs.

## Rationale
This architecture uses embedded runtimes and in-memory caching to consistently achieve P99 latency below 50 ms at 3,000 TPS within budget constraints. Built-in resilience patterns and cryptographic auditing ensure strict regulatory compliance and operational safety for a small engineering team.