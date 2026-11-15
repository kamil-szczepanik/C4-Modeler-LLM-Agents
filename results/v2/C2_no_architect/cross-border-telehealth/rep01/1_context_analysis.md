## Overview
A cross-border telehealth platform providing video consultations, e-prescriptions, and an AI symptom checker for patients in the EU and US. It ensures strict data residency, regulatory compliance, and low-bandwidth availability.

## Key Elements
- **Patients (EU & US):** End-users managing consent, video calls, and AI triage.
- **Licensed Clinicians:** Medical professionals conducting consultations and issuing e-prescriptions.
- **Pharmacies (EU & US):** External systems receiving e-prescription fulfillments.
- **Compliance & QA Officers:** Regulators monitoring EU MDR and HIPAA compliance.
- **GCP Cloud Infrastructure:** Dual-region deployment in `europe-west3` (EU) and `us-central1` (US).
- **Core Containers:** WebRTC video gateway, AI symptom-checker service, regional API gateways, and audit logging pipelines.

## Relationships
- **Patients/Clinicians to Video Gateway:** WebRTC (TLS 1.3) for real-time video consultations.
- **Clients to API Gateways:** HTTPS/REST and OAuth 2.0 / OIDC for consent management and symptom checking.
- **AI Symptom Checker to Cloud KMS:** Internal gRPC for cryptographic signing of recommendations.
- **API Gateways to Regional Pharmacies:** mTLS and OAuth 2.0 token exchange for e-prescriptions (HL7 FHIR in US, national standards in EU).

## Technology Stack
- **Cloud Provider:** Google Cloud Platform (GCP) across `europe-west3` and `us-central1` for localized data residency.
- **Security & Encryption:** Cloud KMS with region-specific Customer-Managed Encryption Keys (CMEK) and GCP Confidential VMs for in-memory encryption.
- **Video & Network:** GCP Media CDN and adaptive bitrate WebRTC gateways for rural connectivity.
- **Data & Compliance:** Cloud Logging and BigQuery for region-isolated, immutable audit trails.
- **Interoperability:** HL7 FHIR for US systems and national standards for EU pharmacies.

## Rationale
This architecture guarantees regional data isolation to comply with GDPR and HIPAA mandates. It leverages edge optimization and confidential computing to ensure high availability for low-bandwidth users and strict traceability for AI medical outputs.