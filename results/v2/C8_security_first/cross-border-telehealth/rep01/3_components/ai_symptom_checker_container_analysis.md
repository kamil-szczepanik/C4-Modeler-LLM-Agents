## Overview
- **System:** Cross-Border Telehealth Platform providing video consultations, e-prescriptions, and an AI symptom checker across the EU and US.
- **Purpose:** Deliver compliant, region-restricted telemedicine services with rigorous traceability, resilience, and privacy controls.

## Key Elements
- **Users:** Patients, Clinicians, and Compliance Officers.
- **External Systems:** National E-Prescription Gateways (EU), US Pharmacy Networks, and Identity Providers (IdP).
- **Core Containers:** API Gateway / Ingress (Envoy / GCP HTTPS Load Balancer), Video Consultation Service (Mediasoup WebRTC SFU), AI Symptom Checker Container, E-Prescription Integration Container, Patient Consent & Profile Container, and Data Tier (Cloud SQL PostgreSQL, Memorystore with CMEK).
- **AI Symptom Checker Internal Components:** Resilience & Fallback Middleware, Inference API Router (FastAPI), Clinical NLP & Preprocessing Engine, PyTorch Inference Core & Explainability Module, and Asynchronous Event Publisher.
- **Infrastructure & Observability:** Google Cloud Pub/Sub, OpenTelemetry, Cloud Audit Logs, and Google Kubernetes Engine (GKE) with KEDA.

## Relationships
- **API Gateway / Ingress -> AI Symptom Checker Container:** Routes inference requests via gRPC over mTLS.
- **AI Symptom Checker Container -> Google Cloud Pub/Sub:** Publishes asynchronous, guaranteed-delivery immutable audit logs.
- **AI Symptom Checker Container -> Data Tier:** Persists encrypted regional data via SQL with CMEK over internal GCP network.
- **GKE Node Pools -> AI Symptom Checker Container:** Manages isolated GPU/CPU execution within regional clusters (`europe-west3` and `us-central1`).

## Technology Stack
- **Compute & Orchestration:** Google Kubernetes Engine (GKE) with NVIDIA T4 GPU node pools for isolated PyTorch execution.
- **Backend & AI Framework:** Python with FastAPI and PyTorch for the inference engine.
- **Security & Identity:** SPIFFE/SPIRE via Anthos Service Mesh for mTLS, Cosign for container image signing, and CMEK for database encryption.
- **Messaging & Observability:** Google Cloud Pub/Sub for asynchronous logging and OpenTelemetry with Cloud Monitoring for metrics.

## Rationale
- Enforces strict data residency (EU/US) and compliance (GDPR, HIPAA, EU MDR) using regional GKE clusters, CMEK, and verifiable audit logging.
- Guarantees high availability and low latency for rural users with unstable connections through asynchronous Pub/Sub logging, circuit-breaking middleware, and graceful fallback responses.