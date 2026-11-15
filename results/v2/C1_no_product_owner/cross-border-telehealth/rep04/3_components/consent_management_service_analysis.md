## Overview
[The Consent Management Service is an internal microservice responsible for enforcing granular, purpose-based data-sharing rules, managing GDPR and HIPAA compliance, and validating inline consent. It operates across regionally isolated Google Kubernetes Engine clusters to strictly enforce data residency.]

## Key Elements
- **Consent API Handler**: Go/gRPC server managing ingress and validation requests
- **Consent Policy Engine**: Evaluates RBAC, ABAC, and GDPR/HIPAA compliance rules
- **Audit Logger Component**: Emits cryptographically verifiable immutable access logs
- **Consent Repository Adapter**: Interfaces with regional Cloud SQL PostgreSQL instances
- **Cache Invalidation Subsystem**: Manages eventual consistency for the local Ristretto cache
- **GCP Pub/Sub**: Relays regional cache invalidation events securely

## Relationships
- API Gateway -> Consent API Handler: Validates inline consent via [gRPC over mTLS]
- Consent API Handler -> Consent Policy Engine: Evaluates rules via [In-memory Go function calls]
- Consent Policy Engine -> Consent Repository Adapter: Reads and writes policies via [gRPC/SQL]
- Consent Repository Adapter -> Cloud SQL PostgreSQL: Executes region-isolated queries via [pgx / TLS-secured SQL]
- Consent API Handler -> Audit Logger Component: Emits security audit logs via [gRPC]
- Cache Invalidation Subsystem -> GCP Pub/Sub: Publishes and consumes hashed revocation events via [Pub/Sub protocol]

## Technology Stack
- **Go**: Chosen for high-throughput, low-latency gRPC processing and concurrency model
- **gRPC / Protocol Buffers**: Used for fast, strongly typed internal service communication
- **Istio Service Mesh**: Enforces mTLS and strict service-to-service security
- **Cloud SQL PostgreSQL**: Provides region-isolated persistent storage with strict data residency
- **Ristretto**: In-memory caching with short TTL for sub-15ms p99 latency targets
- **GCP Pub/Sub**: Propagates cache invalidation events regionally without leaking PII

## Rationale
[This architecture satisfies strict data residency and privacy mandates (GDPR/HIPAA) by isolating components and state within regional GCP zones (`europe-west3` and `us-central1`). It meets demanding performance goals (<15ms p99 latency) via regional caching while maintaining data integrity through cryptographic verification and secure audit logging.]