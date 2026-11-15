## Overview
The Cross-Border Telehealth Platform provides video consultations, e-prescriptions, and an AI symptom checker for patients in the EU and US. It enforces strict regional data residency, GDPR/HIPAA compliance, and medical traceability on GCP.

## Key Elements
- Patients (EU/US) & Licensed Clinicians
- API Gateway (GCP Cloud Endpoints / Envoy)
- Core Telehealth Service (Go / gRPC)
- AI Symptom Checker Service (Python / FastAPI on Cloud Run)
  - Intake & Normalization Component
  - Inference & Explainability Engine (Vertex AI)
  - Audit & Traceability Component
  - Handoff Formatter Component
- Regional Data Storage & Audit Layer (Cloud SQL, BigQuery)
- Regional Pharmacy Networks & Identity Providers

## Relationships
- Patients/Clinicians -> API Gateway: Client requests [HTTPS / gRPC]
- API Gateway -> AI Symptom Checker Service: Routes requests [geo-DNS, gRPC]
- AI Symptom Checker Service -> Vertex AI: ML inference requests [gRPC]
- AI Symptom Checker Service -> Regional Data Storage & Audit Layer: Persists audit logs and WORM storage [VPC Service Controls, BigQuery]
- Core Telehealth Service -> AI Symptom Checker Service: Communicates internally [mTLS-secured gRPC]
- AI Symptom Checker Service -> Cloud Pub/Sub: Audit dead-letter queue overflow [gRPC]

## Technology Stack
- GCP (`europe-west3`, `us-central1`): Ensures regional data residency compliance.
- Python / FastAPI on Cloud Run: Powers the containerized microservices architecture with `min-instances=1`.
- Vertex AI: Hosts machine learning models with model registry integration.
- BigQuery & Cloud Pub/Sub: Provides immutable regional audit logging and dead-letter queues.
- Go / gRPC: Powers internal high-performance service communication.

## Rationale
This architecture guarantees strict regional data isolation between the EU and US to satisfy GDPR, HIPAA, and EU MDR constraints. Microservice decomposition ensures high availability, strict audit traceability, and clinical safety via deterministic safety overrides.