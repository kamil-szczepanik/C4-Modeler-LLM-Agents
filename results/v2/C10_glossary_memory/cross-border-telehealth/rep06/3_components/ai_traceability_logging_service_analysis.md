## Overview
The Cross-Border Telehealth Platform provides secure video consultations, e-prescriptions, and an AI symptom checker for patients in the EU and US. It enforces strict regional data residency, GDPR, HIPAA, and EU MDR compliance using GCP regions `europe-west3` and `us-central1`.

## Key Elements
- Patients
- Licensed Clinicians
- Compliance Officers
- Patient Portal App (Flutter/Web & Mobile)
- Clinician Workspace App (React/TypeScript SPA)
- API Gateway / BFF (Node.js/GraphQL)
- Consultation & Prescriptions Service (Go/gRPC)
- AI Traceability & Logging Service (Python/FastAPI)
- Consent & Policy Engine (Go/OPA)
- Video Infrastructure Provider (WebRTC SFU)
- AI Inference Engine (External LLM service)
- Regional Pharmacy Gateways (HL7 FHIR / National APIs)
- Identity & Consent Providers (OIDC/OAuth2)

## Relationships
- Patients -> API Gateway / BFF (HTTPS, WebSockets)
- Licensed Clinicians -> API Gateway / BFF (HTTPS, WebSockets)
- Compliance Officers -> API Gateway / BFF (HTTPS)
- API Gateway / BFF -> Consultation & Prescriptions Service (gRPC over TLS via SPIFFE/SPIRE)
- Cross-Border Telehealth Platform -> Video Infrastructure Provider (HTTPS, WebSockets (WSS), SRTP/DTLS)
- Cross-Border Telehealth Platform -> AI Inference Engine (HTTPS (REST/gRPC))
- Consultation & Prescriptions Service -> Regional Pharmacy Gateways (HTTPS (HL7 FHIR / National APIs))
- Cross-Border Telehealth Platform -> Identity & Consent Providers (OIDC/OAuth2 with FIDO2/WebAuthn)

## Technology Stack
- Google Cloud Platform: Target cloud provider with strict regional isolation in `europe-west3` and `us-central1`.
- Node.js/GraphQL: API Gateway / BFF for efficient client-driven data fetching.
- Go: High-performance microservices and inter-container communication (gRPC) and ABAC enforcement (OPA).
- Python/FastAPI: AI Traceability & Logging Service for machine learning integration, audit trails, and export formatting.
- Flutter & React: Cross-platform mobile/web client apps optimized for unstable networks and caching.
- GCP Cloud KMS & Cloud Storage: CMEK encryption and WORM storage for regional data residency and immutability.

## Rationale
The architecture guarantees strict regional data isolation to satisfy GDPR and HIPAA requirements while maintaining sub-second audit logging and compliance export capabilities for EU MDR. Regional multi-cluster deployments and asynchronous background processing ensure high availability and reliability for users on unstable rural internet connections.