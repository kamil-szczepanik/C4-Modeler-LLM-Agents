## Overview
The Cross-Border Telehealth Platform provides secure video consultations, e-prescriptions, and an AI symptom checker for EU and US patients. The architecture enforces strict regional data residency, HIPAA/GDPR compliance, and low-bandwidth availability.

## Key Elements
- Patients (EU & US) and Licensed Clinicians
- Frontend Client Apps (Flutter)
- API Gateway / BFF (Envoy / gRPC-Web)
- Video Consultation Service Container (Mediasoup SFU)
- Signaling Component (Node.js / WebSocket)
- SFU Media Router (C++ / Mediasoup)
- Session Audit Logger (Go)
- Consent & Policy Engine (Opa / Go)
- Data Layer (PostgreSQL / Cloud SQL)
- GCP Regional Infrastructure (`europe-west3`, `us-central1`)

## Relationships
- Frontend Client Apps -> API Gateway / BFF: Client requests [HTTPS, gRPC-Web]
- API Gateway / BFF -> Signaling Component: Room signaling and session initiation [gRPC, mTLS]
- Signaling Component -> Consent & Policy Engine: Ephemeral token validation [gRPC]
- Frontend Client Apps <-> SFU Media Router: Real-time media streaming [DTLS-SRTP, ICE/STUN/TURN]
- Session Audit Logger -> Cloud Logging: Asynchronous metadata emission [HTTPS]

## Technology Stack
- **Flutter:** Cross-platform client application framework for consistent user experience.
- **Envoy & gRPC-Web:** High-performance API gateway and inter-service communication protocol.
- **C++ Mediasoup SFU:** High-throughput selective forwarding unit optimized for Simulcast/SVC adaptive streaming.
- **Node.js & Go:** Microservice runtimes for signaling, audit logging, and policy enforcement.
- **Google Kubernetes Engine (GKE):** Container orchestration utilizing `c2` compute-optimized instances.

## Rationale
The architecture uses isolated regional GKE clusters in GCP to strictly enforce EU and US health data residency constraints. Mediasoup SFU with adaptive streaming guarantees uninterrupted consultations for rural users on unstable connections below 300 kbit/s.