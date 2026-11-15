## Overview
The Cross-Border Telehealth Platform provides video consultations, e-prescriptions, and an AI symptom checker for patients in the EU and US. It enforces strict regional data residency while ensuring regulatory compliance, interoperability, and low-bandwidth availability.

## Key Elements
- Patients and Clinicians (External Actors)
- Telehealth Platform (EU) (`europe-west3`) and Telehealth Platform (US) (`us-central1`) (Regional Systems)
- Global Media Relay Network (External WebRTC Infrastructure)
- National E-Prescription Gateways (EU) and US Pharmacy Networks (External Systems)
- Identity & Consent Providers (Regional External IDPs)
- AI Model Registry & Inference Provider (External ML Service)
- API Gateway / BFF (Cloud Run / Cloud Load Balancing)
- Consultation Service & AI Proxy & Audit Service (GKE Microservices)
- Consent & Identity Service & E-Prescription Integration Service (Cloud Run Containers)
- Cloud SQL (PostgreSQL) and Cloud Storage (Regional Persistence)

## Relationships
- Patients & Clinicians to Global Media Relay Network via WebRTC/UDP/TCP over TLS (Video consultations)
- Patients & Clinicians to API Gateway / BFF via HTTPS/WebSockets (Signaling and app interactions)
- API Gateway to Regional Microservices via internal gRPC over mTLS
- E-Prescription Integration Service to National Gateways/Pharmacy Networks via HTTPS/REST (HL7 FHIR in US)
- AI Proxy Service to AI Model Registry via gRPC/HTTPS

## Technology Stack
- Google Cloud Platform (GCP): Selected for robust regional isolation (`europe-west3` and `us-central1`).
- Google Kubernetes Engine (GKE) & Cloud Run: Used for container orchestration and scalable microservices.
- WebRTC: Enables low-bandwidth video down to 300 kbit/s via edge relays.
- Cloud SQL (PostgreSQL) & Cloud Storage: Provides regional persistence with Customer-Managed Encryption Keys (CMEK).
- Google Cloud Pub/Sub: Powers asynchronous audit logging for AI traceability.

## Rationale
Splitting the system into two distinct regional platforms guarantees compliance with GDPR and HIPAA data residency constraints. Delegating media streaming to edge relays and utilizing gRPC over mTLS ensures high availability in degraded network conditions and secure, low-latency internal communication.