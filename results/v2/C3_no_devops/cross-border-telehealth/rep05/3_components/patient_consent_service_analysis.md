## Overview
The Patient Consent Service manages granular, purpose-based data sharing consents for cross-border telehealth operations while enforcing strict GDPR and HIPAA compliance. It ensures low-latency evaluations and secure regional data residency across GCP deployments.

## Key Elements
- Consent API Controller (Go component)
- Consent Evaluation Engine (Go component)
- Audit & Ledger Writer (Go component)
- Cache Invalidation & Event Dispatcher (Go component)
- Ledger Storage Adapter (Go component)
- Redis Cache (In-memory storage)
- GCP Pub/Sub (Messaging service)
- Google Cloud Storage (WORM Object Storage)

## Relationships
- Consent API Controller -> Consent Evaluation Engine: Evaluates policies [In-process Go function calls]
- Consent Evaluation Engine <-> Redis Cache: Reads/writes cached consent states [RESP protocol over TLS]
- Consent API Controller -> Audit & Ledger Writer: Triggers async audit events [Go channels]
- Audit & Ledger Writer -> Ledger Storage Adapter: Writes immutable logs [HTTPS / Storage API]
- Cache Invalidation & Event Dispatcher -> GCP Pub/Sub: Publishes/subscribes to revocation events [gRPC]

## Technology Stack
- Go: Chosen for high concurrency, low memory overhead, and strict regional resource efficiency.
- Redis Cache: Provides in-memory lookups to eliminate database round-trips during consultations.
- GCP Pub/Sub: Enables instant, distributed cache invalidation and revocation event broadcasting.
- Google Cloud Storage (Object Lock / WORM): Guarantees tamper-proof compliance audit logging.
- Google Cloud KMS: Enforces customer-managed encryption keys (CMEK) for data at rest.

## Rationale
This component architecture enforces regional data residency and immutability while utilizing in-memory caching to eliminate latency during consultations. Decoupled async auditing and pub/sub cache invalidation ensure regulatory compliance without compromising user experience.