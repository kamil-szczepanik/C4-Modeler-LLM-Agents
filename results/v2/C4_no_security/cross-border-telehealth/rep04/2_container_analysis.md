## Overview
The Cross-Border Telehealth Platform provides secure video consultations, e-prescriptions, and an AI symptom checker for patients in the EU and US. The system enforces strict regional data residency while ensuring low-bandwidth resilience and regulatory compliance.

## Key Elements
- Patients (EU & US) and Licensed Clinicians (Users)
- Web/Mobile Client Containers (Flutter/React Native)
- API Gateway (Cloud Endpoints/Envoy)
- Core Telehealth Backend Container (Node.js/Go)
- AI Symptom Checker Container
- Consent Management Container
- Billing & Subscriptions Container (Go)
- Notification Container
- Video Media Server (Janus/WebRTC on GCE)
- TURN/STUN Relay Tier
- Databases (Cloud SQL PostgreSQL & Cloud Storage)
- External Systems: Pharmacies, Identity Providers (Auth0/GCP IAM), National e-Prescription Gateways, Stripe, Twilio, SendGrid

## Relationships
- Patients/Clinicians interact with Web/Mobile Clients via HTTPS and WebRTC (R-01, R-06).
- Clients communicate with regional API Gateways using mTLS and JWT validation.
- API Gateway routes internal traffic to Core Telehealth, Consent, AI Symptom Checker, Billing, and Notification containers via gRPC.
- Core Telehealth Backend communicates with EU/US national e-prescription gateways and pharmacies (R-02, R-08).
- Notification Container triggers Twilio and SendGrid APIs for SMS/Email/Push alerts.
- Billing Container integrates with Stripe API using regional keys.

## Technology Stack
- **Cloud Provider:** GCP (`europe-west3` and `us-central1`) for regional data isolation (R-05).
- **Orchestration:** GKE Enterprise (Anthos) with Anthos Service Mesh for zero-leakage traffic gating.
- **Frontend:** Flutter / React Native with local SQLite caching for offline-first rural resilience (R-06).
- **Backend Services:** Node.js / Go for stateless, highly performant microservices.
- **Data Persistence:** Cloud SQL PostgreSQL and Cloud Storage with region-locked CMEK encryption.
- **Video & Real-time:** Janus WebRTC on GCE with regional TURN/STUN relays and adaptive bitrate control.
- **Messaging & Secrets:** GCP Pub/Sub (region-segregated) and GCP Secret Manager with regional KMS keys.

## Rationale
Mirrored regional container deployments in GKE ensure complete adherence to GDPR and HIPAA data residency mandates by keeping EU health data in Europe and US data in America. Decoupled microservices with local caching, robust WebRTC relays, and regional pub/sub queues guarantee high availability and low-bandwidth resilience for rural users without compromising traceability or security.