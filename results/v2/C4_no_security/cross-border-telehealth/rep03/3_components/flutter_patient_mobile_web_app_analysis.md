## Overview
Cross-Border Telehealth Platform provides video consultations, e-prescriptions, and an AI symptom checker for EU and US patients. It enforces strict regional data residency and compliance with GDPR, HIPAA, and EU MDR.

## Key Elements
* Flutter Patient Mobile/Web App (Flutter container)
* Presentation Layer (Dart/Flutter UI component)
* State & Local Storage Manager (Hive / SQLite component)
* API Client & Region Router (Dio / HTTP component)
* WebRTC Video Module component
* Feature Flag & Configuration Provider component
* GCP API Gateway (`europe-west3`, `us-central1`)
* Consent & Profile Management Service

## Relationships
* Flutter App to GCP API Gateway via HTTPS (REST/GraphQL) and WSS (WebSockets) for signaling
* WebRTC Video Module to regional TURN/STUN relays for peer-to-peer media streams
* API Client & Region Router to GCP API Gateways (`europe-west3` or `us-central1`) based on user geolocation
* Feature Flag Provider to Consent & Profile Management Service via HTTPS for asynchronous sync

## Technology Stack
* Flutter: Cross-platform mobile and web client framework
* Hive / SQLite: Local client-side caching for offline resilience (<300 kbit/s)
* Dio / HTTP: Regional API routing and communication
* WebRTC: Low-bandwidth video consultations with regional TURN/STUN fallback
* GCP Cloud Build / GitHub Actions: Automated CI/CD deployment pipelines

## Rationale
This architecture ensures regional compliance and data residency by routing requests through localized GCP gateways. Client-side caching and WebRTC support reliable telehealth access for rural patients with unstable connections.