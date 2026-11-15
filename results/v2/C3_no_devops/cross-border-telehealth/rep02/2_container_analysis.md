## Overview
[Cross-Border Telehealth Platform providing video consultations, e-prescriptions, and an AI symptom checker across the EU and US. Operates on GCP with strict regional data residency isolation.]

## Key Elements
- Patients (EU/US), Licensed Clinicians, Pharmacies, Compliance Officers
- Web & Mobile Client Containers (Flutter/React Native with offline-first caching)
- API Gateway (Cloud Endpoints / Apigee)
- Core Telehealth Backend (Node.js/Go in GKE)
- Patient Consent & Preference Service Container (Go in GKE)
- Video Streaming Gateway (WebRTC SFU / MediaSoup on GCE/GKE)
- AI Inference Wrapper Service (Python/FastAPI)
- Regionally Isolated Cloud SQL (PostgreSQL) and Cloud Storage

## Relationships
- Clients to API Gateway: HTTPS/gRPC via mTLS
- API Gateway to Microservices: gRPC over mTLS with cryptographically signed JWTs
- Clients to Video Gateway: WebRTC media streams with SRTP/DTLS (E2EE)
- Services to Datastores: Regional GCP Cloud SQL and Cloud Storage using CMEK via Cloud KMS

## Technology Stack
- Cloud Provider: GCP (Regions: `europe-west3` for EU, `us-central1` for US) to enforce R-05 data residency
- Compute: Google Kubernetes Engine (GKE) and Google Compute Engine (GCE) for microservices and video streaming
- Databases: Cloud SQL (PostgreSQL) and Cloud Storage with Cloud KMS encryption
- Security: GCP Secret Manager for asymmetric key rotation and workload identity federation

## Rationale
[Regional GKE separation guarantees strict GDPR and HIPAA compliance while maintaining localized data residency. Zero-trust networking, E2EE video, and dedicated consent services ensure high availability, privacy, and regulatory traceability.]