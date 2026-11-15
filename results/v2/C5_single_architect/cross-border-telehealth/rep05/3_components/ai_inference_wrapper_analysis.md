## Overview
The Cross-Border Telehealth Platform provides video consultations, e-prescriptions, and an AI symptom checker for patients in the EU and US. It ensures strict regulatory compliance, data residency, and traceability for medical AI outputs.

## Key Elements
- Patients (EU/US) and Clinicians (Users)
- API Gateway & Routing Layer (Google Cloud Load Balancing, Apigee)
- Core Telehealth Service (Go on GKE)
- Video Media Server (WebRTC SFU on GKE)
- AI Inference Wrapper (Python on Vertex AI container)
  - Inference Controller (FastAPI)
  - Regional Data Sanitizer (Python/Pandas)
  - Model Execution Engine (PyTorch/Vertex AI SDK)
  - Audit & Logging Interceptor (Python middleware)
- Integration Service (Go / Camel-K on GKE)
- Audit & Traceability Ledger (Cloud Pub/Sub, BigQuery)
- Datastores (Cloud SQL PostgreSQL)
- External Systems: AI Model Registry, EU National E-Prescription Gateways, US Surescripts

## Relationships
- Patients/Clinicians -> API Gateway & Routing Layer [HTTPS, WebRTC]
- API Gateway -> AI Inference Wrapper (Inference Controller) [gRPC / HTTP]
- Inference Controller -> Regional Data Sanitizer [In-memory Python call]
- Regional Data Sanitizer -> Model Execution Engine [In-memory Python call]
- Inference Controller -> Audit & Logging Interceptor [Async queue]
- Audit & Logging Interceptor -> Audit & Traceability Ledger [Cloud Pub/Sub, gRPC]
- Model Execution Engine -> AI Model Registry [gRPC / REST]
- Integration Service -> EU National E-Prescription Gateways / US Surescripts [REST, HL7 FHIR]

## Technology Stack
- Google Cloud Platform (GCP): Target cloud provider across `europe-west3` and `us-central1` regions for data residency enforcement.
- Google Kubernetes Engine (GKE): Container orchestration for core services and WebRTC media servers.
- Python & FastAPI / PyTorch / Vertex AI: Powers the AI Inference Wrapper and symptom-checker execution.
- Go: Used for high-throughput Core Telehealth and Integration services.
- Cloud Pub/Sub & BigQuery: Implements asynchronous audit logging and traceability tracking.
- Cloud SQL PostgreSQL: Regional relational data storage.

## Rationale
This architecture enforces regional data isolation between `europe-west3` and `us-central1` to satisfy GDPR and HIPAA mandates. The internal AI component decomposition guarantees EU MDR traceability via dedicated logging interceptors while maintaining high availability and low latency for cross-border telemedicine users.