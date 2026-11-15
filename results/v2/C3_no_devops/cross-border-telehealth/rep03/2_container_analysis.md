## Overview
The Cross-Border Telehealth Platform provides secure video consultations, e-prescriptions, and an AI symptom checker for patients in the EU and US. It ensures strict regional data residency, regulatory compliance, and resilience for low-bandwidth users.

## Key Elements
- **Users**: Patients, Licensed Clinicians, Pharmacy Staff, Platform Administrators / Compliance Officers.
- **Client Layer**: Web & Mobile Client Apps (Flutter/React Native).
- **Edge Layer**: API Gateway (Google Cloud API Gateway / Apigee).
- **Core Microservices**: Core Telehealth Service, AI Symptom Checker Service, Interoperability & E-Prescription Service.
- **Media Layer**: WebRTC SFU Media Relay (LiveKit on GKE).
- **Data & Security**: Regional Cloud SQL (PostgreSQL), Cloud Storage, GCP Cloud KMS, GCP Service Mesh (Istio).

## Relationships
- **Clients to API Gateway**: HTTPS and GraphQL over TLS 1.3.
- **API Gateway to Services**: Regional internal routing via gRPC with service-to-service mTLS (GCP Service Mesh / Istio).
- **Core Telehealth Service to Data Layer**: Encrypted database connections using Cloud KMS keys.
- **Video Consultations**: WebRTC, SRTP, and DTLS media streaming via regional SFU Media Relays.
- **Interoperability Service to External Systems**: HL7 FHIR (US) and national e-prescription standards (EU).

## Technology Stack
- **Cloud Provider**: GCP (`europe-west3` for EU, `us-central1` for US) for strict regional isolation.
- **Frontend**: Flutter and React Native for mobile-first, low-bandwidth optimized client applications.
- **Backend Services**: Spring Boot / Java (Core Telehealth) and FastAPI / Python (AI Symptom Checker).
- **Interoperability**: Node.js for payload translation to HL7 FHIR and EU e-prescription formats.
- **Media Streaming**: LiveKit on GKE for WebRTC adaptive bitrate streaming.
- **Security & Infrastructure**: GCP Service Mesh, Cloud KMS for envelope encryption, and Workload Identity.

## Rationale
This architecture guarantees GDPR and HIPAA compliance by enforcing strict regional data residency and localized VPC isolation. It ensures high availability and accountability for medical devices through decentralized microservices, robust encryption, and immutable audit logging.