## Overview
The Cross-Border Telehealth Platform provides video consultations, e-prescriptions, and an AI symptom checker for patients across the EU and US. The architecture enforces strict regional data residency, HIPAA/GDPR compliance, and EU MDR traceability.

## Key Elements
- Patients & Licensed Clinicians
- API Gateway (Envoy / Google Cloud API Gateway)
- AI Symptom Checker Service (Python / FastAPI)
- API Controller Component
- Inference Orchestrator Component
- Audit & Compliance Logger Component
- Response Formatting & Disclaimer Engine Component
- Data Storage Layer (Cloud SQL PostgreSQL + WORM Cloud Storage)
- Vertex AI Model Registry

## Relationships
- API Gateway -> API Controller: Routes symptom checking requests [gRPC over mTLS]
- API Controller -> Inference Orchestrator: Delegates pseudonymized analysis [In-memory]
- Inference Orchestrator -> Audit & Compliance Logger: Emits prediction audit events [Async Pub/Sub]
- Inference Orchestrator -> Response Formatting & Disclaimer Engine: Passes raw triage output [In-memory]
- Response Formatting & Disclaimer Engine -> API Controller: Returns compliant payload [In-memory]
- Audit & Compliance Logger -> Data Storage Layer: Writes immutable logs [SSL-enforced TCP/Postgres & WORM Storage]

## Technology Stack
- GCP (`europe-west3`, `us-central1`): Enforces regional data residency constraints.
- Python / FastAPI: Powers the AI Symptom Checker microservice.
- Vertex AI Model Registry: Manages model versioning, cryptographic signing, and auditability.
- GCP Cloud Storage (Bucket Lock): Implements WORM storage for immutable audit logs.
- OpenTelemetry: Provides distributed tracing for latency SLO enforcement (<2s p95).

## Rationale
Regional deployments and decoupled storage guarantee strict compliance with GDPR, HIPAA, and EU MDR. Asynchronous logging and optimized processing components maintain high availability and low latency for rural users.