## Overview
The Cross-Border Telehealth Platform provides video consultations, e-prescriptions, and an AI symptom checker for patients across the EU and the US. The architecture enforces strict regional data residency while ensuring offline resilience for rural users.

## Key Elements
- Patients (EU & US) and Licensed Clinicians
- Web & Mobile Client Containers (Flutter / React Native with offline-first caching)
- API Gateway (Cloud Endpoints / Apigee)
- Core Telehealth Backend (GKE microservices in `europe-west3` and `us-central1`)
- Transaction Ingestion Component (Go / gRPC)
- Resilient Sync Orchestrator (Go / Temporal on GKE)
- Session & State Manager (Go / Redis Memorystore)
- Clinical Exception & Audit Notifier (Go / GCP Pub/Sub)
- Cloud SQL (PostgreSQL) and Cloud Storage with Cloud KMS (CMEK)

## Relationships
- Web & Mobile Clients -> API Gateway: Routes requests via HTTPS and mTLS with JWTs
- API Gateway -> Core Telehealth Backend: Forwards authenticated traffic via gRPC over mTLS
- Transaction Ingestion Component -> Resilient Sync Orchestrator: Passes idempotency-keyed payloads securely
- Resilient Sync Orchestrator -> Clinical Exception & Audit Notifier: Dispatches failure events via GCP Pub/Sub regional topics

## Technology Stack
- Google Cloud Platform (GCP): Target cloud provider for regional isolation in `europe-west3` and `us-central1`
- Kubernetes (GKE): Container orchestration for backend services with regional node pools
- Go: Primary language for Core Telehealth Backend components ensuring high performance
- Temporal: Workflow engine managing offline-resilient transactions
- Redis (Memorystore): Real-time session and state management
- GCP Pub/Sub: Asynchronous regional event distribution

## Rationale
This architecture guarantees strict regulatory compliance (GDPR and HIPAA) by isolating data processing and storage within designated regional boundaries. Furthermore, the offline-resilient components ensure continuous service availability and transaction integrity for users in rural areas with unstable internet connections.