## Overview
The Cross-Border Telehealth Platform provides video consultations, e-prescriptions, and an AI symptom checker for patients across the EU and US. It ensures strict regional data residency, HIPAA/GDPR compliance, and EU MDR AI traceability.

## Key Elements
* **Inference Controller**: FastAPI component exposing REST/gRPC endpoints and enforcing region isolation headers.
* **Consent & Policy Enforcer**: Middleware validating patient consent and geographic compliance before processing.
* **Region-Aware AI Gateway Client**: Client routing requests securely to regional AI services via gRPC.
* **Audit & Traceability Logger**: SDK capturing exact inputs, model versions, and outputs for EU MDR compliance.
* **Cloud SQL PostgreSQL**: Regional database storing versioned audit logs and persistent data.

## Relationships
* `Inference Controller` -> `Consent & Policy Enforcer`: Validates regional consent [In-memory]
* `Consent & Policy Enforcer` -> `Region-Aware AI Gateway Client`: Authorizes request dispatch [In-memory]
* `Inference Controller` -> `Region-Aware AI Gateway Client`: Invokes inference [In-memory]
* `Inference Controller` -> `Audit & Traceability Logger`: Dispatches audit payloads [Asyncio Queue]
* `Audit & Traceability Logger` -> `Cloud SQL PostgreSQL`: Writes versioned audit logs [SQLAlchemy via TLS 1.3]

## Technology Stack
* **Python / FastAPI**: Chosen for the AI Symptom Checker Orchestrator to support rapid AI ecosystem integration.
* **gRPC**: Used for secure, low-latency inter-service and gateway communication.
* **SQLAlchemy / Cloud SQL PostgreSQL**: Provides reliable, encrypted regional persistence via TLS 1.3.
* **GCP (europe-west3, us-central1)**: Ensures strict geographic data residency separation between the EU and US.

## Rationale
This architecture enforces strict regional data isolation to satisfy EU and US healthcare regulations. Explicit consent validation and immutable version logging ensure full compliance with EU MDR traceability mandates.