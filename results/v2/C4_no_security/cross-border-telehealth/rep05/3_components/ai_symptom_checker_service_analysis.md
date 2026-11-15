## Overview
A cross-border telehealth platform providing video consultations, e-prescriptions, and an AI symptom checker for patients in the EU and US. It guarantees regional data residency, HIPAA/GDPR compliance, and EU MDR traceability.

## Key Elements
- Patients and Licensed Clinicians (Users)
- API Gateway / BFF (Envoy / Cloud Endpoints)
- AI Symptom Checker Service Container (Python / FastAPI)
- Triage Orchestrator (Internal Component)
- Inference Adapter (Python / LangChain / PyTorch)
- Audit & Traceability Logger (Python Component)
- Compliance Exporter (Python Background Worker)
- Regional Relational Database (Google Cloud SQL PostgreSQL)
- Google Kubernetes Engine (GKE) Autopilot Clusters (`europe-west3`, `us-central1`)

## Relationships
- API Gateway / BFF -> Triage Orchestrator: Forwards symptom analysis requests [gRPC / REST]
- Triage Orchestrator -> Inference Adapter: Requests urgency calculation [In-process async / gRPC]
- Triage Orchestrator -> Audit & Traceability Logger: Dispatches payload snapshots [Cloud Pub/Sub Lite]
- Audit & Traceability Logger -> Regional Relational Database: Writes immutable records [SQL / TLS]
- Compliance Exporter -> Regional Relational Database: Aggregates logs for compliance reports [SQL / TLS]

## Technology Stack
- Google Cloud Platform (GCP): Target cloud provider for regional isolation in `europe-west3` and `us-central1`.
- Python / FastAPI / LangChain / PyTorch: Powers the stateless AI symptom checker and inference runtime.
- Google Cloud SQL PostgreSQL: Stores regional transactional data and immutable audit logs with WORM policies.
- Istio Service Mesh & OpenTelemetry: Handles circuit breaking, service communication, latency tracking, and monitoring.

## Rationale
Stateless microservices deployed across isolated GCP regions enforce strict EU and US data residency and privacy mandates. Asynchronous logging and dedicated compliance exporters guarantee EU MDR traceability without sacrificing runtime performance for rural users.