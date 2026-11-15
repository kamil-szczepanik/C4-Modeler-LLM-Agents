## Overview
The Cross-Border Telehealth Platform provides video consultations, e-prescriptions, and an AI symptom checker for patients in the EU and the US. It ensures strict regional data residency, regulatory compliance, and low-bandwidth availability.

## Key Elements
- Patients and Clinicians (Primary Users)
- Regulatory & Compliance Auditors (External Users)
- Cross-Border Telehealth Platform (Central Software System spanning GCP regions)
- Regional API Gateways and Application Services (GCP Cloud Run / GKE containers)
- Regional Datastores and Audit Logging Services (GCP Cloud SQL and Cloud Logging)
- Native AI Inference Service (GCP Vertex AI)
- Video/Media Gateways (WebRTC SFU / LiveKit)
- External Pharmacy Networks, National Identity Providers, and Payment Gateways

## Relationships
- Patients/Clinicians -> Regional API Gateways via HTTPS and WebRTC
- Telehealth Platform -> External Pharmacy Networks via REST and HL7 FHIR APIs
- Telehealth Platform -> National Identity Providers via OIDC/SAML
- Telehealth Platform -> Payment & Insurance Providers via HTTPS
- Inter-container communication via gRPC and internal REST within GCP regions

## Technology Stack
- **Cloud Provider:** Google Cloud Platform (GCP) across `europe-west3` (Frankfurt) and `us-central1` (Iowa) for data residency
- **Compute:** GCP Cloud Run and GKE for scalable regional microservices
- **Database & Storage:** GCP Cloud SQL for isolated regional patient datastores
- **AI & Analytics:** GCP Vertex AI for regionally hosted, traceable medical AI inference
- **Media Streaming:** WebRTC with STUN/TURN fallback for rural, low-bandwidth connections (<300 kbit/s)
- **Interoperability:** HL7 FHIR (US) and national e-prescription standards (EU)

## Rationale
Partitioning infrastructure across isolated GCP regions guarantees compliance with GDPR, HIPAA, and EU MDR data residency mandates. Native AI and adaptive WebRTC streaming satisfy stringent traceability and low-bandwidth availability requirements.