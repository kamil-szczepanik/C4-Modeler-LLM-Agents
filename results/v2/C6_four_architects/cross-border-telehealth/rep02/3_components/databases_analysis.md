## Overview
The Cross-Border Telehealth Platform provides secure video consultations, e-prescriptions, and an AI symptom checker for patients across the EU and US. It ensures strict regional data residency, regulatory compliance, and high availability over unstable connections.

## Key Elements
- Patients and Clinicians (Users)
- Global Media Relay Network, National E-Prescription Gateways (EU), US Pharmacy Networks, Identity & Consent Providers, AI Model Registry & Inference Provider (External Systems)
- Web & Mobile Clients (React / React Native)
- API Gateway & Routing (Kong / GCP API Gateway)
- Core Telehealth Service (Java / Spring Boot)
- WebRTC Media Broker (Node.js / Mediasoup)
- AI Symptom Checker Service (Python / FastAPI)
- FHIR & E-Prescription Integration Service (Python / Java)
- Consent & Audit Logging Service (Go)
- Messaging (Cloud Pub/Sub)
- Databases (Cloud SQL PostgreSQL, Cloud Storage, Regional Memorystore for Redis)

## Relationships
- Web & Mobile Clients -> API Gateway & Routing: HTTPS / WSS over TLS 1.3
- API Gateway & Routing -> Core Telehealth Service: gRPC / REST over TLS 1.3
- Core Telehealth Service -> WebRTC Media Broker: WebRTC / DTLS over UDP/TCP
- AI Symptom Checker Service -> AI Model Registry & Inference Provider: HTTPS over TLS 1.3
- FHIR & E-Prescription Integration Service -> National E-Prescription Gateways / US Pharmacy Networks: HL7 FHIR / National APIs over TLS 1.3
- Consent & Audit Logging Service -> Databases: Stores audit logs and consent records encrypted via CMEK (Cloud Storage / Cloud SQL)

## Technology Stack
- GCP (europe-west3, us-central1): Cloud provider and isolated regional hosting ensuring data residency.
- Cloud SQL for PostgreSQL: Regional transactional databases with Row-Level Security (RLS) for patient data and consent enforcement.
- Cloud Storage: Regional WORM buckets with CMEK for immutable AI traceability logging.
- Regional Memorystore for Redis: Fast patient-to-region mapping caches.
- React / React Native: Cross-platform web and mobile client interfaces.
- Java (Spring Boot) & Python (FastAPI): Robust backend services for telehealth logic and AI processing.
- WebRTC (Mediasoup): Real-time video communication supporting degraded connection modes.

## Rationale
This architecture strictly enforces GDPR and HIPAA data residency mandates by isolating all operational data and backups within regional GCP boundaries. Furthermore, it guarantees compliance, auditability, and interoperability through regional database partitioning, cryptographic logging, and adherence to local healthcare standards.