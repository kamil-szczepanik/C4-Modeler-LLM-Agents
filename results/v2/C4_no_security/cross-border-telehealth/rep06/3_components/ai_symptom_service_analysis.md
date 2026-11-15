## Overview
[A secure, cross-border telehealth platform providing video consultations, e-prescriptions, and an AI-driven symptom checker for patients across the EU and US. The system ensures strict regional data residency, GDPR/HIPAA compliance, and traceability under EU MDR.]

## Key Elements
* Patients (EU and US) and Licensed Clinicians
* API Gateway (GCP Cloud Endpoints / API Gateway)
* AI Symptom Service (Python / FastAPI)
* API Router / Controller Component
* Localization & Normalization Engine (with Clinical Semantic Normalizer sub-component)
* LLM Orchestrator Component
* Audit & Traceability Logger Component
* AI LLM Provider (External)
* Regional Storage & Messaging (GCP Cloud SQL PostgreSQL, Pub/Sub, Cloud Storage with WORM)

## Relationships
* API Gateway -> AI Symptom Service: Routes symptom check requests [gRPC / REST / HTTPS]
* API Router / Controller -> Localization & Normalization Engine: Passes raw patient inputs [In-memory Pydantic models]
* Localization & Normalization Engine -> LLM Orchestrator: Sends normalized clinical data [In-memory Pydantic models]
* LLM Orchestrator -> AI LLM Provider: Sends diagnostic prompts and receives AI responses [HTTPS]
* Audit & Traceability Logger -> Regional Cloud Storage: Writes versioned inputs, outputs, and model versions [HTTPS / Direct Write]

## Technology Stack
* GCP Cloud Run / GKE: Region-isolated hosting (europe-west3 and us-central1) for strict data residency.
* Python / FastAPI: Core framework for the AI Symptom Service and internal Pydantic typing.
* GCP Secret Manager: Secures regional API keys and localization dictionaries.
* GCP Cloud Storage: WORM-compliant storage with Object Versioning for MDR-compliant audit logs.
* GCP Pub/Sub Lite / Local Redis: Asynchronous buffering for audit logs to maintain resilience during network degradation.

## Rationale
[This architecture enforces regional data segregation to meet strict GDPR and HIPAA mandates while isolating AI triage logic to ensure low latency. Component decomposition and asynchronous logging protect platform availability and EU MDR traceability requirements even under unstable network conditions.]