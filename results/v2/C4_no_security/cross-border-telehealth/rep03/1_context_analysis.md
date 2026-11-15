## Overview
A cross-border telehealth platform providing video consultations, e-prescriptions, and an AI symptom checker for patients in the EU and the US. The system guarantees regional data residency, regulatory compliance, and resilience for unstable internet connections.

## Key Elements
- Patients (EU & US) and Licensed Clinicians
- Pharmacies and National Pharmacy Networks (EU) / US Pharmacy Systems
- EU Telehealth Platform (GCP `europe-west3`) and US Telehealth Platform (GCP `us-central1`)
- AI Symptom Checker Engine with immutable audit logging sidecars
- Regional Identity Providers (EU eIDAS-compliant / US OAuth via OIDC)
- Regional Health Authorities and Auditors
- Managed Cloud KMS with Customer-Managed Encryption Keys (CMEK)

## Relationships
- Patients and Clinicians interact with regional telehealth platforms via HTTPS/REST and WebRTC for video.
- Regional platforms connect to National Pharmacy Networks and US Pharmacy Systems using national standards and HL7 FHIR over HTTPS/REST.
- Regional platforms call the AI Symptom Checker Engine via gRPC with strict local caching.
- Third-Party Identity Providers integrate via OpenID Connect (OIDC) over HTTPS.
- Health Authorities access regional audit endpoints via mTLS and signed JWTs over HTTPS.

## Technology Stack
- Google Cloud Platform (GCP): Deployed in `europe-west3` and `us-central1` for geographic isolation.
- WebRTC: Powers video consultations with adaptive bitrate streaming for connections below 300 kbit/s.
- HL7 FHIR & REST/HTTPS: Ensures US interoperability and secure API communications.
- gRPC: Facilitates low-latency internal communication with the AI Symptom Checker.
- OpenID Connect (OIDC): Manages regional identity federation.
- Cloud KMS (CMEK): Provides cryptographic data isolation per region.

## Rationale
The architecture strictly enforces data residency boundaries to comply with GDPR and HIPAA mandates. Regional isolation combined with localized AI processing and cryptographic controls ensures regulatory compliance while maintaining high availability for low-bandwidth users.