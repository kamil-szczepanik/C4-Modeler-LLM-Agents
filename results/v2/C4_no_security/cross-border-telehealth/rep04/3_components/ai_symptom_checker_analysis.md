## Overview
The Cross-Border Telehealth Platform provides video consultations, e-prescriptions, and an AI symptom checker for EU and US patients. It enforces regional data residency and regulatory compliance under GDPR, HIPAA, and EU MDR.

## Key Elements
*   Triage Orchestrator Service (Go)
*   Inference Execution Engine (Python / PyTorch)
*   Localization & Normalization Component (Python)
*   Clinical Handoff Router (Go)
*   Audit Logging & Versioning Interceptor (Go)
*   GKE Regional Clusters (`europe-west3`, `us-central1`)
*   Cloud SQL PostgreSQL & Cloud Storage
*   API Gateway with Envoy Sidecar

## Relationships
*   API Gateway -> Triage Orchestrator Service via gRPC
*   Triage Orchestrator -> Localization Component via gRPC
*   Localization Component -> Inference Execution Engine via gRPC
*   Triage Orchestrator -> Clinical Handoff Router via Go internal function call
*   Triage Orchestrator -> Cloud SQL PostgreSQL for transactional dual-write logging via SQL/TCP
*   Triage Orchestrator -> Cloud Storage for model version logging via HTTPS

## Technology Stack
*   Go: Used for microservices requiring high concurrency and low latency (Triage Orchestrator, Clinical Handoff Router).
*   Python / PyTorch / FastAPI: Powers medical NLP models and inference execution.
*   Google Kubernetes Engine (GKE): Deploys containerized services with GPU node pools and Knative.
*   Cloud SQL PostgreSQL: Enforces regional relational data storage and transactional audit logging.
*   gRPC: Enables high-performance, low-latency internal service communication.

## Rationale
This architecture decouples AI inference from orchestration to meet strict EU MDR traceability and latency requirements. Regional GKE clusters and transactional dual-writes ensure strict HIPAA and GDPR compliance without compromising performance for low-bandwidth users.