## Overview
The Cross-Border Telehealth Platform provides video consultations, e-prescriptions, and an AI symptom checker for patients across the EU and US. It ensures strict regional data residency, regulatory compliance, and high availability for users with unstable internet connections.

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
- React / Next.js for Web Application Container to support Server-Side Rendering and rural performance
- Envoy / GCP API Gateway for secure routing and traffic management
- Go / Node.js for Core Services Container microservices for performance and scalability
- Python / FastAPI + Vertex AI for AI Symptom Checker Container to deliver versioned recommendations
- Janus / WebRTC SFU for Media Relay Container to handle real-time video consultations
- Java / Spring Boot for E-Prescription Integration Container to ensure reliable gateway integrations
- GCP Cloud SQL for PostgreSQL secured via CMEK for persistent relational data storage

## Rationale
This architecture uses regional GCP deployments in `europe-west3` and `us-central1` to strictly enforce data residency and regulatory compliance. It incorporates resilient frontend caching and media relay technologies to maintain service availability under unstable rural network conditions.