## Overview
The Cross-Border Telehealth Platform provides secure video consultations, e-prescriptions, and an AI symptom checker for patients across the EU and US. It strictly enforces regional data residency, regulatory compliance, and high availability over GCP.

## Key Elements
- Patients
- Licensed Clinicians
- Compliance Officers / Auditors
- EU National E-Prescription Gateways
- US Pharmacy Networks (Surescripts)
- Identity Providers (eIDAS / OAuth2/OIDC)
- Regional Payment & Insurance Gateways
- Web Application Container (React / Next.js)
- API Gateway Container (Envoy / GCP API Gateway)
- Core Services Container (Go / Node.js microservices)
- AI Symptom Checker Container (Python / FastAPI + Vertex AI)
- Media Relay Container (Janus / WebRTC SFU)
- E-Prescription Integration Container (Java / Spring Boot)
- Databases (GCP Cloud SQL for PostgreSQL)

## Relationships
- Patients -> Web Application Container [HTTPS]
- Licensed Clinicians -> Web Application Container [HTTPS]
- Web Application Container -> API Gateway Container [HTTPS / REST & GraphQL]
- Patients -> Media Relay Container [WebRTC / DTLS-SRTP, UDP]
- Licensed Clinicians -> Media Relay Container [WebRTC / DTLS-SRTP, UDP]
- API Gateway Container -> Core Services Container [gRPC over mTLS]
- API Gateway Container -> AI Symptom Checker Container [gRPC over mTLS]
- Core Services Container -> E-Prescription Integration Container [gRPC over mTLS]
- Core Services Container -> Databases [TCP / SSL]
- E-Prescription Integration Container -> EU National E-Prescription Gateways [HTTPS / mTLS / HL7 FHIR]
- E-Prescription Integration Container -> US Pharmacy Networks (Surescripts) [HTTPS / mTLS / HL7 FHIR]

## Technology Stack
- GCP Cloud SQL for PostgreSQL: Relational persistence featuring multi-region deployment (`europe-west3` and `us-central1`) for regional data residency.
- GCP Cloud KMS: Customer-Managed Encryption Keys (CMEK) with annual rotation for robust encryption.
- React / Next.js: Frontend web application framework for patients and clinicians.
- Go / Node.js & Java / Spring Boot: Core microservices and integration runtimes.
- Python / FastAPI + Vertex AI: Scalable AI symptom checking and model processing.
- Janus WebRTC SFU: Media relay handling real-time video consultations.
- Envoy / GCP API Gateway: Secure routing and API management layer.

## Rationale
This architecture guarantees strict regional isolation of EU and US health data to comply with GDPR and HIPAA mandates. It utilizes resilient GCP services and WebRTC streaming to maintain high availability and performance even for rural patients with unstable connections.