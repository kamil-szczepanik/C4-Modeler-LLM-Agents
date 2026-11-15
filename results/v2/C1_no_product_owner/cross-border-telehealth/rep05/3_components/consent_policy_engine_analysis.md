## Overview
The Consent & Policy Engine is a Go-based regional service that enforces strict GDPR, HIPAA, and data residency compliance across GCP regions. It manages granular patient consents, validates cross-border access requests, and issues cryptographic capability tokens.

## Key Elements
- Policy Decision Point (PDP) (Go, Open Policy Agent / OPA)
- Consent Manager (Go, BigCache)
- Regional Residency Enforcer (Go)
- Residency Token Issuer (Go)
- GCP Cloud SQL (PostgreSQL)
- GCP Pub/Sub

## Relationships
- API Gateway -> Policy Decision Point: Evaluates access tokens and scopes [gRPC over mTLS]
- Policy Decision Point -> Consent Manager: Queries active patient consents [In-process Go function call]
- Consent Manager -> Cloud SQL: Persists consent state [PostgreSQL Protocol / TLS with GCP KMS]
- Policy Decision Point -> Residency Token Issuer: Requests scoped capability token [In-process Go function call]
- Consent & Policy Engine -> Immutable Audit Logging Service: Publishes cryptographically signed logs [gRPC over mTLS]
- Regional Residency Enforcer -> Regional Message Broker: Publishes policy violation alerts [GCP Pub/Sub]

## Technology Stack
- Go: Chosen for high-throughput, low-latency microservice implementation.
- Open Policy Agent (OPA): Embeds Rego policies for rapid, declarative access evaluations.
- GCP Confidential VMs (AMD SEV): Provides hardware-level memory encryption for cached patient consent data.
- BigCache: Delivers high-performance in-memory caching to maintain sub-5ms evaluation latencies.
- PostgreSQL / Cloud SQL: Secures persistent storage of regional consent records with GCP KMS.

## Rationale
Isolated regional deployments in `europe-west3` and `us-central1` enforce strict data residency constraints without cross-region dependencies. In-memory caching with hardware-level encryption balances low-latency requirements with rigorous security and compliance mandates.