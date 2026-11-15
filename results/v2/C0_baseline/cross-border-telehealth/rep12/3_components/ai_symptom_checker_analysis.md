## Overview
[Cross-Border Telehealth Platform providing video consultations, e-prescriptions, and an AI symptom checker for EU and US patients.]
[Ensures strict GDPR/HIPAA compliance, regional data residency, and MDR traceability using GCP infrastructure.]

## Key Elements
* Patients, Licensed Clinicians, Pharmacies, Compliance Officers/Auditors
* Web/Mobile Client Applications (Flutter / React Native)
* Cloud Load Balancing / API Gateway (OAuth2/OIDC, TLS 1.3)
* AI Symptom Checker Container (Python / FastAPI on Cloud Run)
  - API Router, Triage Orchestrator, LLM/Inference Adapter (Vertex AI), Audit & Traceability Logger, Localization & Terminology Adapter, Clinical Handoff Dispatcher
* Core Telehealth & E-Prescription (Spring Boot on GKE)
* Consent Management Service (Spring Boot on GKE)
* Google Cloud Pub/Sub, BigQuery, Google Cloud KMS (CMEK), Secret Manager

## Relationships
* Web/Mobile Client -> Cloud Load Balancing / API Gateway [HTTPS / TLS 1.3, OAuth2/OIDC]
* Cloud Load Balancing / API Gateway -> AI Symptom Checker [gRPC over mTLS]
* Triage Orchestrator -> LLM/Inference Adapter [In-Memory]
* Triage Orchestrator -> Audit & Traceability Logger [Async via Google Cloud Pub/Sub]
* Clinical Handoff Dispatcher -> Cloud Pub/Sub [gRPC] for urgent consultations (R-01/R-03)

## Technology Stack
* GCP (`europe-west3`, `us-central1`): Ensures regional data residency per compliance requirements.
* Cloud Run & GKE: Provides serverless scaling for AI services and robust container orchestration for core services.
* Vertex AI: Powers regional AI symptom analysis with traceable model versions.
* Python / FastAPI: Delivers high-performance asynchronous API routing for the AI Symptom Checker.
* Google Cloud Pub/Sub & BigQuery: Enables decoupled asynchronous audit logging and regional event-driven clinical handoffs.

## Rationale
[This architecture satisfies rigorous GDPR, HIPAA, and EU MDR constraints by enforcing strict regional data residency and immutable audit trails via GCP.]
[It guarantees high availability and traceability for critical health workflows through decoupled asynchronous messaging and robust serverless scaling.]