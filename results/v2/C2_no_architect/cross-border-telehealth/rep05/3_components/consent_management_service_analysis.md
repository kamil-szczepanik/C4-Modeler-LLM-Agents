## Overview
The Consent Management Service is a core container of the Cross-Border Telehealth Platform responsible for enforcing granular data-sharing consents and regional compliance. It operates in Google Cloud Platform (`europe-west3` and `us-central1`) to support GDPR and HIPAA requirements.

## Key Elements
- Patients
- Licensed Clinicians
- Compliance/Legal Officers
- API Gateway
- Consent Management Service
- Cloud Storage (WORM / Object Retention)
- Cloud KMS

## Relationships
- Patients & Clinicians -> API Gateway: Manages consents, video consultations, and e-prescriptions [HTTPS / TLS 1.3]
- API Gateway -> Consent Management Service: Validates user consent, authentication, and token exchange [mTLS / OAuth 2.0 / OIDC]
- Consent Management Service -> Cloud Storage: Streams immutable audit logs and consent history [Encrypted gRPC]
- Consent Management Service -> Cloud KMS: Encrypts consent records using region-isolated keys [Internal GCP API]

## Technology Stack
- OAuth 2.0 / OIDC: Standard protocol for authentication and fine-grained authorization
- JSON Web Tokens (JWT): Short-lived (<60s) cryptographically signed tokens for instant consent revocation
- Istio Service Mesh: Enforces strict mTLS and network policies for service-to-service communication
- Google Cloud KMS: Provides region-isolated encryption at rest with customer-managed encryption keys (CMEK)
- Cloud Storage with WORM: Ensures append-only, immutable audit logging for compliance mandates

## Rationale
This architecture fits requirements by strictly isolating consent records per region (`europe-west3` and `us-central1`) with cross-border replication disabled, satisfying strict data residency mandates (R-05). Additionally, fail-closed circuit breakers, short-lived JWTs, and multi-party cryptographic "break-glass" attestations guarantee robust security, immediate revocation, and compliance auditability.