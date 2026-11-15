## Overview
This architecture defines a real-time payment fraud screening system for card-not-payments, processing 3,000 authorizations per second while enabling fraud analyst case reviews. It enforces PCI-DSS Level 1 compliance, maintains 7-year tamper-evident audit logs, and operates within a 25,000 EUR monthly AWS budget managed by three engineers.

## Key Elements
- Fraud Analyst UI (React SPA via Amazon S3 / CloudFront)
- Case Management Backend (Node.js / TypeScript)
- Real-Time Scoring Engine (Java / Spring Boot + ONNX)
- Case API Controller (Express.js / TypeScript)
- Case Workflow Service (TypeScript)
- Data Access Repository (Prisma ORM / TypeScript)
- Audit Logging Interceptor (TypeScript)
- Tokenization Gateway Client (Axios / TypeScript)
- Scoring API Controller (Spring WebFlux / Java)
- Feature Assembler (Java)
- Inference Executor (ONNX Runtime via JNI)
- Resilience & Fallback Handler (Resilience4j / Java)
- Amazon Aurora PostgreSQL
- Amazon ElastiCache (Redis)

## Relationships
- Fraud Analyst UI -> Case API Controller: Performs case reviews and workflow actions [HTTPS]
- Case API Controller -> Case Workflow Service: Invokes business logic [In-memory function calls]
- Case Workflow Service -> Audit Logging Interceptor: Dispatches audit events [Async/Sync method calls]
- Case Workflow Service -> Data Access Repository: Persists state changes [TypeScript/Prisma]
- Case Workflow Service -> Tokenization Gateway Client: Requests tokenized payload [HTTPS/REST]
- Data Access Repository -> Amazon Aurora PostgreSQL: Executes parameterized queries with optimistic locking [TLS/TCP]
- Scoring API Controller -> Resilience4j Fallback Handler: Wraps pipeline execution [In-memory]
- Feature Assembler -> Amazon ElastiCache: Fetches real-time profiles [TCP/Redis Protocol]
- Inference Executor -> ONNX Runtime: Executes fraud model [In-memory via JNI]

## Technology Stack
- AWS (eu-west-1): Provides a scalable cloud infrastructure within the fixed 25,000 EUR budget.
- Node.js & TypeScript: Powers the Case Management Backend for rapid development by a 3-engineer team.
- Java, Spring Boot, & Spring WebFlux: Delivers high-throughput, non-blocking I/O for sub-50ms P99 scoring latency.
- ONNX Runtime via JNI: Eliminates network serialization overhead for in-memory model execution.
- Resilience4j: Implements circuit breakers and fallbacks to satisfy the 1-minute availability constraint.
- Amazon Aurora PostgreSQL & Prisma ORM: Ensures type-safe data access and encrypted, auditable storage.

## Rationale
The architecture combines Node.js for maintainable case management workflows with Java and Spring WebFlux to meet stringent performance requirements. By leveraging in-memory ONNX execution and robust fallback mechanisms, it achieves high availability and low latency within the team and budget constraints.