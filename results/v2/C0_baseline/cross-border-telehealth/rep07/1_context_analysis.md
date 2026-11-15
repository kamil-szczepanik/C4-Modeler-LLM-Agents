## Overview
The Cross-Border Telehealth Platform provides video consultations, e-prescriptions, and an AI symptom checker for patients in the EU and the US. It enforces strict regional data residency while ensuring high availability for rural users and compliance with GDPR, HIPAA, and EU MDR.

## Key Elements
- Patients (EU / US)
- Licensed Clinicians
- Local Pharmacies (EU / US)
- Platform Administrator / Compliance Officer
- Cross-Border Telehealth Platform (GCP hosted)
- AI Symptom Checker Engine
- Notification Gateway
- EU Pharmacy Networks & US Pharmacy Networks (HL7 FHIR / NCPDP)
- Identity Providers (EU eIDAS / US OAuth Providers)

## Relationships
- Patients & Clinicians $\rightarrow$ Cross-Border Telehealth Platform: HTTPS / WebRTC for video consultations, AI checks, and consent management
- Cross-Border Telehealth Platform $\rightarrow$ Pharmacies: Secure REST / HL7 FHIR over mTLS for e-prescription dispatch
- Cross-Border Telehealth Platform $\rightarrow$ AI Symptom Checker Engine: HTTPS / gRPC for real-time urgency assessment
- Cross-Border Telehealth Platform $\rightarrow$ Notification Gateway: Asynchronous Pub/Sub for low-bandwidth patient alerts

## Technology Stack
- Cloud Provider: Google Cloud Platform (GCP) across `europe-west3` and `us-central1` regions for regional data residency
- Security: Cloud KMS with CMEK for encryption at rest; TLS 1.3 and mTLS for data in transit; VPC Service Controls for isolation
- Networking & Availability: Cloud CDN and Cloud Armor for edge-routing and degraded mode support below 300 kbit/s
- Interoperability & Integration: HL7 FHIR (US), national e-prescription standards (EU), and asynchronous Pub/Sub messaging

## Rationale
This architecture uses multi-region GCP isolation and VPC Service Controls to strictly enforce EU and US data residency mandates. Edge-routing and asynchronous messaging guarantee availability for rural users on unstable connections while meeting rigorous compliance, encryption, and traceability standards.