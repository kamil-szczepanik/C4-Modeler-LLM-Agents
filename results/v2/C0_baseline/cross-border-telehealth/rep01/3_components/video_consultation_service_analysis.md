## Overview
• The Cross-Border Telehealth Platform provides video consultations, e-prescriptions, and an AI symptom checker for EU and US patients.
• It ensures strict data residency, low-bandwidth optimization, and regulatory compliance across multi-region cloud infrastructure.

## Key Elements
• Patients and Clinicians (Users)
• External Pharmacy Networks, National Health Systems, Identity Providers (External Systems)
• API Gateway (Cloud Endpoints / Apigee)
• Regional Application Services (Google Kubernetes Engine)
• Video Consultation Service: Signaling & Session Manager, Media Relay & SFU Controller (Janus/Mediasoup), Localization & UI Gateway (React/Next.js), Media Quality & Audit Logger
• AI Symptom Checker (Vertex AI endpoints)
• Policy & Consent Engine (Open Policy Agent)
• Interoperability Adapter
• Data & Audit Tier (Cloud SQL, Cloud Spanner, WORM Cloud Storage, Redis)

## Relationships
• Regional Application Services -> Signaling & Session Manager: Authenticates and initializes session [gRPC / mTLS]
• Signaling & Session Manager -> Media Relay & SFU Controller: Allocates media paths [Internal API]
• Media Relay & SFU Controller -> Media Quality & Audit Logger: Emits real-time stream quality metrics [Async / Cloud Pub/Sub]
• Signaling & Session Manager -> Data & Audit Tier: Persists session metadata locally per region [gRPC / SQL]
• Patients/Clinicians -> Localization & UI Gateway: Accesses localized waiting rooms and video UI [HTTPS / WebSockets]

## Technology Stack
• Google Cloud Platform (GCP): Target cloud provider utilizing `europe-west3` and `us-central1` for regional isolation.
• Google Kubernetes Engine (GKE): Container orchestration with Istio service mesh for mTLS and strict network policies.
• WebRTC SFU (Janus/Mediasoup) & DTLS-SRTP: Powers adaptive bitrate video streaming for low-bandwidth connections (<300 kbit/s) with encrypted media paths.
• Node.js / Go & Redis: Used for signaling state management and short-lived session token caching.
• Vertex AI: Hosts the traceable AI symptom checker model endpoints.

## Rationale
• Separate air-gapped GKE clusters per region enforce strict GDPR and HIPAA data residency mandates.
• WebRTC adaptive bitrate streaming and regional SFU controllers ensure reliable consultations for rural patients with unstable connections.