## Overview
The Cross-Border Telehealth Platform provides video consultations, e-prescriptions, and an AI symptom checker for patients across the EU and US. The system ensures strict data residency, regulatory compliance (GDPR/HIPAA/EU MDR), and resilience for rural, low-bandwidth users.

## Key Elements
* **Web Application & Mobile Apps**: Multi-platform client interface (Flutter/React) featuring Consent & Profile, Adaptive Video Streaming, Triage & AI Interface, Offline Cache Manager, Localization & Regulatory Banner, and Routing & Regional Affinity modules.
* **Regional API Gateways**: Google Cloud API Gateways deployed in `europe-west3` (EU) and `us-central1` (US).
* **Core Services**: Core Telehealth Service (Go/Spring Boot), Video Mediation Service (Twilio/WebRTC), E-Prescription Integrator (Node.js), and AI Orchestrator & Audit Logger (Python).
* **Data & Messaging**: Google Cloud Pub/Sub, Cloud SQL for PostgreSQL, and Memorystore for Redis.
* **External Systems**: Local Pharmacies, EU National E-Prescription Networks, Third-party Video Provider, AI Symptom Checker Model Registry, Identity Verification Services, and Regional Payment Gateways.

## Relationships
* **Patients & Clinicians -> Web Application & Mobile Apps**: Accesses telehealth, video consultations, and AI symptom checker via HTTPS and WSS.
* **Web Application & Mobile Apps -> Regional API Gateways**: Sends client requests and syncs state via HTTPS and WSS with SSL/TLS certificate pinning.
* **Regional API Gateways -> Core Telehealth Service**: Routes regional requests securely within GCP (`europe-west3` and `us-central1`).
* **Core Telehealth Service -> Video Mediation Service**: Mediates video consultations using WebRTC.
* **AI Orchestrator -> Model Registry**: Logs symptom-checker inputs and model versions for EU MDR traceability.

## Technology Stack
* **Flutter & React**: Chosen for cross-platform mobile and web frontend development with local UI state management.
* **WebRTC & VP8/H.264**: Enables adaptive, low-bandwidth video streaming (<300 kbit/s) with audio-only fallback.
* **SQLite & IndexedDB**: Provides encrypted local storage for offline caching on mobile and web clients.
* **Android Keystore & iOS Keychain**: Secures hardware-backed encryption for local PHI and authentication tokens.
* **Go, Spring Boot, Node.js & Python**: Powers microservices for core telehealth, integrations, and AI orchestration.
* **Google Cloud Platform (GCP)**: Enforces regional data residency in `europe-west3` and `us-central1` using Cloud SQL, Memorystore, and Pub/Sub.

## Rationale
This architecture enforces strict regional data segregation to guarantee GDPR and HIPAA compliance while maintaining high availability for rural users via offline caching and adaptive video streaming. Component-level security controls, including hardware-backed encryption, SSL/TLS pinning, and cryptographic signing, protect sensitive health data across cross-border operations.