## Overview
A cross-border telehealth platform delivering video consultations, AI-driven symptom checking, and e-prescriptions for patients in the EU and US. The system guarantees strict data residency, regulatory compliance (GDPR/HIPAA/MDR), and high availability over unstable connections.

## Key Elements
- **Users**: Patients, Licensed Clinicians, Compliance Officers.
- **Client Apps**: Flutter / Web application.
- **API Gateway**: Google Cloud API Gateway / Envoy.
- **Core Telehealth Service**: Node.js / Go container.
- **AI Symptom Checker Container**: Python / FastAPI.
- **Patient Consent Service**: Node.js / Go container.
- **Pharmacy Integration Gateway**: Go / Apache Camel container.
- **Video Media Server**: LiveKit / WebRTC SFU.
- **Data Storage**: Regional Google Cloud SQL (PostgreSQL with FHIR extensions).
- **External Systems**: EU National E-Prescription Gateways, US Pharmacy Networks, TURN Infrastructure.

## Relationships
- **Client Apps to API Gateway**: HTTPS / WebSockets.
- **API Gateway to Core & Microservices**: gRPC (internal service-to-service with mTLS).
- **Client Apps to Video Media Server**: WebRTC (SRTP with DTLS-SRTP) for video streaming.
- **Pharmacy Integration Gateway to External Gateways**: mTLS over HTTPS for e-prescriptions.
- **Services to Data Storage**: Encrypted SQL connections isolated to regional databases.

## Technology Stack
- **Cloud Infrastructure**: Google Cloud Platform (GCP) deployed in `europe-west3` and `us-central1` for data residency.
- **Backend & APIs**: Node.js, Go, and Python (FastAPI) for scalable microservices.
- **Data & Security**: Google Cloud SQL (PostgreSQL), Cloud KMS (CMEK encryption), OAuth2/OIDC with JWT claims.
- **Integration & Messaging**: GCP Pub/Sub for asynchronous dispatch; HL7 FHIR (US) and national standards (EU).
- **Media**: LiveKit / WebRTC SFU with adaptive bitrate for low-bandwidth resilience.

## Rationale
Regional container duplication in `europe-west3` and `us-central1` strictly enforces EU and US health data residency laws. Decoupling compliance, consent, and pharmacy integration into dedicated microservices isolates jurisdictional complexity while ensuring low-latency care and resilience over unstable connections.