## Overview
The Cross-Border Telehealth Platform provides video consultations, e-prescriptions, and an AI symptom checker across the EU and US. It ensures strict data residency, EU MDR traceability, and resilience for rural users via GCP.

## Key Elements
- **Users**: Patients, Licensed Clinicians
- **External Systems**: AI Triage Engine, Local Pharmacies, Identity Providers (IdP)
- **Containers**: Istio Service Mesh, GraphQL BFF (Node.js), Mediasoup SFU, AI Triage Service, Consent Manager, E-Prescription Adapter, Regional WORM Storage (GCP Storage)
- **AI Triage Components**: API Controller (Node.js), Consent & Policy Enforcer (OPA/Rego), Inference Orchestrator (Python/LangChain), Audit & Cryptographic Signer (Python/Tink), Fallback & Circuit Breaker Manager (Python)

## Relationships
- **BFF -> AI Triage Service**: Sends triage requests [gRPC over mTLS, Istio]
- **AI Triage Service -> Consent Manager**: Verifies regional permissions [gRPC]
- **Inference Orchestrator -> AI Triage Engine**: Queries symptoms [HTTPS / gRPC]
- **Audit & Cryptographic Signer -> Regional WORM Storage**: Writes signed logs [HTTPS, GCP IAM]

## Technology Stack
- **Cloud Infrastructure**: GCP (`europe-west3` for EU, `us-central1` for US) ensuring strict regional data residency.
- **Networking & Security**: Istio for mTLS/AuthorizationPolicies, Google Tink for cryptographic log signing.
- **Backend & AI**: Node.js for API gateways and BFF, Python with LangChain for AI orchestration.
- **Policy & Resilience**: OpenAccess (OPA/Rego) for consent, custom async timeouts for rural fallback handling.

## Rationale
This architecture enforces regional data segregation to guarantee GDPR and HIPAA compliance while securing EU MDR audit trails via cryptographic signing. Additionally, circuit breakers and graceful fallbacks maintain platform availability for patients in rural areas with unstable connections.