## Overview
The Cross-Border Telehealth Platform provides video consultations, e-prescriptions, and an AI symptom checker for patients in the EU and US. It runs on GCP (europe-west3 and us-central1) ensuring strict data residency, regulatory compliance (GDPR/HIPAA/MDR), and graceful degradation in low-bandwidth environments.

## Key Elements
- Patients and Licensed Clinicians
- Client Apps (Flutter / Web application)
- API Gateway (Google Cloud API Gateway / Envoy)
- Core Telehealth Service (Consultation Manager, Prescription Coordinator, Consent Verifier, Telemetry & Adaptation Engine)
- Supporting Containers (AI Symptom Checker, Patient Consent Service, Pharmacy Integration Gateway, Video Media Server)
- Data Storage (Google Cloud SQL PostgreSQL with FHIR extensions)

## Relationships
- Client Apps -> API Gateway: HTTPS / WebRTC
- API Gateway -> Core Telehealth Service: gRPC with mTLS
- Core Telehealth Service -> Patient Consent Service: gRPC with mTLS
- Core Telehealth Service -> Pharmacy Integration Gateway: gRPC over mTLS
- Core Telehealth Service -> Video Media Server (LiveKit): Internal event hooks / WebRTC SFU
- Core Telehealth Service -> Data Storage: Encrypted SQL via pgx driver

## Technology Stack
- Go: Chosen for Core Telehealth Service components to ensure high throughput and low memory footprint.
- GCP (europe-west3 / us-central1): Provides regional isolation enforcing GDPR and HIPAA data residency constraints.
- gRPC with mTLS: Secures internal service-to-service communication with transport-layer encryption.
- Google Cloud SQL (PostgreSQL): Manages structured health data with FHIR extensions for US interoperability.
- LiveKit: Acts as the WebRTC SFU for video consultations supporting bandwidth adaptation.

## Rationale
This architecture enforces strict regional data boundaries and consent verification to satisfy GDPR and HIPAA mandates. Furthermore, internal component decomposition and in-memory consent caching guarantee low-latency reliability for patients with unstable internet connections.