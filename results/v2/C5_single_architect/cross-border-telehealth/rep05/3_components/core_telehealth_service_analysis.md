## Overview
The Core Telehealth Service is a Go-based container running on Google Kubernetes Engine (GKE) that handles video consultations, prescription routing, and AI triage. It operates across EU (`europe-west3`) and US (`us-central1`) regions to fulfill cross-border healthcare requirements.

## Key Elements
- Patients (EU and US) and Clinicians (External Users)
- API Gateway & Routing Layer (Google Cloud Load Balancing, Apigee)
- Core Telehealth Service (Go on GKE) containing:
  - Consultation Session Manager (Go)
  - Prescription Coordinator (Go)
  - Consent Enforcement Engine (Go)
  - Symptom Checker Orchestrator (Go)
  - Telemetry & Audit Interceptor (Go)
- Video Media Server (WebRTC SFU on GKE)
- AI Inference Wrapper (Python on Vertex AI)
- Integration Service (Go / Camel-K on GKE)
- Audit & Traceability Ledger (Cloud Pub/Sub, BigQuery)
- Datastores (Cloud SQL PostgreSQL)

## Relationships
- API Gateway & Routing Layer -> Core Telehealth Service: Routes regional traffic [gRPC / HTTP]
- Consultation Session Manager -> Video Media Server: Coordinates media stream parameters [gRPC]
- Prescription Coordinator -> Integration Service: Routes prescription payloads [gRPC / REST]
- Consent Enforcement Engine -> Datastores: Executes localized queries [SQL]
- Symptom Checker Orchestrator -> AI Inference Wrapper: Requests triage urgency [gRPC]
- Telemetry & Audit Interceptor -> Audit & Traceability Ledger: Publishes immutable audit logs [Cloud Pub/Sub]

## Technology Stack
- Go (GKE): Chosen for high concurrency and performance in core telehealth components.
- Python (Vertex AI): Used for hosting and invoking the AI symptom checker model.
- Cloud SQL PostgreSQL: Provides regional relational storage enforcing GDPR and HIPAA data residency.
- WebRTC SFU: Enables real-time video consultations with low-bandwidth fallback capabilities.
- Cloud Pub/Sub & BigQuery: Captures immutable audit trails for AI traceability and system accountability.

## Rationale
This architecture enforces strict regional data isolation to meet GDPR and HIPAA compliance mandates. It guarantees low-latency, resilient telehealth workflows for unstable rural networks via WebRTC optimizations and native Go component integration.