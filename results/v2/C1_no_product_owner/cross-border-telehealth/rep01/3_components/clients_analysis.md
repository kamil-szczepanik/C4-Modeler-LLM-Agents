## Overview
The Cross-Border Telehealth Platform provides secure video consultations, e-prescriptions, and an AI symptom checker for patients in the EU and US. It ensures strict data residency, regulatory compliance, and high availability for users with unstable internet connections.

## Key Elements
- Patients (EU and US) & Clinicians
- Clients Container: Patient Web App (React), Patient Mobile App (Flutter), Clinician Portal (React), Local State Manager (SQLCipher/IndexedDB), WebRTC Media Engine
- External Systems: AI Symptom Checker Engine, National Pharmacies (EU) & US Pharmacies, Identity Providers, GCP KMS
- Core Containers: API Gateway / BFF (Node.js/GraphQL), Consultation Service (Go), Prescription Service (Java), AI Orchestrator (Python), Consent & Audit Service (Java)
- Infrastructure: GCP (europe-west3, us-central1), Istio Service Mesh, Google Cloud SQL, Memorystore

## Relationships
- Patients/Clinicians -> Clients: Interacts via Web/Mobile UI
- Clients -> API Gateway / BFF: REST/JSON over HTTPS (mutations/queries) and WebSockets (signaling/telemetry)
- WebRTC Media Engine -> GCP Media Relays: Encrypted SRTP audio/video streams over UDP/TCP (TURN/STUN geo-pinned to region)
- API Gateway -> Core Microservices: Internal gRPC over Istio Service Mesh
- Core Services -> GCP Cloud SQL / Memorystore: Encrypted data persistence with region isolation

## Technology Stack
- Client Layer: React (TypeScript) for web; Flutter (Dart) for cross-platform mobile apps to maximize code reuse
- Local Storage: SQLCipher (mobile) and encrypted IndexedDB for offline-first capabilities and secure caching
- Media Streaming: Native WebRTC with DTLS-SRTP for low-bandwidth video (down to 300 kbit/s)
- Backend: Node.js/GraphQL (BFF), Go (Consultation), Java Spring Boot (Prescription/Consent), Python FastAPI (AI)
- Cloud & Security: GCP (europe-west3, us-central1), Istio Service Mesh, TLS 1.3, OAuth 2.0/OIDC with short-lived memory-stored JWTs

## Rationale
This architecture guarantees strict regional data residency (GDPR/HIPAA compliance) by isolating workloads and media relays within GCP EU and US regions. The offline-first client design and adaptive WebRTC engine ensure reliable telehealth delivery for rural users with unstable internet connections.