## Overview
The Cross-Border Telehealth Platform provides video consultations, e-prescriptions, and an AI symptom checker for patients in the EU and US. It enforces strict regional data residency, GDPR/HIPAA compliance, and EU MDR traceability constraints on GCP.

## Key Elements
- Patients (EU/US) and Licensed Clinicians
- API Gateway & Consent Container (Envoy / Google Cloud Endpoints, Open Policy Agent)
- Core Telehealth Backend (Node.js / Go)
- Video Consultation Service (WebRTC / Janus Media Server on GCE MIGs)
- AI Symptom Checker Container (Python / FastAPI)
  - API Router / Controller
  - Inference Orchestrator
  - Model Version & Provenance Tracker
  - Data Residency Enforcer
  - Regional LLM Gateway / Client (Vertex AI SDK)
  - Clinical Safety Guardrail Filter (LangChain Guardrails)
  - Local Audit & State Store (SQLite / Cloud SQL proxy)
  - Async Event Publisher (`asyncio`)
- Interoperability Adapter (Java / Spring Boot)
- Asynchronous Event Broker (GCP Pub/Sub)
- Dedicated Audit & Logging Container (Fluentbit / OpenTelemetry)
- Regional Databases (Cloud SQL PostgreSQL, Cloud Storage, Cloud Firestore in `europe-west3` and `us-central1`)

## Relationships
- API Gateway -> AI Symptom Checker: Routes symptom check requests [gRPC over mTLS]
- API Router -> Inference Orchestrator: Manages symptom analysis [In-process]
- Inference Orchestrator -> Model Version Tracker: Logs metadata [In-process]
- Inference Orchestrator -> Clinical Safety Guardrail Filter: Validates outputs [In-process]
- Inference Orchestrator -> Regional LLM Gateway: Executes model inference [HTTPS / Vertex AI SDK]
- Model Version Tracker -> Local Audit & State Store: Persists hashes locally [SQL / In-process DB]
- Inference Orchestrator -> Async Event Publisher: Queues logs [In-process async]
- Async Event Publisher -> Asynchronous Event Broker (GCP Pub/Sub): Streams telemetry [gRPC over TLS]
- Clinical Safety Guardrail Filter -> Dedicated Audit & Logging Container: Sends raw vs. filtered logs [gRPC]
- AI Symptom Checker -> Regional Databases: Persists check histories [gRPC/SQL]

## Technology Stack
- Cloud Provider: GCP (`europe-west3` for EU, `us-central1` for US) ensuring strict regional data residency.
- AI Symptom Checker: Python with FastAPI for high-performance async processing.
- AI/ML Services: Vertex AI for regional LLM deployments.
- Guardrails: LangChain Guardrails for clinical safety validation.
- Messaging: GCP Pub/Sub for asynchronous event streaming.
- Protocols: gRPC, mTLS, HTTPS, and SQL for secure inter-component and cross-container communication.

## Rationale
This architecture segregates data regionally to comply with GDPR and HIPAA mandates while enforcing EU MDR traceability via dedicated model version tracking and audit logs. Asynchronous event publishing and regional LLM routing ensure high availability, low latency, and adherence to strict clinical safety standards.