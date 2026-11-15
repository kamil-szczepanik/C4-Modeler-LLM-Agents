## Overview
The Cross-Border Telehealth Platform provides secure video consultations, e-prescriptions, and AI-driven symptom checking for patients across the EU and US. It ensures strict data residency, regulatory compliance, and high availability over unstable connections.

## Key Elements
* Patients and Licensed Clinicians (Users)
* Flutter Patient Mobile/Web App and Clinician Portal (Containers)
* GCP API Gateway, Core Telehealth Service (Go/Gin), and AI Inference Wrapper (Python/FastAPI) (Containers)
* Consent & Profile Management Service and Pharmacy Integration Gateway (Containers)
* GCP GKE Regional Clusters (`europe-west3`, `us-central1`), Cloud SQL PostgreSQL, and GCP Cloud Pub/Sub (Infrastructure)

## Relationships
* GCP API Gateway -> Core Telehealth Service: Routes API requests [gRPC]
* Core Telehealth Service -> AI Inference Wrapper: Sends symptom-check requests with audit logging [gRPC]
* Core Telehealth Service -> Pharmacy Integration Gateway: Dispatches prescriptions asynchronously [GCP Pub/Sub]
* Core Telehealth Service -> Cloud SQL PostgreSQL: Persists session state and telemetry [TLS]

## Technology Stack
* Go / Gin: Selected for the Core Telehealth Service for high performance and low memory footprint.
* Python / FastAPI: Powers the AI Inference Wrapper for rapid machine learning integration.
* GCP GKE: Orchestrates containerized workloads across isolated regional clusters.
* Cloud SQL PostgreSQL: Stores region-pinned health data to satisfy HIPAA and GDPR residency constraints.
* GCP Pub/Sub: Decouples asynchronous pharmacy integration to ensure transactional reliability.

## Rationale
This architecture enforces strict regional data isolation to comply with GDPR and HIPAA mandates while decoupling control and media planes for rural network resilience. It ensures full auditability and traceability for AI medical device outputs.