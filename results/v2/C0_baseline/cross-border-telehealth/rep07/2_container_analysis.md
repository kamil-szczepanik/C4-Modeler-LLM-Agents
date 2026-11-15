## Overview
[The Cross-Border Telehealth Platform provides video consultations, e-prescriptions, and an AI symptom checker for patients across the EU and US while strictly enforcing regional data residency and compliance. It leverages a cloud-native architecture on GCP to ensure data isolation, regulatory accountability, and graceful degradation for rural, low-bandwidth users.]

## Key Elements
- Patients (EU/US), Licensed Clinicians, Platform Administrators, Local Pharmacy Staff, Billing Specialists
- Global External HTTP(S) Load Balancers
- Regional API Gateways (Kong / GCP API Gateway)
- Consultation Service (Go/Node.js) & Media Relay/SFU Container (LiveKit/Mediasoup)
- Consent Management Service, Prescription & Interoperability Service (Java/Spring Boot), AI Inference Orchestrator (Python/FastAPI)
- Google Kubernetes Engine (GKE) regional clusters with regional TURN/STUN relays
- Regional Cloud Spanner and BigQuery instances
- External Systems: Local Pharmacies, AI Symptom Checker Engine, Notification Gateway, Identity Providers

## Relationships
- Patients access the platform via Web Applications (SPA) and Native Mobile Apps (Flutter) over HTTPS/gRPC.
- API Gateways route regional traffic, validate OAuth2/OIDC JWTs, and verify cryptographic consent tokens.
- Internal microservices communicate securely via gRPC over mTLS within a GKE service mesh.
- Consultation Services manage WebRTC signaling routed through regional SFU containers and TURN/STUN relays.
- Prescription Services transmit e-prescriptions to regional pharmacy networks using HL7 FHIR (US) and national standards (EU).
- AI Inference Orchestrator logs interactions and model versions to regional BigQuery instances.

## Technology Stack
- Cloud Provider: GCP (regions: europe-west3, us-central1) for regional isolation and data sovereignty
- Frontend: Flutter for cross-platform native mobile and web rendering
- Backend: Go, Node.js, Java (Spring Boot), and Python (FastAPI) for domain-specific microservices
- Real-Time Media: LiveKit or Mediasoup SFU with Google Cloud TURN/STUN relays for bandwidth adaptation
- Orchestration & Mesh: Google Kubernetes Engine (GKE) with SPIFFE/SPIRE-based mTLS service mesh
- Storage & Databases: Regional Cloud Spanner for transactions and BigQuery for immutable AI audit logs
- Security: GCP VPC Service Controls, Cloud KMS with CMEK, and OAuth2/OIDC via regional Identity Providers

## Rationale
[This architecture enforces strict regional isolation through GCP VPC Service Controls and region-locked Cloud Spanner and BigQuery instances, ensuring complete compliance with GDPR and HIPAA mandates. Additionally, integrating regional GKE clusters, SFU media relays, and low-bandwidth fallback mechanisms guarantees continuous, high-availability care for rural users.]