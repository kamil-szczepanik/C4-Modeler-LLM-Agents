## Overview
The Cross-Border Telehealth Platform provides secure video consultations, e-prescriptions, and AI symptom checks for patients in the EU and US. It runs on GCP across regional clusters in `europe-west3` and `us-central1` to ensure strict health data residency compliance.

## Key Elements
- Patients (EU / US)
- Licensed Clinicians
- Web Applications (Flutter / HTML5 / CSS)
- Native Mobile Apps (Flutter)
- GCP Global HTTP(S) Load Balancer
- Kong / GCP API Gateway
- Consultation Service (Go / Node.js)
- Media Relay / SFU Container (LiveKit / Go)
- Consent Management Service (Go / Node.js)
- Prescription & Interoperability Service (Java / Spring Boot)
- AI Inference Orchestrator (Python / FastAPI)
- GKE Regional Clusters (Google Kubernetes Engine with SPIFFE/SPIRE mTLS)
- Google Cloud TURN/STUN Relays
- GCP Cloud Spanner
- GCP BigQuery

## Relationships
- Web and Mobile Apps -> Global External HTTP(S) Load Balancer [HTTPS / WSS]
- Global External HTTP(S) Load Balancer -> Regional API Gateways [HTTPS / gRPC]
- Regional API Gateways -> Consultation Service [gRPC]
- Consultation Service -> Media Relay / SFU Container (Signaling & Room Manager) [gRPC]
- Media Relay / SFU Container -> Regional TURN/STUN Relays [ICE / TURN / UDP / TCP]
- Consultation Service -> AI Inference Orchestrator [gRPC]
- Prescription & Interoperability Service -> Local Pharmacies [HL7 FHIR / National APIs]

## Technology Stack
- **Compute & Orchestration:** Google Kubernetes Engine (GKE) with GKE Autopilot for automated container management and scaling.
- **Media Streaming:** LiveKit (Go) for Selective Forwarding Unit (SFU) real-time video handling.
- **Database & Storage:** GCP Cloud Spanner for transactional data with regional partitioning.
- **Data Analytics:** GCP BigQuery for traceable AI symptom checker audit logs.
- **Security & Networking:** SPIFFE/SPIRE for mTLS service identity, DTLS 1.3 / SRTP for encrypted media streams.

## Rationale
This architecture uses GCP regional clusters to enforce strict data residency boundaries between the EU and US, satisfying GDPR and HIPAA constraints. The LiveKit-based SFU container and ABR controller support unstable rural connections via adaptive bitrate streaming and low-bandwidth degraded modes.