## Overview
Cross-border telehealth platform providing video consultations, e-prescriptions, and an AI symptom checker for EU and US patients. The architecture ensures strict regional data residency, offline resilience, and regulatory compliance under GDPR, HIPAA, and EU MDR.

## Key Elements
- Patients & Licensed Clinicians
- Web/Mobile Client Applications (Flutter / React Native)
- Cloud Load Balancing / API Gateway
- LiveKit WebRTC SFU on Google Kubernetes Engine (GKE)
- AI Symptom Checker (Python / FastAPI on Cloud Run)
- Consent Management Service & Core Telehealth (Spring Boot on GKE)
- Google Cloud Pub/Sub, BigQuery, Cloud Logging
- Google Cloud KMS (CMEK) and Google Secret Manager

## Relationships
- Web/Mobile Client Applications -> Cloud Load Balancing / API Gateway via HTTPS, WebSockets (WSS)
- API Client & WebRTC Module -> LiveKit SFU via WebRTC
- Notification & Messaging -> Web/Mobile Client Applications via APNS, FCM, WebSockets
- Services -> Google Cloud Pub/Sub via gRPC/AMQP

## Technology Stack
- Flutter & React Native: Unified cross-platform client codebase for rapid multi-region market entry.
- WatermelonDB / Hive: Local offline-first caching for rural patients with unstable connections (R-06).
- LiveKit WebRTC SFU: Dynamic bitrate video adaptation for degraded network conditions.
- Spring Boot & FastAPI: Microservices powering core telehealth logic and AI symptom checking.
- Google Cloud Platform (europe-west3, us-central1): Regional isolation ensuring strict EU/US data residency (R-05).

## Rationale
The architecture combines regional cloud pinning with offline-first client storage to satisfy strict GDPR and HIPAA data residency constraints while maintaining availability in rural areas. Containerized microservices and decoupled messaging ensure scalability, traceability for EU MDR, and robust cross-border interoperability.