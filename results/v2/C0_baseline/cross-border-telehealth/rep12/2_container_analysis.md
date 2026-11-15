## Overview
A cross-border telehealth platform providing video consultations, e-prescriptions, and an AI symptom checker for EU and US patients. It enforces strict regional data residency while ensuring low-bandwidth resilience and regulatory compliance.

## Key Elements
- **Clients:** Web/Mobile Client Applications (Flutter/React Native)
- **Edge:** Cloud Load Balancing (API Gateway with OAuth2/OIDC, TLS 1.3)
- **Containers (GKE & Cloud Run):** Video Consultation (LiveKit SFU), AI Symptom Checker (Python/FastAPI), Consent Management (Spring Boot), Patient Onboarding & Identity, Billing & Regional Monetization, Core Telehealth & E-Prescription (Spring Boot), Notification & Messaging (Node.js)
- **Messaging & Storage:** Cloud Pub/Sub, Cloud Logging, BigQuery, Google Cloud KMS (CMEK), Google Secret Manager
- **External Systems:** EU National E-Prescription Gateways, US Pharmacy Networks, External IdPs, Regional Payment Gateways

## Relationships
- **Clients to API Gateway:** HTTPS and WebSockets (WSS) for external client-to-gateway traffic
- **Internal Microservices:** gRPC over mTLS (Istio service mesh) for low-latency service-to-service communication
- **Core Telehealth to External:** REST and HL7 FHIR for US Pharmacy Networks and EU National E-Prescription Gateways
- **Notification to Clients:** Regional Cloud Pub/Sub buffering asynchronous push alerts and SMS notifications

## Technology Stack
- **Cloud Provider:** Google Cloud Platform (GCP) across `europe-west3` and `us-central1` regions for strict data residency
- **Compute:** Google Kubernetes Engine (GKE) for stateful/core services and Cloud Run for serverless scaling (AI Symptom Checker, Notifications)
- **Real-Time Video:** LiveKit WebRTC SFU on GKE with dynamic codec step-down for low-bandwidth resilience (<300 kbit/s)
- **Security & Compliance:** Google Cloud KMS (CMEK) for region-separated envelope encryption, Google Secret Manager, and Istio for mTLS

## Rationale
Regional container deployments in GCP (`europe-west3` and `us-central1`) strictly enforce GDPR and HIPAA data residency requirements. Decoupled microservices with gRPC/mTLS, regional Pub/Sub buffering, and WebRTC SFU optimization ensure fault tolerance, audit traceability, and stable video delivery for rural users.