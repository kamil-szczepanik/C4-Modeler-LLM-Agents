## Overview
The Cross-Border Telehealth Platform provides video consultations, e-prescriptions, and an AI symptom checker for EU and US patients. It ensures strict regional data residency, regulatory compliance, and resilience for unstable network connections.

## Key Elements
- **Users**: Patients, Licensed Clinicians, Support Staff, Compliance/Legal Officers
- **External Systems**: Local Pharmacy Networks, National Health Authorities
- **Containers**: Multi-region Web/Mobile Clients, Edge Routing & WebRTC SFU Containers (TLS 1.3), API Gateway (Istio Service Mesh with mTLS), E-Prescription Routing Container (GCP Pub/Sub), AI Symptom Checker Container (AI/ML Runtime), Consent Management Service (OAuth 2.0 / OIDC)

## Relationships
- Multi-region Web/Mobile Clients -> API Gateway: Sends HTTPS/WebSockets requests [TLS 1.3]
- API Gateway -> AI Symptom Checker Container: Forwards symptom analysis requests [mTLS]
- AI Symptom Checker Container -> GCP BigQuery: Streams immutable audit logs and feedback [Secure GCP VPC]
- AI Symptom Checker Container -> Regional Redis Cache: Stores session state for offline resilience [AES-256]

## Technology Stack
- **Cloud Provider**: Google Cloud Platform (GCP) across `europe-west3` and `us-central1` regions for strict data residency.
- **Orchestration**: Google Kubernetes Engine (GKE) with regional clusters and Istio Service Mesh for zero-trust mTLS.
- **AI/ML Runtime**: Containerized ML runtime with Redis for caching and Fluentbit for log streaming.
- **Data & Logging**: GCP BigQuery for audit logging, GCP Pub/Sub for asynchronous feedback ingestion.
- **Security**: Cosign for container image signing, OAuth 2.0 / OIDC for authorization.

## Rationale
This architecture guarantees GDPR and HIPAA compliance by isolating regional data workloads in GCP. Additionally, it satisfies EU MDR traceability and rural connectivity constraints through robust audit logging, local caching, and resilient mesh routing.