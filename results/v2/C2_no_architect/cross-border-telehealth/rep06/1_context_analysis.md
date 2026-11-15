## Overview
A cross-border telehealth platform providing video consultations, e-prescriptions, and an AI symptom checker for patients in the EU and US. It ensures regional compliance, strict data residency, and high availability over unstable networks.

## Key Elements
- Patients, Licensed Clinicians, Platform Administrators, Compliance Auditors
- Cross-Border Telehealth Platform (GCP Containerized Services)
- EU Container (`europe-west3`) and US Container (`us-central1`)
- AI Symptom Checker Container (with model versioning)
- External Pharmacies, National Health Authorities, and E-Prescription Networks

## Relationships
- Patients to Telehealth Platform via Web/Mobile apps (HTTPS, TLS 1.3)
- Clinicians to Telehealth Platform via Web UI (mTLS, OAuth2/OIDC, MFA)
- Telehealth Platform to External Pharmacies via regional message queues (GCP Pub/Sub, mTLS, payload signatures)
- Telehealth Platform to National Health Authorities via REST APIs (Circuit Breaker, mTLS, HL7 FHIR / EU national standards)
- Platform Auditors to WORM Audit Logs via read-only encrypted tunnels (Explicit Consent verification)

## Technology Stack
- Cloud Provider: Google Cloud Platform (GCP) across `europe-west3` and `us-central1` for strict regional data residency
- Messaging: GCP Pub/Sub for asynchronous e-prescription delivery and decoupled service resilience
- Security: TLS 1.3, CMEK encryption at rest, WORM storage for immutable audit logs, and OAuth2/OIDC with ABAC
- Observability: Region-locked GCP Cloud Logging and Prometheus instances
- Interoperability: HL7 FHIR (US) and national e-prescription standards (EU)

## Rationale
The multi-region GCP deployment isolates EU and US health data to strictly satisfy GDPR, HIPAA, and regional data residency constraints. Decoupled asynchronous messaging and strict regional boundaries ensure continuous availability and resilience despite unstable local networks.