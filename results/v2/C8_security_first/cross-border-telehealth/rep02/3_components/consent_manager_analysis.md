## Overview
A cross-border telehealth platform providing video consultations, e-prescriptions, and an AI symptom checker for patients in the EU and US. It enforces strict regional data residency and compliance using isolated GCP cloud infrastructure.

## Key Elements
- Patients & Licensed Clinicians
- Istio Service Mesh & API Gateway (Istio)
- Backend-for-Frontend (BFF) (Node.js, GraphQL)
- Consent Manager (Containerized Service with Go / Gin, OPA, Fallback Policy Cache, Break-Glass Mediator)
- Regional WORM Storage (GCP Storage with regional key rings)
- AI Triage Service & Mediasoup SFU

## Relationships
- BFF -> Consent Manager: Validates user consent and compliance policies via gRPC over mTLS (Istio)
- Consent Manager -> Regional WORM Storage: Persists encrypted consent records and audit logs via HTTPS
- Consent API Router -> Fallback Policy Cache: Reads cached local consent states via In-Memory / Local Disk
- Break-Glass Mediator -> Regional WORM Storage: Persists immutable emergency access justifications via HTTPS

## Technology Stack
- GCP (`europe-west3`, `us-central1`): Ensures regional data residency for EU and US compliance
- Open Policy Agent (OPA): Evaluates dynamic GDPR/HIPAA compliance rules in real-time
- Go (Gin framework): Used for high-performance Consent Manager internal components
- GCP KMS: Provides regional envelope encryption for stored PII payloads
- SQLite: Powers the local fallback policy cache for unstable rural connections

## Rationale
Isolated regional deployments and OPA policy evaluation guarantee strict GDPR and HIPAA compliance while respecting data residency boundaries. Embedded fallbacks and break-glass mechanisms maintain availability and safety for rural or emergency scenarios without violating privacy constraints.