## Overview
The Cross-Border Telehealth Platform provides video consultations, e-prescriptions, and an AI symptom checker for EU and US patients. It enforces strict regional data residency and regulatory compliance under GDPR, HIPAA, and EU MDR.

## Key Elements
- Patients
- Licensed Clinicians
- Compliance Officers
- Video Infrastructure Provider
- AI Inference Engine
- Regional Pharmacy Gateways
- Identity & Consent Providers
- API Gateway / BFF (Node.js/GraphQL)
- Consultation & Prescriptions Service (Go/gRPC)
- AI Traceability & Logging Service (Python/FastAPI)
- Consent & Policy Engine (Go/OPA)
- Patient Portal App (Flutter/Web & Mobile)
- Clinician Workspace App (React/TypeScript SPA)

## Relationships
- Patients -> API Gateway / BFF (HTTPS, WebSockets)
- Licensed Clinicians -> API Gateway / BFF (HTTPS, WebSockets)
- Compliance Officers -> API Gateway / BFF (HTTPS)
- Cross-Border Telehealth Platform -> Video Infrastructure Provider (HTTPS, WebSockets (WSS), SRTP/DTLS)
- Cross-Border Telehealth Platform -> AI Inference Engine (HTTPS (REST/gRPC))
- Cross-Border Telehealth Platform -> Regional Pharmacy Gateways (HTTPS (HL7 FHIR / National APIs))
- Cross-Border Telehealth Platform -> Identity & Consent Providers (OIDC/OAuth2 with FIDO2/WebAuthn)
- API Gateway / BFF -> Consultation & Prescriptions Service (gRPC over TLS via SPIFFE/SPIRE)

## Technology Stack
- GCP (europe-west3, us-central1): Target cloud infrastructure ensuring regional data residency.
- Node.js / GraphQL: API Gateway / BFF for efficient client-driven data fetching.
- Go / gRPC: High-performance backend microservices and secure inter-container communication.
- Python / FastAPI: AI Traceability & Logging Service for ML integration and auditing.
- Go / OPA: Fine-grained ABAC enforcement for patient consent validation.
- Flutter / React & TypeScript: Cross-platform patient and clinician client applications.

## Rationale
The architecture decouples regional frontends and backend services to strictly enforce data residency within GCP `europe-west3` and `us-central1`. Microservices communicate securely via gRPC over mTLS while adapting to diverse US (HL7 FHIR) and EU national interoperability standards.