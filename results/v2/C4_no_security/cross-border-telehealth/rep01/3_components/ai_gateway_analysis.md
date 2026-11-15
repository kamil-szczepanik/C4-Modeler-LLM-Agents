## Overview
The Cross-Border Telehealth Platform provides video consultations, e-prescriptions, and an AI symptom checker for patients across the EU and US. It ensures strict data residency, regulatory compliance, and high availability for unstable rural connections.

## Key Elements
- Patients (EU and US) and Licensed Clinicians
- API Gateway / Region Router (Cloud Endpoints, Envoy)
- AI Gateway Container (GKE, Node.js, Go, Python)
  - Policy & Data Residency Interceptor (Go)
  - Audit & Version Logger (Go)
  - Throttling & Fallback Proxy (Go)
  - Triage Explanation Formatter (Go)
- External AI Symptom Checker Engine
- Data Layer (Cloud SQL PostgreSQL, Firestore, Cloud Storage)

## Relationships
- API Gateway / Region Router -> Policy & Data Residency Interceptor: Forwards raw symptom payload [gRPC over internal VPC]
- Throttling & Fallback Proxy -> AI Symptom Checker Engine: Proxies sanitized requests [mTLS]
- Throttling & Fallback Proxy -> Triage Explanation Formatter: Passes raw upstream AI responses [In-memory Go structs]
- Triage Explanation Formatter -> Audit & Version Logger: Sends structured metadata and summaries [gRPC]
- Audit & Version Logger -> Data Layer: Persists compliance logs [gRPC/SQL]
- Triage Explanation Formatter -> API Gateway / Region Router: Returns finalized recommendations [gRPC]

## Technology Stack
- Google Cloud Platform (GCP): Primary cloud provider using regions `europe-west3` and `us-central1` for data residency.
- Go: Used for high-throughput concurrency within the AI Gateway components.
- Google Kubernetes Engine (GKE): Container orchestration with KEDA autoscaling and Istio service mesh network policies.
- OpenTelemetry: Used for tracking p99 latency and upstream AI engine error rates.

## Rationale
This architecture guarantees strict regional data separation required by GDPR and HIPAA by utilizing GCP regional deployments and Istio egress controls. The decoupled AI Gateway components ensure traceability, fault tolerance, and low latency for users with unstable rural internet connections.