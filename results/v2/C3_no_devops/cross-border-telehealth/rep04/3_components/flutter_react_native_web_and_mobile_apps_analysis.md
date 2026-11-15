## Overview
The Cross-Border Telehealth Platform provides video consultations, e-prescriptions, and an AI symptom checker for patients in the EU and US. It enforces strict regional data residency, GDPR/HIPAA compliance, and EU MDR traceability while supporting low-bandwidth rural environments.

## Key Elements
- Patients (EU/US), Licensed Clinicians, System Administrators, Caregivers/Guardians
- Flutter/React Native Web and Mobile Apps (Client Container)
  - Region & Compliance Gateway Client
  - Offline Resilience Store (SQLite/MMKV with SQLCipher AES-256)
  - WebRTC Media Client
  - AI/MDR Interaction Module
  - State Synchronizer Component
- Kong API Gateway/BFF
- Spring Boot Core Telehealth Service
- FastAPI AI Symptom Checker
- Node.js E-Prescription Service
- Java Consent Management Service
- GCP Cloud SQL (PostgreSQL), GCP Cloud Storage, GCP Cloud Pub/Sub, GCP Cloud KMS

## Relationships
- Patients & Clinicians -> Flutter/React Native Apps: Access via HTTPS / WebSockets (TLS 1.3) with OAuth2/OIDC & PKCE
- Flutter/React Native Apps -> Kong API Gateway/BFF: API requests and auth via HTTPS / WebSockets with Certificate Pinning
- WebRTC Media Client -> Kong API Gateway: Adaptive video streaming via ICE/TURN over UDP with TCP/TLS fallback and SRTP/DTLS-SRTP
- Regional Services -> GCP Cloud SQL: Data storage isolated within `europe-west3` (EU) and `us-central1` (US)

## Technology Stack
- **Frontend Framework:** Flutter / React Native for cross-platform web and mobile deployment
- **Local Storage & Security:** SQLCipher (AES-256) backed by Android Keystore and iOS Keychain for secure offline caching
- **Communication Protocols:** HTTPS, WebSockets (TLS 1.3), WebRTC, SRTP, and DTLS-SRTP for secure low-bitrate video
- **Backend Frameworks:** Spring Boot (Java), FastAPI (Python), and Node.js for microservices
- **Cloud Infrastructure:** Google Cloud Platform (GCP) across `europe-west3` and `us-central1` regions

## Rationale
This architecture ensures strict multi-region compliance (GDPR/HIPAA) by isolating data processing and storage within designated GCP regions. Client-side security controls, offline caching, and WebRTC fallback mechanisms guarantee reliable, secure telehealth delivery even for rural users with unstable connections.