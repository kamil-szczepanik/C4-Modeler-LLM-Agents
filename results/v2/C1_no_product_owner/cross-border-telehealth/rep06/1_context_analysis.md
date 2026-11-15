## Overview
A cross-border telehealth platform providing video consultations, e-prescriptions, and an AI symptom checker for EU and US patients. It enforces strict regional data residency, GDPR/HIPAA compliance, and medical device traceability.

## Key Elements
- **Patients (EU/US):** Mobile and web clients using Flutter/React over HTTPS and WebRTC.
- **Clinicians:** Medical professionals conducting consultations and issuing e-prescriptions.
- **Cross-Border Telehealth Platform:** Core system encompassing video engine, consent manager, and self-hosted AI symptom checker.
- **Infrastructure:** GCP regions `europe-west3` (EU) and `us-central1` (US) utilizing GKE with GPU node pools.
- **External Systems:** EU National E-Prescription Gateways, US Pharmacy Systems, National Health Registries, and external Identity Providers (Login.gov, eIDAS).

## Relationships
- **Patient/Clinician to Platform:** HTTPS (TLS 1.3) and WebRTC for secure UI and video consultations.
- **Platform to External Gateways/Pharmacies:** HTTPS/REST and HL7 FHIR with mTLS and certificate pinning for e-prescriptions and registries.
- **Platform to Identity Providers:** OAuth 2.0 / OIDC federation for secure authentication.
- **Intra-Platform Communication:** mTLS for all inter-service traffic.

## Technology Stack
- **Cloud Provider:** GCP (`europe-west3` and `us-central1`) for regional data isolation and compliance.
- **Infrastructure as Code:** Terraform with parameterized modules to prevent configuration drift.
- **Video & Network:** TURN/STUN servers deployed at network edges for <300 kbit/s degraded-mode connectivity.
- **AI & Compute:** Self-hosted containerized AI models on GKE GPU-accelerated node pools for EU MDR traceability and data residency.
- **Security & Storage:** Cloud KMS with regional CMEK for encryption at rest; GCP Cloud Logging with regional sinks for tamper-proof audit logs.

## Rationale
This architecture uses regional GCP isolation and self-hosted AI inference to strictly satisfy GDPR, HIPAA, and EU MDR constraints without data leakage. Edge TURN/STUN servers and containerized degradation handling ensure continuous availability for rural patients with unstable connections.