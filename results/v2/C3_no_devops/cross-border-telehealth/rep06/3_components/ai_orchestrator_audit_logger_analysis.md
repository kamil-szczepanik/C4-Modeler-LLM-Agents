## Overview
The Cross-Border Telehealth Platform provides video consultations, e-prescriptions, and an AI symptom checker for patients across the EU and US. It ensures strict regional data residency, regulatory compliance (GDPR, HIPAA, EU MDR), and high availability for low-bandwidth rural users.

## Key Elements
- Patients and Licensed Clinicians
- Regional API Gateways (Google Cloud API Gateway in `europe-west3` and `us-central1`)
- AI Orchestrator & Audit Logger (Python container)
- AI Gateway Router (Python / FastAPI)
- Model Execution Engine (PyTorch / ONNX Runtime)
- Audit Logger Interceptor (Python / gRPC Interceptor)
- Immutable Ledger Writer (Python / Google Cloud Storage & PostgreSQL Client)
- Clinician Feedback Collector (Python / FastAPI)
- Telemetry & Metrics Publisher (OpenTelemetry SDK)
- Google Cloud Pub/Sub
- Cloud SQL for PostgreSQL and Cloud KMS

## Relationships
- Regional API Gateways -> AI Gateway Router: Routes AI symptom checks and audit requests [gRPC over mTLS]
- Regional API Gateways -> Clinician Feedback Collector: Routes doctor validation inputs [gRPC over mTLS]
- AI Orchestrator & Audit Logger -> Google Cloud Pub/Sub: Publishes signed audit events asynchronously [Cloud Pub/Sub API over mTLS]
- AI Orchestrator & Audit Logger -> AI Symptom Checker Model Registry: Accesses and loads models [gRPC / HTTPS]

## Technology Stack
- Google Cloud Platform (GCP): Target cloud provider across `europe-west3` and `us-central1` for localized infrastructure and data residency.
- Python & FastAPI: Powers the backend orchestration and micro-components with high developer velocity and async support.
- PyTorch / ONNX Runtime: Executes localized regional AI symptom checker models efficiently.
- Google Cloud Pub/Sub & Cloud SQL for PostgreSQL: Handles asynchronous event streaming and persistent relational storage with local write-ahead logs (WAL).
- Cloud KMS: Provides Customer-Managed Encryption Keys (CMEK) and regional key isolation for data protection.

## Rationale
This architecture guarantees strict regional data isolation to comply with GDPR and HIPAA mandates. Furthermore, it decouples audit logging via Google Cloud Pub/Sub and local WALs, ensuring EU MDR traceability without sacrificing availability for rural users on unstable connections.