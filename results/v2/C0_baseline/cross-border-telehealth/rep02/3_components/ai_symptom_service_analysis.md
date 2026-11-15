## Overview
The Cross-Border Telehealth Platform provides video consultations, e-prescriptions, and an AI symptom checker for patients in the EU and US. It ensures strict data residency, regulatory compliance, and high availability across unstable internet connections.

## Key Elements
- Patients (EU & US) and Licensed Clinicians
- Pharmacy Partners (EU & US) and Third-Party WebRTC SFU
- API Gateway (Envoy / Cloud Endpoints)
- AI Symptom Service container (Python / FastAPI) running on GKE (`europe-west3`, `us-central1`)
- Triage Orchestrator Component, Inference Adapter, Explanation Generator, and De-identification Middleware
- Fluentbit sidecar container for asynchronous log shipping
- Google Cloud SQL (PostgreSQL) and GCP Cloud Storage WORM buckets

## Relationships
- Web / Mobile Client -> API Gateway: Routes requests via HTTPS / WSS
- API Gateway -> AI Symptom Service: Routes AI symptom check requests via gRPC over mTLS
- AI Symptom Service -> AI Model Registry / Inference Service: Executes symptom evaluation via gRPC
- AI Symptom Service -> Fluentbit sidecar: Offloads audit payloads via local ephemeral volumes with LUKS encryption
- Fluentbit sidecar -> Cloud Storage WORM buckets: Batch-writes immutable audit payloads via HTTPS / Cloud Storage API

## Technology Stack
- Google Cloud Platform (GCP): Target cloud provider ensuring regional isolation in `europe-west3` and `us-central1`
- Python / FastAPI: Core framework for the AI Symptom Service enabling low-latency execution
- Google Kubernetes Engine (GKE): Container orchestration with HPA and Argo Rollouts for canary deployments
- Fluentbit: Sidecar container for asynchronous log shipping and batch-writing to storage
- Google Cloud Storage WORM: Immutable storage with regional KMS-managed cryptographic keys for audit integrity
- Istio / Cilium: Service mesh enforcing strict mTLS across internal components

## Rationale
This architecture guarantees strict regional data residency and compliance with GDPR, HIPAA, and EU MDR through localized de-identification, cryptographic audit logging, and strict IAM policies. Decoupling the audit pipeline with sidecar Fluentbit buffering and implementing circuit breakers ensures high availability and graceful degradation for patients with unstable internet connections.