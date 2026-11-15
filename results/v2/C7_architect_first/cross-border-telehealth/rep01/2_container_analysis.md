## Overview
The Cross-Border Telehealth Platform provides secure video consultations, e-prescriptions, and an AI symptom checker for patients in the EU and US. It ensures strict data residency, regulatory compliance, and high availability over unstable connections.

## Key Elements
- Patients and Licensed Clinicians (Users)
- GCP API Gateway (Cloud Endpoints)
- Web Application & Mobile App Containers (React/React Native)
- Core Services GKE Clusters (Consultation, Prescription, AI Symptom Checker, Consent & Policy, Notification, Localization, BI Ingestion)
- Data Containers (Cloud SQL PostgreSQL, Cloud Storage with WORM policies)
- Media Relay Containers (Coturn TURN/STUN, Mediasoup SFU)
- External Systems (EU National e-Prescription Gateways, US Pharmacy Networks, Third-Party AI Model Providers, Identity Providers)

## Relationships
- Patients/Clinicians interact with API Gateway via HTTPS/WSS
- API Gateway routes requests to regional GKE services via gRPC over mTLS
- Consultation Service connects to Media Relay Containers via WebRTC (DTLS-SRTP)
- Prescription Service integrates with EU e-prescription gateways and US HL7 FHIR networks
- AI Symptom Checker invokes Third-Party AI Models via Istio Egress Gateways with anonymized payloads

## Technology Stack
- Google Cloud Platform (`europe-west3`, `us-central1`): Core cloud infrastructure providing strict regional isolation
- Google Kubernetes Engine (GKE): Container orchestration with multi-primary network topology
- Istio Service Mesh: Enforces mTLS, traffic routing, and egress filtering
- Cloud SQL (PostgreSQL) & Cloud Storage: Region-isolated transactional data and encrypted medical artifacts
- Cloud KMS & Secret Manager: Customer-Managed Encryption Keys (CMEK) and runtime secret injection

## Rationale
This architecture uses GCP multi-region isolation and Istio service mesh to strictly enforce GDPR and HIPAA data residency constraints. Pluggable integration adapters, WebRTC media relays, and local mobile caching ensure interoperability and reliable telehealth delivery even over unstable rural internet connections.