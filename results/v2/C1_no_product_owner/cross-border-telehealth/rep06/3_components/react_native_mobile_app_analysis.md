## Overview
[The Cross-Border Telehealth Platform provides video consultations, e-prescriptions, and an AI symptom checker for patients in the EU and US under GDPR and HIPAA compliance. The React Native Mobile App container serves as the cross-platform client for patients and clinicians, engineered for unstable rural internet connections and secure regional data routing.]

## Key Elements
* UI Layer (React Navigation & Native UI)
* State & Offline Sync Engine (WatermelonDB / Redux Toolkit)
* Video Module (LiveKit React Native Client)
* Secure Storage (`react-native-encrypted-storage`)
* Local Biometric & Auth Module (`react-native-biometrics`)
* Telemetry & Diagnostics Agent (Sentry RN / OpenTelemetry)
* Anti-Tampering & RASP Module (`react-native-jailbreak-detection`)

## Relationships
* `UI Layer` -> `State & Offline Sync Engine` [In-App Events]
* `UI Layer` -> `Local Biometric & Auth Module` [In-App Events]
* `State & Offline Sync Engine` -> `GCP Cloud Endpoints / Envoy API Gateway` [HTTPS (JSON/REST) and WSS (WebSockets/QUIC)]
* `Video Module` -> `Video Media Server (LiveKit SFU)` [WebRTC/QUIC]
* `Telemetry & Diagnostics Agent` -> `GCP Cloud Endpoints / Envoy API Gateway` [HTTPS - Anonymized Telemetry]

## Technology Stack
* React Native & TypeScript: For cross-platform mobile rendering
* WatermelonDB: For offline data caching and synchronization over unstable rural connections (NFR-06)
* LiveKit React Native Client: For low-bandwidth WebRTC video streaming
* `react-native-encrypted-storage`: For secure local client-side encryption of health tokens
* CodePush / EAS Update: For instant over-the-air hot-fixing with cryptographic signature verification and crash-loop rollback
* Sentry / OpenTelemetry: For edge-anonymized crash and WebRTC telemetry tracking

## Rationale
[The architecture ensures strict data residency (R-05) and regulatory compliance across EU and US jurisdictions through dynamic gateway routing and secure local isolation. It guarantees high availability and usability in rural areas via robust offline synchronization and low-bandwidth WebRTC video adaptation.]