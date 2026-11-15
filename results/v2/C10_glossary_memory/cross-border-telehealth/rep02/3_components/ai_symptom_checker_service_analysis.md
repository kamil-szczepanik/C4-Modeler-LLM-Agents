## Overview
[The Cross-Border Telehealth Platform provides video consultations, e-prescriptions, and an AI symptom checker for EU and US patients. It enforces strict regional data residency, HIPAA, and EU MDR compliance using Google Cloud Platform.]

## Key Elements
- Patients (EU & US)
- Licensed Clinicians
- Pharmacists (EU/US)
- Compliance & Regulatory Auditors
- National e-Prescription Gateways (EU)
- Pharmacy Systems (US)
- Third-Party Video Infrastructure (WebRTC CPaaS)
- Regional Identity Providers (eIDAS/OIDC/OAuth 2.0)
- Regional API Gateways (GCP Cloud Endpoints/API Gateway)
- Frontend UI (Flutter Web/Mobile)
- Video Streaming Service (WebRTC, UDP/TCP/TLS, TURN)
- AI Symptom Checker Service (AI / GCP, Cloud HSM)
- Consent & Data Management Service (CMEK, GCP)
- Immutable Logging Service (GCP Cloud Storage, Cloud Logging, Pub/Sub)

## Relationships
- Patients (EU & US) -> Frontend UI (HTTPS (TLS 1.3), secure WebSockets, OIDC/OAuth 2.0)
- Licensed Clinicians -> Frontend UI (HTTPS (TLS 1.3), secure WebSockets, OIDC/OAuth 2.0)
- Pharmacists (EU/US) -> Frontend UI (HTTPS (TLS 1.3), secure WebSockets, OIDC/OAuth 2.0)
- Compliance & Regulatory Auditors -> Frontend UI (HTTPS (TLS 1.3))
- Frontend UI -> Regional API Gateways (HTTPS (REST/GraphQL), TLS 1.3)
- Regional API Gateways -> Consent & Data Management Service (gRPC over mTLS)
- AI Symptom Checker Service -> Immutable Logging Service (GCP Pub/Sub, regional CMEK)
- Regional API Gateways -> Third-Party Video Infrastructure (WebRTC via UDP/TCP/TLS and TURN)
- Regional API Gateways -> National e-Prescription Gateways (EU) (HTTPS/REST)
- Regional API Gateways -> Pharmacy Systems (US) (HTTPS/REST via HL7 FHIR)

## Technology Stack
- GCP (europe-west3, us-central1): Target cloud provider and regions for strict data residency.
- Flutter Web/Mobile: Frontend technology supporting localized, offline-first user interfaces.
- WebRTC CPaaS: External video infrastructure ensuring low-bandwidth adaptability.
- PyTorch & GCP Vertex AI: Powers regional AI symptom triage models with auto-scaling.
- Google Cloud HSM: Cryptographic hardware security for signing AI outputs (EU MDR traceability).
- GCP Pub/Sub & CMEK: Asynchronous messaging and regional encryption for immutable logs.

## Rationale
[The chosen architecture isolates regional data within GCP to satisfy strict GDPR and HIPAA residency mandates. Furthermore, asynchronous pipelines and cryptographic signing ensure low-bandwidth resilience and full EU MDR traceability.]