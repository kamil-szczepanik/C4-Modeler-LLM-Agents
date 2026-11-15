## Overview
The Cross-Border Telehealth Platform provides secure video consultations, e-prescriptions, and an AI symptom checker for patients across the EU and US. It enforces strict regional data residency while ensuring regulatory compliance, auditability, and resilience for low-bandwidth connections.

## Key Elements
- Patients (EU/US) and Licensed Clinicians
- Cross-Border Telehealth Platform (GCP-hosted)
- National E-Prescription Gateways (EU) and US Pharmacy Networks
- AI Symptom Checker Engine
- Compliance / Regulatory Authorities and Medical Licensing Board Services

## Relationships
- Patient/Clinician to Platform via HTTPS/WebRTC (optimized for <300 kbit/s connections)
- Platform to External Pharmacies/Gateways via mTLS with REST/FHIR payloads
- Platform to Medical Licensing Board Services via REST/HTTPS with local caching
- Platform to Compliance Authorities via OAuth2/mTLS for secure audit export

## Technology Stack
- Google Cloud Platform (GCP) deployed in `europe-west3` (EU) and `us-central1` (US) for regional data residency
- WebRTC Selective Forwarding Units (SFUs) deployed locally in each region for adaptive video streaming
- Cloud KMS with regional customer-managed encryption keys (CMEK) and TLS 1.3 for data protection
- Cloud Audit Logs with Object Lock for append-only, tamper-proof AI traceability
- OAuth2 and Web Application Firewall (WAF) for secure API gateway enforcement

## Rationale
This architecture guarantees strict HIPAA and GDPR compliance by physically separating EU and US health data into dedicated GCP regions while enabling cross-border access through explicit, token-based consent. Additionally, it ensures medical device traceability and high availability for rural patients via local SFUs and immutable audit logging.