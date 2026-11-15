## Overview
- A multi-region cross-border telehealth platform providing video consultations, e-prescriptions, and an AI symptom checker for EU and US patients.
- Enforces strict regional data residency and regulatory compliance under GDPR, HIPAA, and EU MDR.

## Key Elements
- Patients
- Licensed Clinicians
- Compliance Officers
- Video Infrastructure Provider
- AI Inference Engine
- Regional Pharmacy Gateways
- Identity & Consent Providers
- API Gateway / BFF
- Consultation & Prescriptions Service
- AI Traceability & Logging Service
- Consent & Policy Engine
- Patient Portal App
- Clinician Workspace App

## Relationships
- Patients -> Cross-Border Telehealth Platform via HTTPS, WebSockets
- Licensed Clinicians -> Cross-Border Telehealth Platform via HTTPS, WebSockets
- Compliance Officers -> Cross-Border Telehealth Platform via HTTPS
- Cross-Border Telehealth Platform -> Video Infrastructure Provider via HTTPS, WebSockets (WSS), SRTP/DTLS
- Cross-Border Telehealth Platform -> AI Inference Engine via HTTPS (REST/gRPC)
- Cross-Border Telehealth Platform -> Regional Pharmacy Gateways via HTTPS (HL7 FHIR / National APIs)
- Cross-Border Telehealth Platform -> Identity & Consent Providers via OIDC/OAuth2 with FIDO2/WebAuthn
- API Gateway / BFF -> Consultation & Prescriptions Service via gRPC over TLS (mTLS via SPIFFE/SPIRE)
- Consultation & Prescriptions Service -> Regional Pharmacy Gateways via HTTPS (HL7 FHIR in US / National APIs in EU)

## Technology Stack
- GCP (`europe-west3`, `us-central1`): Ensures regional data residency per compliance mandates.
- Node.js/GraphQL: Powers the API Gateway / BFF for efficient client-driven data fetching.
- Go/gRPC: Drives high-performance backend microservices and inter-container communication.
- Python/FastAPI: Powers the AI Traceability & Logging Service for machine learning integration and auditing.
- Go/OPA: Enforces fine-grained ABAC for patient consent validation.
- Flutter & React/TypeScript: Optimizes client applications for multi-standard records and offline caching.

## Rationale
- The architecture isolates regional workloads in GCP to strictly fulfill GDPR and HIPAA data residency mandates.
- Decoupled microservices and robust outbox patterns ensure high availability and offline resilience for users with unstable rural internet connections.