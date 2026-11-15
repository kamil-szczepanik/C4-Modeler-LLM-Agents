## Overview
The Cross-Border Telehealth Platform provides secure video consultations, e-prescriptions, and an AI symptom checker for patients across the EU and US. It enforces strict regional data residency and compliance using isolated cloud deployments.

## Key Elements
- Patients & Licensed Clinicians
- Compliance Officers / Auditors
- Regional Ingress (Cloud Load Balancing & Envoy)
- Web/Mobile Frontend (Flutter)
- Telehealth Service (Go / WebRTC)
- Prescription & Record Service (Java / Spring Boot)
- AI Orchestrator & Audit Service (Python / FastAPI)
- Consent & Identity Service (Keycloak / PostgreSQL)

## Relationships
- Patients & Clinicians to Regional Ingress via HTTPS / WSS
- Frontend to Telehealth Service via WebRTC / UDP (adaptive bitrate streaming)
- Internal Containers to Internal Containers via gRPC with mTLS
- Prescription Service to National E-Prescription Gateways (EU) and US Pharmacy Networks via HL7 FHIR / national standards
- AI Orchestrator to Regional Cloud Storage via WORM file protocols

## Technology Stack
- Google Cloud Platform (GCP): Deployed in `europe-west3` and `us-central1` for strict regional data residency
- Flutter: Enables offline-first client state for low-bandwidth rural connections (<300 kbit/s)
- Go / WebRTC: Manages low-latency media streams with global regional TURN relays
- Java / Spring Boot: Abstracts fragmented EU and US e-prescription standards
- Python / FastAPI: Orchestrates AI symptom checker with immutable audit logging
- Keycloak / PostgreSQL: Manages identity, OAuth2/OIDC, and per-purpose GDPR/HIPAA consent

## Rationale
This architecture guarantees strict regional data isolation between the EU and US to comply with GDPR and HIPAA mandates. Regional container redundancy ensures high availability, auditability, and low-bandwidth resilience for rural users.