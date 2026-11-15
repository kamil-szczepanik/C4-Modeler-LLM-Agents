## Overview
The Cross-Border Telehealth Platform provides secure video consultations, e-prescriptions, and an AI symptom checker for patients across the EU and US. It strictly enforces regional data residency and compliance using GCP infrastructure.

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
- Cross-Border Telehealth Platform -> Identity Providers (eIDAS / OAuth2/OIDC) [OIDC/OAuth2]
- Cross-Border Telehealth Platform -> Regional Payment & Insurance Gateways [HTTPS/REST with tokenization via GCP VPC Service Controls]

## Technology Stack
- Google Cloud Platform (GCP): Target cloud infrastructure in `europe-west3` and `us-central1` for data residency.
- React / Next.js: Frontend web application framework.
- Envoy / GCP API Gateway: API routing and management.
- Go / Node.js: Core business logic microservices.
- Python / FastAPI + Vertex AI: AI symptom checker processing and model inference.
- Janus / WebRTC SFU: Media relay for real-time video consultations.
- Java / Spring Boot: E-Prescription Integration Container with Spring Cloud OpenFeign and Resilience4j.
- GCP Cloud SQL for PostgreSQL: Relational database secured via CMEK.

## Rationale
This architecture ensures strict GDPR and HIPAA compliance by isolating regional data storage and processing within `europe-west3` and `us-central1`. Microservices and resilient gateway integrations guarantee continuous operation even under unstable network conditions.