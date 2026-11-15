## Overview
The Cross-Border Telehealth Platform provides secure video consultations, e-prescriptions, and an AI symptom checker for patients in the EU and US. The architecture enforces strict regional data residency and regulatory compliance under GDPR and HIPAA using Google Cloud Platform.

## Key Elements
- Web & Mobile Client Apps (Flutter / React Native)
- API Gateway (Google Cloud API Gateway / Apigee)
- Core Telehealth Service (Spring Boot / Java)
- AI Symptom Checker Service (FastAPI / Python)
- Interoperability & E-Prescription Service (Node.js)
- WebRTC SFU Media Relay (LiveKit on GKE)
- SFU Core Router (Go / LiveKit SDK)
- Adaptive Bitrate (ABR) Controller (Go)
- Media Auth & Token Validator (Go)
- Telemetry & Audit Exporter (Go)
- Data & Security Layer (Cloud SQL, Cloud Storage, GCP Cloud KMS, GCP Service Mesh / Istio)

## Relationships
- Web & Mobile Client Apps -> SFU Core Router: Streams video consultations [WebRTC, SRTP/UDP]
- Core Telehealth Service -> Media Auth & Token Validator: Issue/Verify session tokens [gRPC with mTLS]
- ABR Controller -> Telemetry & Audit Exporter: Publishes QoS metrics [In-memory channel]
- Telemetry & Audit Exporter -> Regional Cloud Logging: Exports anonymized session metadata [gRPC/TLS]

## Technology Stack
- Google Cloud Platform (GCP): Target cloud provider for regional isolation in `europe-west3` and `us-central1`.
- LiveKit on Google Kubernetes Engine (GKE): Container orchestration and media relay for real-time video.
- Go (Golang): High concurrency language used for all WebRTC SFU components and the LiveKit SDK.
- DTLS-SRTP (AES-128/256-CM): Encrypts all media streams with ephemeral Diffie-Hellman keys.
- GCP Service Mesh (Istio): Secures internal control plane traffic with mutual TLS (mTLS).

## Rationale
This architecture ensures strict compliance with EU and US healthcare regulations by isolating regional data infrastructure. The containerized WebRTC SFU with adaptive bitrate control guarantees high availability and resilient video consultations even over unstable connections.