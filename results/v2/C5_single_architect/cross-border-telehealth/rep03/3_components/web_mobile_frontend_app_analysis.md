## Overview
The Cross-Border Telehealth Platform provides video consultations, e-prescriptions, and an AI symptom checker for patients across the EU and US. It ensures strict data residency, regulatory compliance, and resilience for unstable rural internet connections.

## Key Elements
- Patients and Clinicians (Users)
- Web/Mobile Frontend App (Flutter)
- UI Presentation Layer, Local State & Storage Manager (SQLite/Hive with SQLCipher), API Client & Sync Engine, WebRTC Media Client, Regional Region-Routing / Config Module (Components)
- API Gateway (Envoy/GCP API Gateway)
- WebRTC SFU Video Service (Mediasoup)
- AI Inference Service (Python/FastAPI)
- Regional Data Stores (GCP Cloud SQL/Spanner)

## Relationships
- Web/Mobile Frontend App -> Regional Region-Routing Module: Pins app instance to correct regional endpoint [HTTPS]
- Web/Mobile Frontend App -> API Gateway: Sends API requests, consent payloads, and symptom-checker inputs with session telemetry [HTTPS and WSS using TLS 1.3]
- Web/Mobile Frontend App -> WebRTC SFU Video Service: Streams media directly for consultations [WebRTC / ICE / DTLS / SRTP]

## Technology Stack
- Flutter: Standardizes cross-platform mobile and web application development.
- SQLite/Hive with SQLCipher: Enables encrypted offline data caching for degraded rural internet connections (R-06).
- WebRTC, DTLS, SRTP: Delivers low-latency, resilient peer-to-peer video streaming.
- GCP (`europe-west3` and `us-central1`): Enforces regional data residency for EU and US compliance.

## Rationale
This architecture uses localized client routing and regional cloud infrastructure to strictly enforce data residency and privacy mandates (GDPR/HIPAA). Furthermore, offline caching and direct WebRTC streaming guarantee high availability and continuous video consultations in low-bandwidth rural environments.