## Overview
[A cross-border telehealth platform providing video consultations, e-prescriptions, and an AI symptom checker for patients in the EU and US. Core purpose is delivering secure, compliant telemedicine services across international jurisdictions with strict data residency.]

## Key Elements
*   Patients (EU and US)
*   Licensed Clinicians
*   Platform Administrators / Compliance Officers
*   Web App & Mobile App (React / Flutter)
*   API Gateway (Cloud Endpoints / Envoy)
*   Identity & Access Management (IAM) / Consent Service
*   Core Services Container (Spring Boot / Java)
*   AI Symptom Checker Container (Python / FastAPI / PyTorch with MLflow)
*   SFU Video Container (LiveKit / Janus)
*   Async Event Broker (Google Cloud Pub/Sub)
*   Data Storage (Cloud SQL PostgreSQL, Cloud Storage)
*   External Pharmacies, Regional Payment Gateways, Health Authorities & Auditors, Identity Providers

## Relationships
*   Patients / Clinicians to Web App & Mobile App via HTTPS/JSON and WebRTC (Video)
*   Web App / Mobile App to API Gateway via HTTPS/TLS 1.3
*   API Gateway to Core Services, AI Symptom Checker, and Consent Service via gRPC with mTLS (Istio/Anthos)
*   Core Services to Async Event Broker via AMQP/Pub/Sub protocols
*   Core Services to Data Storage via secure database connections with CMEK encryption
*   Async Event Broker to External Pharmacies via encrypted HTTPS

## Technology Stack
*   Cloud Provider: Google Cloud Platform (GCP) across `europe-west3` and `us-central1` for regional data isolation
*   Orchestration & Mesh: Google Kubernetes Engine (GKE) with Istio/Anthos service mesh for zero-trust mTLS
*   Backend Services: Spring Boot (Java) for core logic; Python (FastAPI/PyTorch) with MLflow for AI traceability
*   Frontend: React and Flutter for cross-platform support with degraded video handling (<300 kbit/s)
*   Real-Time & Messaging: LiveKit or Janus SFU for video; Google Cloud Pub/Sub with Dead Letter Queues for async events
*   Security & Compliance: Cloud KMS with CMEK, Google Secret Manager, and OpenTelemetry for immutable audit logs

## Rationale
[This architecture enforces strict regional data residency on GCP to comply with GDPR, HIPAA, and EU MDR mandates. Resilient video streaming and async messaging ensure high availability for rural users and unstable connections.]