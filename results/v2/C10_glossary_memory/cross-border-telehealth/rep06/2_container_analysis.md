## Overview
[Cross-Border Telehealth Platform [system, context]] is a multi-region telehealth system providing video consultations, e-prescriptions, and an AI symptom checker for EU and US patients. It enforces strict regional data residency and regulatory compliance under GDPR, HIPAA, and EU MDR.

## Key Elements
* **Patients** [person, context]
* **Licensed Clinicians** [person, context]
* **Compliance Officers** [person, context]
* **Video Infrastructure Provider** [externalSystem, context]
* **AI Inference Engine** [externalSystem, context]
* **Regional Pharmacy Gateways** [externalSystem, context]
* **Identity & Consent Providers** [externalSystem, context]
* **API Gateway / BFF** (Node.js/GraphQL) [container]
* **Consultation & Prescriptions Service** (Go/gRPC) [container]
* **AI Traceability & Logging Service** (Python/FastAPI) [container]
* **Consent & Policy Engine** (Go/OPA) [container]
* **Patient Portal App** (Flutter/Web & Mobile) [container]
* **Clinician Workspace App** (React/TypeScript SPA) [container]

## Relationships
* **Patients** -> **API Gateway / BFF**: HTTPS, WebSockets
* **Licensed Clinicians** -> **API Gateway / BFF**: HTTPS, WebSockets
* **Compliance Officers** -> **API Gateway / BFF**: HTTPS
* **Consultation & Prescriptions Service** -> **Regional Pharmacy Gateways**: HTTPS (HL7 FHIR in US / National APIs in EU)
* **API Gateway** -> **Consultation & Prescriptions Service**: gRPC over TLS (mTLS via SPIFFE/SPIRE)
* **Cross-Border Telehealth Platform** -> **Video Infrastructure Provider**: HTTPS, WebSockets (WSS), SRTP/DTLS
* **Cross-Border Telehealth Platform** -> **AI Inference Engine**: HTTPS (REST/gRPC)
* **Cross-Border Telehealth Platform** -> **Identity & Consent Providers**: OIDC/OAuth2 with FIDO2/WebAuthn

## Technology Stack
* **GCP (`europe-west3`, `us-central1`)**: Cloud provider ensuring physical regional data separation.
* **Node.js / GraphQL**: API Gateway / BFF for efficient client-driven data fetching.
* **Go / gRPC**: High-performance backend microservices and inter-container communication.
* **Python / FastAPI**: AI Traceability & Logging Service for machine learning integration and auditing.
* **Open Policy Agent (OPA)**: Fine-grained ABAC enforcement for patient consent validation.
* **Cloud SQL PostgreSQL**: Regionally isolated relational data storage with CMEK encryption.
* **Flutter & React/TypeScript**: Client applications optimized for multi-standard records and offline caching.

## Rationale
Isolated container clusters per region (`europe-west3` and `us-central1`) strictly enforce data residency and HIPAA/GDPR constraints without compromising cross-border functionality. Open Policy Agent and dedicated traceability containers ensure EU MDR compliance and granular patient consent verification.