## Overview
The Cross-Border Telehealth Platform provides video consultations, e-prescriptions, and an AI symptom checker for EU and US patients on GCP. It ensures regional data residency, regulatory compliance (GDPR/HIPAA), and high availability for rural areas.

## Key Elements
- Patients (EU & US) and Licensed Clinicians
- Web/Mobile Client (Flutter / React Native)
- API Gateway (Cloud Endpoints / Envoy)
- Core Telehealth Backend (Node.js / Go)
- Video Media Server (Janus / WebRTC on GCE)
- TURN/STUN Relay Tier
- Databases (Cloud SQL PostgreSQL & Cloud Storage)

## Relationships
- Patients & Clinicians -> Web/Mobile Client: HTTPS and WebRTC [HTTPS / WebRTC]
- Web/Mobile Client -> API Gateway: Mutual TLS and JWT validation [mTLS / JWT]
- Web/Mobile Client -> Video Media Server: Video streaming and media traversal [WebRTC / SRTP]

## Technology Stack
- Flutter / React Native: Enables cross-platform client delivery with offline-first SQLite caching for unstable networks.
- WebRTC / Janus: Delivers low-latency, resilient video consultations for degraded bandwidth conditions.
- GCP (europe-west3 / us-central1): Enforces strict regional data residency compliance for EU and US health data.
- PostgreSQL & Cloud Storage: Secures patient records and audit logs regionally.

## Rationale
This architecture guarantees strict regional compliance with GDPR and HIPAA by isolating data storage within GCP regions. It maintains high availability for rural users through offline-first local caching and robust WebRTC media handling.