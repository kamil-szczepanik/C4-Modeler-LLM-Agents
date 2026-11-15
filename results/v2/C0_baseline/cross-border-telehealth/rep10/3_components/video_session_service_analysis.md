## Overview
[The Cross-Border Telehealth Platform provides secure video consultations, e-prescriptions, and an AI symptom checker for EU and US patients. The architecture ensures strict regional data residency, regulatory compliance, and high availability over unstable connections.]

## Key Elements
* Patients (EU / US), Licensed Clinicians, Compliance Auditors
* Regional API Gateway / BFF (Node.js, GraphQL)
* Consent & Policy Engine (.NET)
* Video Session Service (Go)
  * Session Coordinator Component (Go)
  * SFU Media Proxy Component (Go, Pion WebRTC)
  * Quality Telemetry Logger Component (Go)
* AI Orchestration Service (Python, FastAPI)
* FHIR & Prescription Integration Service (.NET)
* Regional WORM Storage (GCP Cloud Storage, Cloud KMS)
* Third-Party Video Infrastructure

## Relationships
* Regional API Gateway -> Video Session Service: Manages session initiation [gRPC, mTLS, Istio Service Mesh]
* Session Coordinator -> SFU Media Proxy: Orchestrates media routing state [gRPC]
* SFU Media Proxy -> Third-Party Video Infrastructure: Relays encrypted streams [WebRTC, SRTP, DTLS]
* Quality Telemetry Logger -> Regional WORM Storage: Persists cryptographically signed audit logs [gRPC, TLS 1.3, Cloud KMS]

## Technology Stack
* GCP (`europe-west3`, `us-central1`): Ensures regional data residency and multi-region deployment.
* Go (Pion WebRTC): Powers high-performance, low-latency video session handling and adaptive bitrate switching.
* Kubernetes (GKE): Manages containerized microservices with regional namespace isolation.
* gRPC & mTLS: Secures internal microservice communication and transport encryption.
* GCP Cloud KMS: Enforces regional customer-managed encryption keys for WORM storage.

## Rationale
[This decoupled, region-isolated architecture guarantees strict GDPR and HIPAA compliance while supporting adaptive video degradation for rural connectivity. Component-level separation of telemetry and media routing ensures absolute regulatory auditability without compromising real-time performance.]