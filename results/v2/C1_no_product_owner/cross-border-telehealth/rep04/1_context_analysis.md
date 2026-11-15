## Overview
The Cross-Border Telehealth Platform provides video consultations, e-prescriptions, and an AI symptom checker for patients in the EU and US. It enforces strict regional data residency while supporting secure cross-border management and interoperability.

## Key Elements
- **Users**: Patients and Licensed Clinicians using Mobile/Web Apps (HTTPS/WebRTC).
- **Regional Systems**: EU Telehealth System (`europe-west3`) and US Telehealth System (`us-central1`).
- **Global Management Plane**: Oversees metadata synchronization, AI versioning, and governance.
- **External Integrations**: National E-Prescription Gateways (EU) and HL7 FHIR Interoperability Services (US).
- **Identity Providers**: Regional IAM services utilizing OAuth2/OIDC.
- **Pharmacies**: Local EU/US pharmacies receiving prescriptions via HTTPS/REST.

## Relationships
- **Users to Regional Systems**: Patients and clinicians connect via HTTPS for APIs and WebRTC/DTLS-SRTP for video consultations.
- **Regional Systems to Pharmacies**: EU systems transmit e-prescriptions via national gateways; US systems use HL7 FHIR over HTTPS/REST.
- **Regional Systems to IAM**: Local applications validate tokens via regional OIDC/OAuth2 services.
- **Global Management Plane to Regional Systems**: Communicates via mTLS and scoped OAuth2 APIs for configuration and AI audit logging.

## Technology Stack
- **Cloud Provider**: Google Cloud Platform (GCP) deployed in `europe-west3` and `us-central1` for region-locked data isolation.
- **Protocols**: TLS 1.3 and mTLS for data in transit; AES-256 for data at rest; WebRTC with adaptive media gateways for low-bandwidth video.
- **Interoperability**: HL7 FHIR for US healthcare data exchange and national standards for EU e-prescriptions.
- **Security & Logging**: OAuth2/OIDC with step-up MFA, region-locked Cloud Monitoring/Logging, and an immutable AI audit ledger.

## Rationale
This dual-region architecture guarantees absolute compliance with GDPR and HIPAA by isolating patient health data within its origin region. Autonomous regional design ensures high availability and continuous degraded-mode video consultations even during global management outages or rural network instability.