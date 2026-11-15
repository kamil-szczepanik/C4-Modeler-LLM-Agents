## Overview
The Cross-Border Telehealth Platform provides secure video consultations, e-prescriptions, and an AI symptom checker for patients across the EU and US. It ensures strict data residency, offline resilience for rural users, and regulatory compliance (GDPR/HIPAA/MDR).

## Key Elements
- **Users**: Patients and Licensed Clinicians.
- **External Systems**: EU National E-Prescription Gateways, US Pharmacy Networks, AI Symptom Checker Engine, Compliance Authorities.
- **Containers**: Web/Mobile Frontend (Flutter), Regional Ingress (Cloud Load Balancing & Envoy), Telehealth Service (Go/WebRTC), Prescription & Record Service (Java/Spring Boot), AI Orchestrator & Audit Service (Python/FastAPI), Consent & Identity Service (Keycloak/PostgreSQL).
- **Frontend Components**: Routing & State Component (Hive/SQLite), Video Consultation Component, Consent & Triage UI Component, Region-Aware API Client.

## Relationships
- Web/Mobile Frontend -> Regional Ingress: Routes all API, WebSocket, and WebRTC traffic [HTTPS, WebSockets, WebRTC / TLS 1.3].
- Web/Mobile Frontend -> Telehealth Service: Streams video and audio consultations [WebRTC / UDP].
- Web/Mobile Frontend -> AI Orchestrator & Audit Service: Requests symptom check triage and recommendations [HTTPS/REST].
- Web/Mobile Frontend -> Consent & Identity Service: Authenticates users and manages granular consents [OAuth2/OIDC].

## Technology Stack
- **Flutter**: Cross-platform web/mobile frontend framework chosen for offline-first capabilities.
- **SQLite/Hive with AES-256**: Local storage encrypted via device hardware keystores (Android Keystore/iOS Keychain) for offline rural support (R-06).
- **Go & WebRTC**: Telehealth streaming engine supporting adaptive bitrate scaling below 300 kbit/s.
- **Python / FastAPI**: AI orchestrator for traceable symptom checker logging (R-07).
- **GCP (`europe-west3`, `us-central1`)**: Cloud provider and regions enforcing strict data residency (R-05).

## Rationale
This architecture uses an offline-first Flutter client with hardware-backed encryption to maintain rural availability and security without violating compliance. Dynamic regional API pinning and isolated GCP deployments guarantee that EU and US health data remain strictly segregated per regulatory mandates.