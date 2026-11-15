## Overview
The Patient Consent & Preference Service Container manages cross-border patient consent and preferences under strict regional isolation for the Cross-Border Telehealth Platform. It ensures compliance with GDPR and HIPAA by enforcing fine-grained, time-bound data access policies across the EU and US.

## Key Elements
- Patient Consent & Preference Service Container (Go on GKE)
- Consent API Router (`chi` framework)
- Consent Policy Engine
- Audit Logger with cryptographic chaining
- PostgreSQL Repository Layer (`pgx`)
- Consent Expiry Background Worker
- Regional Cloud SQL (PostgreSQL) and WORM Cloud Storage (GCP Cloud KMS)

## Relationships
- API Gateway -> Consent API Router: Queries and updates consent [gRPC over mTLS with JWTs]
- Consent Policy Engine -> PostgreSQL Repository Layer: Persists and evaluates consent states [PostgreSQL wire protocol with CMEK]
- Audit Logger -> Cloud Storage: Writes tamper-evident logs [Google Cloud Storage APIs]
- Consent Policy Engine -> Pub/Sub: Broadcasts state changes for cache invalidation [GCP Pub/Sub]

## Technology Stack
- Go: Chosen for high concurrency and performance in microservices.
- Google Kubernetes Engine (GKE): Container orchestration across `europe-west3` and `us-central1`.
- GCP Cloud SQL (PostgreSQL) with Row-Level Security: Enforces regional data residency.
- GCP Cloud KMS: Manages Customer-Managed Encryption Keys (CMEK) for data at rest.

## Rationale
This architecture guarantees strict regional data segregation, fulfilling GDPR and HIPAA compliance mandates. The internal design components ensure auditability, secure multi-tenant isolation, and automated lifecycle management of patient privacy consents.