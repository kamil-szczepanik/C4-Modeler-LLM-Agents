## Overview
The Cross-Border Telehealth Platform provides secure video consultations, e-prescriptions, and an AI symptom checker for EU and US patients. It enforces strict regional data residency and regulatory compliance under GDPR, HIPAA, and EU MDR.

## Key Elements
- Patients
- Licensed Clinicians
- Compliance Officers
- API Gateway / BFF (Node.js/GraphQL)
- Consultation & Prescriptions Service (Go/gRPC)
- AI Traceability & Logging Service (Python/FastAPI)
- Consent & Policy Engine (Go/OPA)
- Patient Portal App (Flutter/Web & Mobile)
- Clinician Workspace App (React/TypeScript SPA)
- Policy Decision Point (PDP) [component] (Open Policy Agent)
- Consent Repository Proxy [component] (Go)
- Audit & Traceability Publisher [component] (Go)

## Relationships
- Patients -> API Gateway / BFF (HTTPS, WebSockets)
- Licensed Clinicians -> API Gateway / BFF (HTTPS, WebSockets)
- Compliance Officers -> API Gateway / BFF (HTTPS)
- API Gateway / BFF -> Consultation & Prescriptions Service (gRPC over TLS with mTLS via SPIFFE/SPIRE)
- API Gateway / BFF -> Policy Decision Point (gRPC over TLS with mTLS via SPIFFE/SPIRE)
- Policy Decision Point -> Consent Repository Proxy (Internal Go interface)
- Policy Decision Point -> Audit & Traceability Publisher (Asynchronous channel)
- Cross-Border Telehealth Platform -> Video Infrastructure Provider (HTTPS, WebSockets (WSS), SRTP/DTLS)
- Cross-Border Telehealth Platform -> AI Inference Engine (HTTPS (REST/gRPC))
- Consultation & Prescriptions Service -> Regional Pharmacy Gateways (HTTPS, HL7 FHIR in US / National APIs in EU)
- Cross-Border Telehealth Platform -> Identity & Consent Providers (OIDC/OAuth2 with FIDO2/WebAuthn)

## Technology Stack
- GCP (regions: europe-west3, us-central1): Cloud infrastructure provider ensuring regional data segregation.
- Google Kubernetes Engine (GKE): Container orchestration for zonal regional deployments.
- Open Policy Agent (OPA) / Rego: Sub-millisecond ABAC and purpose-based consent evaluation via sidecars.
- Cloud Spanner: Regional datastores enforcing data residency (R-05).
- Cloud KMS & WORM Storage: Encryption at rest using CMEK and immutable retention buckets for audit logs.

## Rationale
This architecture uses localized Open Policy Agent sidecars to achieve sub-millisecond policy evaluations without cross-region latency during consultations. It enforces strict data residency and immutable audit logging to satisfy GDPR, HIPAA, and EU MDR requirements.