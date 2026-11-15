## Overview
Cross-Border Telehealth Platform provides video consultations, e-prescriptions, and an AI symptom checker for patients across the EU and US. It guarantees strict regional data residency, regulatory compliance, and resilience for unstable network connections.

## Key Elements
- Patients (EU/US) and Licensed Clinicians
- Google Cloud Platform (GCP)
- API Gateway (Envoy and Google Cloud Load Balancing)
- Core Telehealth Service (Go Container)
- E-Prescription Integration Service (Java / Spring Boot)
- AI Symptom Checker Service (Python / FastAPI)
- Media Streaming Container (Janus WebRTC SFU)
- Appointment Orchestrator Component (Temporal SDK)
- Jurisdiction & Consent Engine Component
- Audit & Traceability Logger Component
- Notification Dispatcher Component
- Timezone & Localization Engine Component

## Relationships
- Patients/Clinicians -> API Gateway: Client requests [HTTPS / WSS]
- API Gateway -> Core Telehealth Service: Internal routing [gRPC over mTLS]
- Core Telehealth Service -> E-Prescription Integration Service: Coordinates prescriptions [gRPC over mTLS]
- Core Telehealth Service -> AI Symptom Checker Service: Requests symptom analysis [gRPC over mTLS]
- Appointment Orchestrator -> Jurisdiction & Consent Engine: Validates rules [In-memory / gRPC]
- Appointment Orchestrator -> Notification Dispatcher: Triggers fallback alerts [gRPC / Cloud Pub/Sub]
- Appointment Orchestrator -> Timezone & Localization Engine: Resolves schedules [In-memory Go package call]

## Technology Stack
- Go: Used for Core Telehealth Service internal components for high concurrency and low latency.
- Temporal SDK: Powers Appointment Orchestrator for resilient, long-running workflow state management over unstable networks.
- Google Kubernetes Engine (GKE): Regional clusters deployed in `europe-west3` and `us-central1` for container orchestration.
- ArgoCD: Enforces GitOps deployment pipelines and configuration parity across regions.
- Istio Service Mesh: Manages traffic shaping, security, and fault injection for degraded network conditions.
- Cloud KMS & GCP Secret Manager: Handles regional encryption keys and runtime secret injection for data residency compliance.
- OpenTelemetry & Prometheus: Provides distributed tracing and SLI/SLO observability.

## Rationale
This architecture uses regional isolation on GCP with identical GKE clusters to satisfy strict GDPR and HIPAA data residency constraints. Temporal workflows and Istio service mesh ensure high availability and graceful degradation for patients with unstable rural internet connections.