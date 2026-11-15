## Overview
The Cross-Border Telehealth Platform provides video consultations, e-prescriptions, and an AI symptom checker for patients across the EU and US. It enforces strict regional data residency, regulatory compliance, and low-bandwidth resilience.

## Key Elements
- Web/Mobile Client SPA/PWA (Flutter/React)
- Google Cloud API Gateway
- Video Streaming Server (LiveKit WebRTC SFU on GKE) containing Signaling Component, SFU Media Router, Recording & Audit Sidecar, and Media Policy & Token Enforcer
- Data Residency & Consent Router (Go)
- Core Services Backend (Go/Spring Boot)
- AI Symptom Checker Service (Python/FastAPI)
- Interoperability Adapter (Node.js/TypeScript)
- Cloud SQL PostgreSQL

## Relationships
- Web/Mobile Client SPA/PWA -> Google Cloud API Gateway: Sends API requests [HTTPS/REST]
- Signaling Component -> Media Policy & Token Enforcer: Validates regional access tokens [In-memory function call]
- Media Policy & Token Enforcer -> Data Residency & Consent Router: Verifies patient consent state [gRPC over TLS]
- Signaling Component -> SFU Media Router: Configures media tracks [Internal gRPC]
- SFU Media Router -> Web/Mobile Client SPA/PWA: Transmits adaptive media streams [WebRTC over UDP/ICE/DTLS]

## Technology Stack
- Google Cloud Platform (GCP regions `europe-west3` and `us-central1`): Enforces regional data residency constraints.
- LiveKit WebRTC SFU on Google Kubernetes Engine (GKE): Powers real-time video consultations with adaptive streaming.
- Go, Python (FastAPI), Node.js, and TypeScript: Backend component languages chosen for high performance and concurrency.
- PostgreSQL (Cloud SQL): Relational storage for platform metadata and application data.

## Rationale
This architecture isolates regional data traffic within GCP regions to satisfy GDPR and HIPAA compliance mandates. The decomposed video streaming components ensure low-bandwidth resilience for rural patients while strictly enforcing regional access policies.