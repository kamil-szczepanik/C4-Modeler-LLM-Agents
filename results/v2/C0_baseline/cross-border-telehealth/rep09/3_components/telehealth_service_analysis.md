## Overview
The Cross-Border Telehealth Platform provides secure video consultations, e-prescriptions, and an AI symptom checker for patients in the EU and US. It ensures strict data residency, regulatory compliance (GDPR/HIPAA), and resilient media streaming for rural areas.

## Key Elements
- Patients and Licensed Clinicians (Users)
- Web/Mobile Frontend (Flutter)
- Regional Ingress (GCP Cloud Load Balancing & Envoy)
- Telehealth Service (Go / WebRTC)
- Consent & Identity Service (Keycloak / PostgreSQL)
- Prescription & Record Service (Java / Spring Boot)
- AI Orchestrator & Audit Service (Python / FastAPI)
- National E-Prescription Gateways (EU) and US Pharmacy Networks
- Internal Telehealth Components: Signaling Component, Media Gateway (SFU / Pion), Bandwidth Adaptation Engine, Session Audit Logger, Session Lifecycle Manager

## Relationships
- Web/Mobile Frontend -> Telehealth Service: Streams video consultations [WebRTC / UDP]
- Signaling Component -> Consent & Identity Service: Validates short-lived session tokens [gRPC / mTLS]
- Session Lifecycle Manager -> Prescription & Record Service: Logs completed session metadata and feedback triggers [gRPC]
- Telehealth Service -> Regional TURN Relays: Relays media streams under strict data residency constraints [TLS/DTLS/SRTP]

## Technology Stack
- Go: Chosen for high-throughput, low-latency media handling in the Telehealth Service
- WebRTC / Pion & SRTP: Provides real-time communication and secure end-to-end media encryption
- GCP (`europe-west3`, `us-central1`): Enforces regional data residency for EU and US health data
- gRPC with mTLS: Ensures secure, efficient inter-container communication

## Rationale
This architecture uses regional GCP deployments and isolated media gateways to satisfy strict GDPR, HIPAA, and data residency mandates. Furthermore, the Go-based WebRTC stack with dynamic bandwidth adaptation guarantees consultation availability even on unstable rural connections below 300 kbit/s.