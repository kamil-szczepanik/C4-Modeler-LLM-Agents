## Overview
The Cross-Border Telehealth Platform provides secure video consultations, e-prescriptions, and an AI symptom checker for patients across the EU and US. It ensures strict regional data residency and granular purpose-based consent management.

## Key Elements
- Patients (EU & US) and Licensed Clinicians
- Client Applications: Patient Mobile/Web App (Flutter/React), Clinician Portal (React)
- Edge & Routing: API Gateway (Envoy/Kong), LiveKit/WebRTC Media Relays (TURN/SRTP/DTLS)
- Core Services on GKE (Python/Go): Core Telehealth Service, Interoperability & E-Prescription Adapter, Consent & Privacy Management Container, AI Orchestrator & Audit Service
- Consent Components: Consent API Controller, Policy Decision Engine (OPA), Cryptographic Token Service, Audit & Ledger Logger, Revocation Publisher
- External Systems: EU National E-Prescription Gateways, US Pharmacy Networks, AI Inference Service
- Data & Security: Regional Data Storage (Cloud SQL PostgreSQL, Cloud Spanner, Redis Memorystore), Cloud KMS

## Relationships
- Patient/Clinician Apps -> API Gateway: Routes requests via HTTPS / WebSocket / Server-Sent Events (SSE)
- API Gateway -> Consent & Privacy Management Container: Routes consent and privacy calls via gRPC / mTLS (Istio Mesh)
- Consent & Privacy Management Container -> Regional Data Storage: Manages consent records, keys, and Redis Pub/Sub via SQL / Cloud KMS / mTLS
- Core Telehealth Service -> LiveKit/WebRTC Media Relays: Establishes video streams via TURN / SRTP / DTLS

## Technology Stack
- Google Cloud Platform (GCP): Deployment targeted to `europe-west3` and `us-central1` for localized data residency compliance.
- Google Kubernetes Engine (GKE): Orchestrates containerized Python and Go microservices.
- Open Policy Agent (OPA): Evaluates real-time access requests against stored consent rules for low-latency decisioning.
- Cloud KMS & Redis Memorystore: Secures regional JWT token signing, KMS rotation, replay prevention, and regional pub/sub event streaming.
- Istio Service Mesh: Enforces strict zero-trust mTLS across all microservice boundaries.

## Rationale
This architecture enforces strict regional data isolation via separate GKE namespaces and Cloud SQL instances in EU and US regions to satisfy GDPR and HIPAA mandates. Granular, cryptographically signed consent tokens combined with OPA and real-time SSE revocation ensure secure, compliant cross-border access.