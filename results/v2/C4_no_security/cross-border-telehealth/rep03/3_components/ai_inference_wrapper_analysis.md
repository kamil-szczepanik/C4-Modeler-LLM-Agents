## Overview
The Cross-Border Telehealth Platform provides video consultations, e-prescriptions, and an AI symptom checker for patients in the EU and US. It enforces regional data residency, HIPAA/GDPR compliance, and EU MDR traceability using GCP infrastructure.

## Key Elements
- Patients & Licensed Clinicians
- Flutter Patient Mobile/Web App & Clinician Portal
- GCP API Gateway (Cloud Endpoints / Envoy)
- Core Telehealth Service (Go / Spring Boot)
- AI Inference Wrapper (Python / FastAPI)
- Consent & Profile Management Service
- Pharmacy Integration Gateway
- GCP GKE Regional Clusters (`europe-west3`, `us-central1`)
- Cloud SQL PostgreSQL Databases
- GCP Cloud Pub/Sub

## Relationships
- Patients/Clinicians -> GCP API Gateway via HTTPS/WSS
- GCP API Gateway -> Core Telehealth Service via gRPC
- Core Telehealth Service -> AI Inference Wrapper via gRPC
- AI Inference Wrapper -> GCP Cloud Pub/Sub via gRPC
- AI Inference Wrapper -> Regional AI Endpoints via gRPC/HTTPS

## Technology Stack
- GCP GKE (`europe-west3`, `us-central1`): Regional container orchestration for data residency
- Python / FastAPI: Lightweight, high-performance runtime for AI inference wrapping
- GCP Cloud Pub/Sub: Asynchronous messaging for decoupled, non-blocking audit logging
- Cloud SQL PostgreSQL: Relational storage for regional transactional data
- Istio Service Mesh: Network control for strict egress locking and data isolation

## Rationale
This architecture guarantees strict regional data residency by deploying isolated GKE clusters in Europe and the US. Decoupling audit logging via Pub/Sub ensures high availability for rural users on unstable connections.