## Overview
A unified cross-border telehealth SaaS platform providing video consultations, e-prescriptions, and an AI symptom checker for patients in the EU and US. It enforces strict regional data residency and compliance using isolated cloud deployments.

## Key Elements
- **Patients & Licensed Clinicians:** Primary human users interacting via Web and Mobile Apps (HTTPS/WebRTC).
- **Pharmacies & Regional Health Authorities/Payers:** External systems handling prescriptions, claims, and reimbursement.
- **AI Triage Model Provider:** GCP Vertex AI managing symptom-checking inference.
- **Identity & Consent Providers:** Region-specific IAM systems supporting OIDC/SAML.
- **Cross-Border Telehealth Platform:** Core system deployed regionally in GCP (`europe-west3` and `us-central1`).

## Relationships
- Patients and Clinicians connect via WebRTC (video) and HTTPS (APIs).
- Core Platform integrates with Pharmacies and Payers using REST and HL7 FHIR protocols.
- Regional platforms communicate with GCP Vertex AI via version-pinned inference APIs.
- Systems enforce mTLS for inter-service and cross-region communication.

## Technology Stack
- **Cloud Provider (GCP):** Deployed in `europe-west3` and `us-central1` for geographical data isolation.
- **Data Privacy & Security:** GCP Cloud KMS (CMEK) and VPC Service Controls for GDPR/HIPAA compliance.
- **Resilience & Streaming:** GCP Media CDN with WebRTC SFU edge relays for low-bandwidth connections (<300 kbit/s).
- **Integration & Messaging:** GCP Pub/Sub for asynchronous regional payer integrations.
- **Audit & Observability:** GCP Cloud Logging with bucket-lock and OpenTelemetry for EU MDR traceability and tracing.

## Rationale
Dual-region GCP deployment guarantees strict regional data residency while supporting cross-border access via explicit patient consent tokens. Asynchronous messaging and edge media relays ensure high availability and performance even in unstable rural network conditions.