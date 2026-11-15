## Overview
The Cross-Border Telehealth Platform provides video consultations, e-prescriptions, and an AI symptom checker for EU and US patients. It ensures strict data residency, privacy compliance, and MDR traceability via regional deployments on GCP.

## Key Elements
* **Clients**: React Web Application & React Native Mobile App
* **Entry Point**: GCP Cloud Endpoints / Envoy API Gateway
* **Core Containers**: Core Services Container (Node.js/NestJS), AI Symptom Checker Container (Python/FastAPI), Video Media Server (LiveKit/WebRTC SFU)
* **Data Tier**: Cloud SQL (PostgreSQL with PgBouncer), BigQuery
* **Infrastructure & Security**: GCP Anthos Service Mesh (Istio), GCP Secret Manager, Artifact Registry

## Relationships
* **Client to API Gateway**: HTTPS (JSON/REST) for metadata and consent; WSS (WebSockets/QUIC) for video media.
* **API Gateway to Core & AI Containers**: gRPC over mTLS secured via GCP Anthos Service Mesh.
* **Core Services to Database**: SSL/TLS-encrypted PostgreSQL connections via PgBouncer.
* **AI Container to Audit Logs**: Decoupled, pseudonymized audit payloads emitted to BigQuery.

## Technology Stack
* **Cloud Infrastructure**: GCP regions `europe-west3` and `us-central1` for geographic data residency.
* **Backend Services**: Node.js/NestJS for core logic; Python/FastAPI for AI inference.
* **Video/Communication**: LiveKit WebRTC SFU optimized for low-bandwidth connections (<300 kbit/s).
* **Databases**: Cloud SQL (PostgreSQL) for transactional data using FHIR/national schemas; BigQuery for immutable audit logs.
* **Security & Ops**: GCP Secret Manager, Anthos Service Mesh (mTLS), ArgoCD for GitOps, Prometheus/Grafana.

## Rationale
The regional container isolation in `europe-west3` and `us-central1` strictly enforces GDPR and HIPAA data residency constraints. Decoupled gRPC microservices with strict mTLS, pseudonymized BigQuery logging, and WebRTC optimizations ensure MDR traceability and reliable service in rural areas.