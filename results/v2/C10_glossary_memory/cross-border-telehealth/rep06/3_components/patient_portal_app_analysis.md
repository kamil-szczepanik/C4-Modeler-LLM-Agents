## Overview
A multi-region cross-border telehealth platform providing video consultations, e-prescriptions, and an AI symptom checker for EU and US patients on GCP. It enforces strict regional data residency and regulatory compliance under GDPR, HIPAA, and EU MDR.

## Key Elements
- Patients
- Licensed Clinicians
- Compliance Officers
- Video Infrastructure Provider
- AI Inference Engine
- Regional Pharmacy Gateways
- Identity & Consent Providers
- Patient Portal App (Flutter/Web & Mobile)
- Clinician Workspace App (React/TypeScript SPA)
- API Gateway / BFF (Node.js/GraphQL)
- Consultation & Prescriptions Service (Go/gRPC)
- AI Traceability & Logging Service (Python/FastAPI)
- Consent & Policy Engine (Go/OPA)

## Relationships
- Patients -> API Gateway / BFF (HTTPS, WebSockets)
- Licensed Clinicians -> API Gateway / BFF (HTTPS, WebSockets)
- Compliance Officers -> API Gateway / BFF (HTTPS)
- API Gateway / BFF -> Consultation & Prescriptions Service (gRPC over TLS with mTLS via SPIFFE/SPIRE)
- Consultation & Prescriptions Service -> Regional Pharmacy Gateways (HTTPS via HL7 FHIR in US / National APIs in EU)
- Cross-Border Telehealth Platform -> Video Infrastructure Provider (HTTPS, WebSockets, SRTP/DTLS)
- Cross-Border Telehealth Platform -> AI Inference Engine (HTTPS via REST/gRPC)
- Cross-Border Telehealth Platform -> Identity & Consent Providers (OIDC/OAuth2 with FIDO2/WebAuthn)

## Technology Stack
- Flutter (Web & Mobile): Powers the Patient Portal App for cross-platform support and offline caching.
- React & TypeScript: Used for the Clinician Workspace App single-page application.
- Node.js & GraphQL: Implements the API Gateway / BFF for efficient client-driven data fetching.
- Go & gRPC: Powers the Consultation & Prescriptions Service for high-performance backend microservice communication.
- Python & FastAPI: Powers the AI Traceability & Logging Service for machine learning integration and auditing.
- Go & OPA: Implements the Consent & Policy Engine for fine-grained ABAC enforcement.
- GCP (europe-west3 & us-central1): Cloud infrastructure ensuring regional data residency.

## Rationale
The microservices architecture on GCP enforces strict regional data residency by isolating data in `europe-west3` and `us-central1`. Decoupled services and offline-first client design ensure HIPAA/GDPR compliance and continuous availability in low-bandwidth rural environments.