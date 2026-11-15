## Overview
[The Cross-Border Telehealth Platform provides video consultations, e-prescriptions, and an AI symptom checker for patients in the EU and US while strictly enforcing regional data residency and healthcare regulations.]

## Key Elements
- Patients (EU and US)
- Licensed Clinicians
- Local Pharmacies
- API Gateway with Consent Enforcement Proxy
- AI Symptom Checker Service with Vertex AI
- Selective Forwarding Unit (SFU) Media Router
- Regional Application Containers (GCP europe-west3 and us-central1)
- GCP Cloud KMS (CMEK) and Cloud HSM

## Relationships
- Patients & Clinicians to API Gateway via TLS 1.3 / mTLS
- API Gateway to Consent Enforcement Proxy via internal gRPC
- Video Consultations via WebRTC through SFU Media Router
- AI Symptom Checker to Vertex AI via LLM Security Gateway
- E-Prescriptions to Local Pharmacies using national e-prescription standards (EU) and HL7 FHIR (US) via secure REST APIs

## Technology Stack
- Google Cloud Platform (GCP) for multi-region hosting (europe-west3, us-central1)
- GCP VPC Service Controls and Organization Policies for data isolation
- OAuth 2.0 / OpenID Connect with adaptive MFA for authentication
- Vertex AI and OpenTelemetry for AI inference and model traceability (R-07)
- GCP Cloud KMS (CMEK) and Cloud HSM for cryptographic key management and digital signatures

## Rationale
[This multi-region, security-first architecture ensures strict GDPR and HIPAA compliance by isolating health data regionally and using cryptographic enforcement for cross-border consent. Additionally, dynamic SFU media routing and immutable audit logging guarantee high availability in rural areas and full traceability for EU MDR compliance.]