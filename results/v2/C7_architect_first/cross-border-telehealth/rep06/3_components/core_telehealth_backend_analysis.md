## Overview
The Cross-Border Telehealth Platform provides secure video consultations, e-prescriptions, and an AI symptom checker for patients in the EU and US. It enforces strict regional data residency and compliance using GCP.

## Key Elements
- Patients and Licensed Clinicians
- API Gateway (Cloud Armor, Cloud Load Balancing)
- Core Telehealth Backend (Node.js, Express) containing Consultation Orchestrator, Prescription Manager, Audit & Compliance Logger, and Identity & Consent Enforcer
- AI Symptom Checker Service (Python, FastAPI)
- Video Media Router (Mediasoup SFU)
- Consent & Preference Management Service (Node.js, Express)
- Data Tier (Cloud SQL PostgreSQL, Cloud Storage, Cloud KMS)
- External EU National E-Prescription Gateways and US Pharmacy Networks

## Relationships
- API Gateway -> Core Telehealth Backend: Routes API requests [gRPC / mTLS]
- Consultation Orchestrator -> Video Media Router: Coordinates video sessions [WebRTC]
- Consultation Orchestrator & Prescription Manager -> Identity & Consent Enforcer: Validates access rights and consent scopes [Internal gRPC]
- Core Telehealth Backend & Audit & Compliance Logger -> Data Tier: Reads/writes clinical and immutable compliance data [TCP/PostgreSQL]
- Prescription Manager -> External EU Gateways / US Pharmacy Networks: Transmits regional prescriptions [HTTPS / TLS 1.3]

## Technology Stack
- Google Cloud Platform (GCP): Target cloud provider utilizing regions `europe-west3` and `us-central1` for data residency.
- Node.js & Express: Powers the Core Telehealth Backend and Consent services for asynchronous I/O handling.
- Python & FastAPI: Powers the AI Symptom Checker Service for rapid machine learning inference.
- Google Kubernetes Engine (GKE): Deploys region-isolated backend containers.
- Cloud SQL PostgreSQL: Stores region-locked transactional and audit data.
- Cloud KMS: Provides customer-managed encryption keys (CMEK) and cryptographic sealing for audit logs.

## Rationale
This architecture enforces strict GDPR and HIPAA compliance by isolating regional health data within GCP `europe-west3` and `us-central1`. Zero-trust mTLS, cryptographically signed audit logs, and dedicated consent enforcement meet rigorous healthcare accountability and interoperability requirements.