## Overview
[Cross-Border Telehealth Platform provides video consultations, e-prescriptions, and an AI symptom checker for EU and US patients. The architecture uses Google Cloud Platform (GCP) with regional separation to ensure strict data residency, security, and EU MDR/HIPAA compliance.]

## Key Elements
- Patients (EU & US) & Licensed Clinicians
- Web / Mobile Client (React / React Native)
- API Gateway (Envoy / Cloud Endpoints)
- Core Telehealth Service (Node.js / NestJS)
- AI Symptom Service (Python / FastAPI)
- Cloud Storage WORM buckets (GCP Cloud Storage WORM with Compliance Mode)
- Google Cloud SQL (PostgreSQL with CMEK)
- Third-Party WebRTC SFU & AI Model Registry / Inference Service

## Relationships
- Web / Mobile Client -> API Gateway: Client requests [HTTPS / WSS]
- API Gateway -> Core Telehealth Service: Routed API calls [gRPC / HTTPS]
- AI Symptom Service -> Cloud Storage WORM buckets: Direct write of immutable audit payloads [HTTPS / Cloud Storage API]
- Core Telehealth Service -> Cloud Storage WORM buckets: Read audit payloads on behalf of clinicians [HTTPS / Cloud Storage API]
- Licensed Clinicians -> Core Telehealth Service: Request AI audit payloads during consultations [HTTPS]

## Technology Stack
- GCP (europe-west3, us-central1): Core cloud provider for regional data residency isolation (R-05)
- GCP Cloud Storage WORM: Immutable storage with Compliance Mode locks for EU MDR audit traceability (R-03, R-07)
- Node.js / NestJS & Python / FastAPI: Backend services for telehealth logic and AI symptom processing
- Cloud KMS: Customer-Managed Encryption Keys (CMEK) with regional key rings for data protection
- Terraform: Infrastructure-as-Code for automated, policy-enforced bucket and IAM deployments

## Rationale
[This architecture enforces regional data boundaries and immutability guarantees required by GDPR, HIPAA, and EU MDR. Routing clinician reads through the core API preserves WORM security while enabling consent-aware, low-latency access during active consultations.]