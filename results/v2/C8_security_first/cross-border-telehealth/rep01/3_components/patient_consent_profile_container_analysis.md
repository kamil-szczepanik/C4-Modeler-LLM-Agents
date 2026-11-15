## Overview
[Cross-Border Telehealth Platform provides video consultations, e-prescriptions, and an AI symptom checker for EU and US patients. The architecture enforces strict regional data residency, GDPR/HIPAA compliance, and low-bandwidth availability.]

## Key Elements
* Patients and Clinicians
* Compliance Officer
* API Gateway / Ingress (Envoy / GCP HTTPS Load Balancer)
* Patient Consent & Profile Container (Go microservice)
* Data Tier (Cloud SQL PostgreSQL, Memorystore with CMEK)
* Messaging & Observability (Google Cloud Pub/Sub, OpenTelemetry, Cloud Audit Logs)

## Relationships
* API Gateway -> Patient Consent & Profile Container: Routes consent and profile management requests [gRPC over mTLS]
* Patient Consent & Profile Container -> Data Tier: Persists consent states, profiles, and audit logs [SQL with CMEK over internal GCP network]
* Patient Consent & Profile Container -> Messaging & Observability: Publishes and consumes revocation events [Google Cloud Pub/Sub]
* Revocation Manager -> Memorystore: Updates regional token blocklist [Redis protocol]

## Technology Stack
* Go / Fiber/Gin: Core implementation language and web framework for the consent microservice due to high concurrency and performance
* GCP Cloud KMS: Regional cryptographic key isolation (`europe-west3` and `us-central1`) for signing JWT consent receipts
* Google Cloud Pub/Sub: Asynchronous event messaging ensuring a <5-second revocation propagation SLO
* Redis Memorystore: Distributed caching for real-time token blocklist checks during authorization

## Rationale
[Regional data residency constraints (R-05) and compliance requirements (GDPR/HIPAA) are met through segregated GCP regions, regional KMS keys, and strict ABAC/ReBAC policy enforcement. Low-bandwidth availability (R-06) is achieved using cryptographically signed consent receipts and offline-resilient client caching to eliminate synchronous database bottlenecks.]