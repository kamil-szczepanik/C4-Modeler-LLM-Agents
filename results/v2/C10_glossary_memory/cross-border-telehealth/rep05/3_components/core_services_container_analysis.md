## Overview
[The system is a Cross-Border Telehealth Platform providing video consultations, e-prescriptions, and an AI symptom checker for patients across the EU and US. Its core purpose is delivering compliant, region-restricted telemedicine workflows with strict data residency and privacy controls.]

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
- Patients -> Cross-Border Telehealth Platform (HTTPS/WebRTC (DTLS-SRTP, adaptive bitrate))
- Licensed Clinicians -> Cross-Border Telehealth Platform (HTTPS/WebRTC (DTLS-SRTP, adaptive bitrate))
- Auditors -> Cross-Border Telehealth Platform (HTTPS (IAM roles))
- Cross-Border Telehealth Platform -> EU National E-Prescription Gateways (secure APIs via mTLS and HL7 FHIR / REST)
- Cross-Border Telehealth Platform -> US Pharmacy Networks (Surescripts) (secure APIs via mTLS and HL7 FHIR / REST)
- Cross-Border Telehealth Platform -> Identity Providers (eIDAS / OAuth2/OIDC) (OIDC/OAuth2)
- Cross-Border Telehealth Platform -> Regional Payment & Insurance Gateways (HTTPS/REST with tokenization via GCP VPC Service Controls)
- Patients -> Web Application Container (HTTPS)
- Licensed Clinicians -> Web Application Container (HTTPS)
- Web Application Container -> API Gateway Container (HTTPS / REST & GraphQL)
- Patients -> Media Relay Container (WebRTC / DTLS-SRTP, UDP)
- Licensed Clinicians -> Media Relay Container (WebRTC / DTLS-SRTP, UDP)
- API Gateway Container -> Core Services Container (gRPC over mTLS)
- API Gateway Container -> AI Symptom Checker Container (gRPC over mTLS)
- Core Services Container -> E-Prescription Integration Container (gRPC over mTLS)
- Core Services Container -> Databases (TCP / SSL)
- E-Prescription Integration Container -> EU National E-Prescription Gateways (HTTPS / mTLS / HL7 FHIR)
- E-Prescription Integration Container -> US Pharmacy Networks (Surescripts) (HTTPS / mTLS / HL7 FHIR)

## Technology Stack
- GCP (`europe-west3`, `us-central1`): Target cloud provider and regions ensuring regional data residency.
- React / Next.js: Frontend web application framework.
- Envoy / GCP API Gateway: API routing and management.
- Go / Node.js: Core services and microservices implementation.
- Python / FastAPI + Vertex AI: AI symptom checker backend and model serving.
- Janus / WebRTC SFU: Media relay for real-time video consultations.
- Java / Spring Boot: E-prescription integration services.
- GCP Cloud SQL for PostgreSQL: Relational database with CMEK encryption.

## Rationale
- This architecture enforces regional data separation between the EU and US to satisfy strict GDPR and HIPAA compliance mandates. GCP regional sharding and VPC Service Controls guarantee that health data remains within its source jurisdiction.