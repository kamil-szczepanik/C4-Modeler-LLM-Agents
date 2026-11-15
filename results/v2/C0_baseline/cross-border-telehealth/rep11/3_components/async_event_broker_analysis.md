## Overview
The Cross-Border Telehealth Platform provides secure video consultations, e-prescriptions, and an AI symptom checker for patients across the EU and US. The system enforces strict regional data residency and compliance using GCP services.

## Key Elements
- Patients (EU and US) and Licensed Clinicians
- External Pharmacies, Regional Payment Gateways, Health Authorities, Identity Providers
- Web App & Mobile App (React / Flutter)
- API Gateway (Cloud Endpoints / Envoy)
- Identity & Access Management / Consent Service (OAuth2 / OIDC / Google Secret Manager)
- Core Services Container (Spring Boot / Java)
- AI Symptom Checker Container (Python / FastAPI / PyTorch / MLflow)
- SFU Video Container (LiveKit / Janus)
- Async Event Broker Container (Google Cloud Pub/Sub) with Ingest Router, Regional Topic Manager, and DLQ Manager
- Data Storage (Cloud SQL PostgreSQL / Cloud Storage / CMEK)

## Relationships
- Patients / Clinicians -> API Gateway: Accesses platform features [HTTPS / WSS]
- API Gateway -> Core Services Container: Routes validated requests [gRPC]
- Core Services Container -> Ingest Router: Publishes domain events [gRPC with mTLS]
- Ingest Router -> Regional Topic Manager: Routes validated payloads [Internal GCP Pub/Sub API]
- Regional Topic Manager -> Core Services Container: Dispatches downstream tasks [gRPC push subscriptions]
- Regional Topic Manager -> DLQ Manager: Offloads poison-pill messages [Pub/Sub subscription rules]

## Technology Stack
- Google Cloud Platform (GCP): Target cloud providing regional infrastructure in `europe-west3` and `us-central1`.
- Google Cloud Pub/Sub: Asynchronous messaging backbone with regional topics and CMEK for data residency.
- Spring Boot / Java & Spring Cloud Stream: Core application framework and event streaming logic.
- Cloud KMS & Client-Side Encryption: Ensures envelope encryption and zero-knowledge storage for PHI/PII.
- W3C Trace Context: Mandates distributed tracing across async boundaries for traceability.

## Rationale
The architecture ensures strict GDPR and HIPAA compliance by isolating EU and US health data regionally using GCP services and CMEK encryption. Asynchronous event brokering with robust DLQ management guarantees service availability and traceability for patients with unstable internet connections.