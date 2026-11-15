## Overview
[Cross-Border Telehealth Platform providing video consultations, e-prescriptions, and an AI symptom checker for EU and US patients while ensuring strict compliance with GDPR and HIPAA.]

## Key Elements
*   Patients and Licensed Clinicians
*   Web App & Mobile App (Flutter / React)
*   GCP API Gateway
*   Core Telehealth Backend & AI Symptom Checker Service
*   Video Streaming Server (WebRTC / SFU Mediasoup)
*   EU E-Prescriptions Adapter & US Healthcare Interoperability Service
*   GCP Cloud SQL, Cloud Storage, Cloud KMS, and Secret Manager

## Relationships
*   Patients & Clinicians -> Web App & Mobile App: Interact via client applications [HTTPS, WebSockets]
*   Web App & Mobile App -> GCP API Gateway: Sends API requests and real-time data [HTTPS, WebSockets]
*   Web App & Mobile App -> Video Streaming Server: Streams video consultations [WebRTC / RTP]
*   Offline State Manager -> Security & Cryptography Module: Encrypts/decrypts cached data [Platform Crypto API]
*   Client Telemetry -> GCP API Gateway: Flushes batched telemetry logs [HTTPS]

## Technology Stack
*   **Flutter & React:** Chosen for cross-platform mobile and web frontend consistency.
*   **WebRTC & SFU (Mediasoup):** Enables real-time video streaming with adaptive bitrate scaling for unstable connections.
*   **Go & Spring Boot / Python & FastAPI:** Backend processing and AI symptom checker services.
*   **GCP (europe-west3 & us-central1):** Target cloud provider enforcing regional data residency.

## Rationale
[This architecture uses regional GCP deployments to strictly separate EU and US health data, meeting GDPR and HIPAA constraints. Component-level security and adaptive media controls ensure availability and data protection across unstable rural networks.]