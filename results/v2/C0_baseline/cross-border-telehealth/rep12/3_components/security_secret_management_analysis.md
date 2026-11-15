## Overview
A cross-border telehealth platform providing video consultations, e-prescriptions, and AI symptom checking for patients in the EU and US. It ensures strict data residency, regulatory compliance (GDPR/HIPAA/MDR), and resilience over unstable connections.

## Key Elements
- **Users**: Patients, Licensed Clinicians, Pharmacies, Compliance Officers
- **External Systems**: EU National E-Prescription Gateways, US Pharmacy Networks, External Identity Providers, Regional Payment Gateways
- **Containers**: Web/Mobile Client (Flutter/React Native), API Gateway (OAuth2/OIDC, TLS 1.3), Video Consultation Service (LiveKit WebRTC SFU on GKE), AI Symptom Checker (Python/FastAPI on Cloud Run), Consent Management Service, Core Telehealth & E-Prescription (Spring Boot on GKE), Security & Secret Management
- **Security Components**: Regional KMS Adapter (Cloud KMS with CMEK), Secret Management Service (Google Secret Manager), Audit & Compliance Logger (Cloud Audit Logs), Ephemeral Credential Broker & Circuit Breaker Sidecar

## Relationships
- **Client Applications -> API Gateway**: HTTPS / TLS 1.3, OAuth2/OIDC
- **Video Consultation Service -> LiveKit WebRTC SFU**: WebRTC / DTLS/SRTP
- **Core Telehealth Services -> Ephemeral Credential Broker**: Local gRPC via mTLS (SPIFFE/SPIRE)
- **Ephemeral Credential Broker -> Regional KMS Adapter & Secret Manager**: HTTPS / gRPC with Workload Identity
- **Audit & Compliance Logger -> Google BigQuery**: Cloud Pub/Sub / Streaming Inserts

## Technology Stack
- **Cloud Provider**: Google Cloud Platform (GCP regions: `europe-west3`, `us-central1`) for regional data isolation
- **Orchestration**: Google Kubernetes Engine (GKE) and Cloud Run for containerized microservices
- **Security & Encryption**: Google Cloud KMS (CMEK), Google Secret Manager, SPIFFE/SPIRE for mTLS, AES-GCM-256 for local caching
- **Observability**: Cloud Monitoring, Prometheus metrics, Cloud Audit Logs for compliance

## Rationale
This architecture uses GCP multi-region deployments with regional key pinning to satisfy strict EU/US data residency mandates. Edge-cached credentials, circuit breakers, and WebRTC ensure high availability and low-bandwidth resilience for rural clinical workflows.