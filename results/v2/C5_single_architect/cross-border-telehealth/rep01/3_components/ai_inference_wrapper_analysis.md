## Overview
The Cross-Border Telehealth Platform provides video consultations, e-prescriptions, and an AI symptom checker for EU and US patients. It ensures strict data residency, regulatory compliance, and resilience for low-bandwidth rural connections on GCP.

## Key Elements
* Patients & Clinicians (Users)
* API Gateway (Cloud API Gateway)
* Core Telehealth Service (Go / gRPC)
* AI Inference Wrapper (Python / FastAPI)
* Inference Router (Python / FastAPI)
* Model Client Adapter (Python / LangChain / HTTPX)
* Audit & Traceability Logger (Python / Google Cloud Logging & SQLAlchemy)
* Consent Enforcement Interceptor (Python Middleware)
* LiveKit SFU Media Server (GKE)
* US FHIR Adapter (Node.js / TypeScript)
* EU E-Prescription Gateway (Java / Spring Boot)
* Cloud SQL PostgreSQL & Cloud Storage (GCP)
* Google Cloud Pub/Sub
* External Systems: Identity Providers, Payment Gateway, External Pharmacy Systems, AI Symptom Checker

## Relationships
* API Gateway -> AI Inference Wrapper: Routes AI symptom check requests [gRPC and HTTPS]
* Inference Router -> Model Client Adapter: Internal function calls [Python]
* Inference Router -> Audit & Traceability Logger: Asynchronous event dispatch [Google Cloud Pub/Sub]
* Model Client Adapter -> External AI Symptom Checker: Secure API calls [HTTPS / JSON]
* Inference Router -> Core Telehealth Service: Validates patient consent tokens [gRPC]

## Technology Stack
* GCP (`europe-west3`, `us-central1`): Enforces regional data residency for EU and US health data.
* Python / FastAPI: Powers the AI Inference Wrapper and Inference Router for high-performance API handling.
* Google Cloud Pub/Sub: Ensures zero log loss for traceability events during worker restarts.
* Google Cloud Logging & Cloud SQL PostgreSQL: Stores immutable audit logs and relational data locally per region.
* LangChain / HTTPX: Manages reliable model client communication and payload sanitization.

## Rationale
This architecture enforces GDPR and HIPAA compliance by isolating regional data workloads while maintaining end-to-end traceability for AI medical outputs. The decoupled component design within GCP guarantees high availability and audit accountability across both regions.