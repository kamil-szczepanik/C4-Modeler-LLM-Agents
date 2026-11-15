## Overview
The Cross-Border Telehealth Platform is a multi-region telehealth system providing video consultations, e-prescriptions, and an AI symptom checker for EU and US patients. It enforces strict regional data residency and regulatory compliance under GDPR, HIPAA, and EU MDR.

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
- Regional Pharmacy Gateways
- Identity & Consent Providers
- Video Infrastructure Provider
- AI Inference Engine

## Relationships
- Patients -> API Gateway / BFF [HTTPS, WebSockets]
- Licensed Clinicians -> API Gateway / BFF [HTTPS, WebSockets]
- Compliance Officers -> API Gateway / BFF [HTTPS]
- API Gateway / BFF -> Consultation & Prescriptions Service [gRPC over TLS (mTLS via SPIFFE/SPIRE)]
- API Gateway / BFF -> Consent & Policy Engine [gRPC over TLS (mTLS)]
- API Gateway / BFF -> AI Traceability & Logging Service [gRPC over TLS (mTLS)]
- Cross-Border Telehealth Platform -> Video Infrastructure Provider [HTTPS, WebSockets (WSS), SRTP/DTLS]
- Cross-Border Telehealth Platform -> AI Inference Engine [HTTPS (REST/gRPC)]
- Cross-Border Telehealth Platform -> Regional Pharmacy Gateways [HTTPS (HL7 FHIR / National APIs)]
- Cross-Border Telehealth Platform -> Identity & Consent Providers [OIDC/OAuth2 with FIDO2/WebAuthn]

## Technology Stack
- GCP (`europe-west3`, `us-central1`): Dedicated regional deployment to enforce data residency constraints.
- Node.js/GraphQL: API Gateway / BFF for efficient client-driven data fetching and schema federation.
- Go/gRPC: High-performance backend microservices and secure inter-container communication.
- Python/FastAPI: AI Traceability & Logging Service for machine learning integration and auditing.
- Go/OPA: Fine-grained ABAC enforcement for patient consent validation.
- Flutter/React: Cross-platform client applications optimized for multi-standard records and offline caching.

## Rationale
The architecture ensures strict regional data residency by deploying isolated API Gateway / BFF instances in GCP European and US regions. It maintains high availability and compliance for cross-border telemedicine through secure microservices, granular consent enforcement, and robust audit logging.