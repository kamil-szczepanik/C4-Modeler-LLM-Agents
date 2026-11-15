## Overview
[The Cross-Border Telehealth Platform provides video consultations, e-prescriptions, and an AI symptom checker for patients in the EU and US. It enforces strict regional data residency and compliance with GDPR and HIPAA.]

## Key Elements
- Patients (EU/US) & Licensed Clinicians
- Regional Deployments in europe-west3 and us-central1 (GCP)
- API Gateway (Go, Envoy)
- Consultation Service (Node.js/WebRTC) & SFU Media Relay (Mediasoup/C++)
- Clinical & Prescription Service (Java/Spring Boot)
- AI Symptom Checker (Python/FastAPI)
- Consent & Policy Engine (Go)
- Regional Message Broker (GCP Pub/Sub)
- Cloud SQL (PostgreSQL)

## Relationships
- Patients/Clinicians to API Gateway via HTTPS (TLS 1.3) and OAuth2/OIDC
- API Gateway to internal services via gRPC over mTLS
- Consultation Service to SFU Media Relay via WebRTC/UDP (DTLS-SRTP)
- Clinical Service to HL7 FHIR (US) and EU e-Prescription Gateways via REST/gRPC
- Services to GCP Pub/Sub via gRPC over mTLS

## Technology Stack
- Google Kubernetes Engine (GKE) Autopilot: Declarative, repeatable regional deployments via ArgoCD
- Envoy & Istio: Zero-trust mTLS service mesh and API gateway routing
- Mediasoup (C++): WebRTC SFU media relay for low-bandwidth video resilience (<300 kbit/s)
- GCP Pub/Sub: Regionally isolated message brokering ensuring strict data residency
- Cloud SQL (PostgreSQL): Isolated regional data storage with KMS encryption

## Rationale
[This regional multi-region container architecture guarantees that EU and US health data never cross borders without explicit consent, fulfilling GDPR and HIPAA mandates. Using GKE Autopilot, SFU media relays, and GCP Pub/Sub ensures resilient, low-latency telemedicine delivery even over unstable rural internet connections.]