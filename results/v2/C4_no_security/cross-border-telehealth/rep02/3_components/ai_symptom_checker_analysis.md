## Overview
[The AI Symptom Checker container uses a Python/FastAPI microservice architecture deployed on Google Cloud Platform to provide traceable, explainable medical triage for patients in the EU and US. It delivers asynchronous symptom evaluation and audit logging while strictly enforcing regional data residency and compliance.]

## Key Elements
- Triage API Controller: FastAPI-based component exposing asynchronous endpoints for step-by-step symptom evaluation.
- Inference Engine Component: PyTorch and LangChain-based service running localized diagnostic models to generate urgency scores and plain-language rationales.
- Audit & Traceability Logger: Captures model versions, feature inputs, and output urgency levels for regulatory compliance.
- Feedback Ingestion Component: Handles post-triage patient feedback and escalation metrics.
- Infrastructure: GKE Autopilot with NVIDIA L4 GPU regional node pools in `europe-west3` and `us-central1`.
- Storage & Observability: Cloud SQL (PostgreSQL), Google Artifact Registry, BigQuery via Fluentbit sidecars, and Pub/Sub dead-letter queues.

## Relationships
- Core Backend -> Triage API Controller: Sends symptom evaluation requests and post-triage feedback via gRPC.
- Triage API Controller -> Inference Engine Component: Invokes diagnostic models internally.
- Inference Engine -> Audit & Traceability Logger: Transmits structured reasoning and model version metadata.
- Audit & Traceability Logger -> BigQuery / Cloud SQL: Persists regional audit trails and feedback telemetry.
- Audit & Traceability Logger -> Pub/Sub: Routes failed audit payloads to a dead-letter queue.

## Technology Stack
- Python / FastAPI: Powers the AI Symptom Checker container for high-performance asynchronous API handling.
- PyTorch & LangChain: Executes localized LLM and diagnostic workloads.
- Protobuf / gRPC: Enforces strict data contracts and communication between the Core Backend and FastAPI service.
- GKE Autopilot & NVIDIA L4 GPUs: Provides scalable, managed infrastructure for AI inference workloads.
- OpenTelemetry & Prometheus: Handles distributed tracing and regional performance monitoring.
- BigQuery & Cloud SQL: Ensures partitioned, region-locked storage for HIPAA and GDPR compliance.

## Rationale
[This architecture satisfies EU MDR and HIPAA requirements by enforcing strict regional data residency in GCP and maintaining immutable audit trails for every AI recommendation. Additionally, asynchronous FastAPI endpoints and GKE Autopilot scaling ensure robust performance for users with unstable rural internet connections.]