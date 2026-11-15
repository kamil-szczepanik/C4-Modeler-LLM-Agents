## Overview
The EMR Service is a high-availability backend component of the Clinic Management System that manages electronic medical records, patient admissions, and audit trails. It ensures HIPAA and GDPR compliance while maintaining sub-second performance for clinical workflows.

## Key Elements
- EMR API Controller (Fastify Routing/Validation)
- Medical Record Manager (Domain Service)
- Audit Logger Interceptor (Middleware)
- Data Access Repository (Prisma ORM / Node.js)
- FHIR Mapping Adapter (Translation Layer)
- Redis Cache Sidecar
- CockroachDB (Database)
- RabbitMQ / Local Buffer (Audit Queue)
- HashiCorp Vault (Secrets & Key Management)

## Relationships
- API Gateway -> EMR API Controller: Routes internal API requests [gRPC over mTLS]
- EMR API Controller -> Medical Record Manager: Invokes business logic [In-memory function calls]
- Medical Record Manager -> Data Access Repository: Persists and retrieves records [SQL via TLS]
- Medical Record Manager -> Audit Logger Interceptor: Triggers audit events [Async Event Emission via Durable Audit Queue]
- Medical Record Manager -> FHIR Mapping Adapter: Transforms internal schemas [In-memory mapping]
- FHIR Interoperability Service -> FHIR Mapping Adapter: Exchanges standardized resources [gRPC with Circuit Breakers]
- Data Access Repository -> CockroachDB: Stores encrypted patient data [Encrypted SQL]

## Technology Stack
- Node.js / TypeScript (Fastify): Chosen for low-latency execution to meet the <1s P95 latency SLA.
- Prisma ORM: Encapsulates database interactions and enforces tenant isolation.
- CockroachDB: Provides active-active high availability and robust data retention capabilities.
- Redis: Acts as a caching sidecar for FHIR resources and demographics to protect performance SLAs.
- HashiCorp Vault: Manages dynamic column-level encryption keys and cryptographic signing secrets.
- ArgoCD / Kubernetes: Manages hybrid multi-cluster deployments across `eu-central-1` and `on-prem-k8s`.

## Rationale
This architecture decouples domain logic, secure auditing, and interoperability translation while embedding caching and circuit breakers to guarantee sub-second performance. Distributed resilience mechanisms and encryption controls satisfy strict 99.99% availability and HIPAA/GDPR compliance mandates.