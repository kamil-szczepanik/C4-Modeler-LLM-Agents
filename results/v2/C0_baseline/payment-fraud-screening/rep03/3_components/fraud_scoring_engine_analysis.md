## Overview
The Real-Time Payment Fraud Screening system evaluates card-not-present payment authorizations to detect fraud prior to approval, while providing a case management interface for fraud analysts. It is designed to process 3,000 requests per second with strict latency, security, and auditability constraints.

## Key Elements
- Fraud Analyst / Risk Manager (User)
- API Gateway (Nginx / AWS ALB)
- Fraud Scoring Engine (Java / Quarkus with embedded ONNX Runtime)
- Case Management Service (Node.js / TypeScript)
- Audit & Compliance Ledger (Rust / Go with AWS KMS-backed signing)
- Data Store (AWS Aurora PostgreSQL & Amazon Redis)

## Relationships
- API Gateway -> Fraud Scoring Engine: Forwards scoring requests via gRPC over TLS (mTLS)
- Fraud Scoring Engine -> Amazon Redis: Performs feature lookups via TCP (TLS)
- Fraud Scoring Engine -> Audit & Compliance Ledger: Emits signed audit payloads via gRPC
- Fraud Scoring Engine -> Case Management Service: Feeds review decisions and risk factor summaries via internal event streams

## Technology Stack
- Java / Quarkus: Chosen for build-time optimization and low memory footprint to meet sub-50ms latency
- ONNX Runtime: Embedded locally in the scoring engine to execute models without network hops
- AWS ECS (Fargate): Provides cost-effective container orchestration within budget without Kubernetes overhead
- Amazon Aurora PostgreSQL & Redis: Provides relational persistence and low-latency feature caching

## Rationale
This architecture uses an embedded inference engine and lightweight container orchestration to meet strict performance and budget constraints. Distributed services are minimized to guarantee predictable sub-50ms P99 latencies while maintaining PCI-DSS Level 1 compliance and 7-year auditability.