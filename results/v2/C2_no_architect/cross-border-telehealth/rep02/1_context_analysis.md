## Overview
The Cross-Border Telehealth Platform provides video consultations, e-prescriptions, and an AI symptom checker for patients across the EU and US. It guarantees strict regulatory compliance and data residency while supporting low-bandwidth connections.

## Key Elements
- **Users**: Patients (rural and urban), Licensed Clinicians, Platform Administrators, Regional Health Authorities/Auditors
- **External Systems**: Local Pharmacy Networks (EU national standards and US HL7 FHIR endpoints)
- **Core Containers**: Regional API Gateways, Video Consultation Service, AI Symptom Checker Service, Consent Management Engine, Immutable Audit Logging Pipeline
- **Infrastructure**: GCP regions `europe-west3` (EU) and `us-central1` (US), Cloud CDN/Media CDN, regional CMEK keys

## Relationships
- Patients & Clinicians to Regional API Gateways via HTTPS/TLS 1.3 and mTLS
- Video Service to Clients via WebRTC (adaptive bitrate streaming for <300 kbit/s connections)
- API Gateways to Local Pharmacy Networks via REST/HL7 FHIR (US) and national e-prescription APIs (EU)
- Services to Consent Engine via scoped OAuth 2.0 / OpenID Connect tokens
- Audit System to Regional Health Authorities via dedicated read-only API gateways

## Technology Stack
- **Cloud Provider**: GCP (`europe-west3`, `us-central1`) for localized infrastructure and strict data residency isolation
- **Video & Edge**: WebRTC with Cloud CDN/Media CDN for low-bandwidth adaptive bitrate streaming
- **Security & Auth**: OAuth 2.0, OpenID Connect, FIDO2/WebAuthn hardware tokens for administrators, regional Customer-Managed Encryption Keys (CMEK)
- **Interoperability**: HL7 FHIR (US) and national e-prescription standards (EU)
- **Observability**: OpenTelemetry distributed tracing and GCP Cloud Logging for immutable audit trails

## Rationale
Asymmetric regional deployment on GCP with isolated data planes enforces strict GDPR and HIPAA data residency constraints (R-05). Edge optimization, decentralized consent, and immutable logging fulfill stringent availability, compliance, and traceability mandates (R-06, R-07).