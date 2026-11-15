## Overview
The Cross-Border Telehealth Platform provides secure video consultations, e-prescriptions, and an AI symptom checker for patients in the EU and US. The system enforces strict regional data residency and regulatory compliance under GDPR and HIPAA.

## Key Elements
- **Users**: Patients, Clinicians, Compliance Officer.
- **External Systems**: National E-Prescription Gateways (EU), US Pharmacy Networks, Identity Providers (IdP).
- **API Gateway / Ingress**: Envoy / GCP HTTPS Load Balancer deployed in `europe-west3` and `us-central1`.
- **Video Consultation Service**: Mediasoup WebRTC SFU containers.
- **AI Symptom Checker Container**: Python/FastAPI and PyTorch inference engine.
- **E-Prescription Integration Container**: Node.js and FHIR protocol adapters.
- **Patient Consent & Profile Container**: Go-based microservice for consent management (R-04).
- **Data Tier**: Region-locked Cloud SQL PostgreSQL and Memorystore with CMEK.
- **Messaging & Observability**: Google Cloud Pub/Sub and OpenTelemetry.

## Relationships
- **Patients/Clinicians to API Gateway**: HTTPS / TLS 1.3, OAuth 2.0 / OIDC, FIDO2/WebAuthn.
- **API Gateway to Internal Containers**: gRPC over mTLS.
- **Internal Containers to Data Tier**: SQL with CMEK over internal GCP network.
- **E-Prescription Container to External Gateways**: Outbound mTLS with pinned IPs and client certificates.
- **Consent Container to Downstream Services**: Google Cloud Pub/Sub for event-driven revocation.

## Technology Stack
- **Cloud Provider**: GCP (`europe-west3` for EU, `us-central1` for US) to enforce regional isolation.
- **Orchestration & Security**: GKE with Binary Authorization and Artifact Registry.
- **Networking**: Envoy / GCP HTTPS Load Balancer with mTLS (TLS 1.3).
- **Backend Languages**: Go (Consent Service), Node.js (E-Prescription), Python/FastAPI + PyTorch (AI).
- **Streaming**: Mediasoup WebRTC SFU for adaptive bitrate video.
- **Messaging & Audit**: Google Cloud Pub/Sub, OpenTelemetry, and Cloud Audit Logs with retention locks.

## Rationale
Regional isolation on GCP with dedicated API gateways guarantees that EU and US health data never cross borders without explicit consent, satisfying GDPR and HIPAA constraints. Event-driven consent propagation via Pub/Sub and lightweight Go microservices ensure sub-second authorization checks and resilient degraded-mode video streaming for rural users.