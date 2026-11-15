## Overview
Cross-Border Telehealth Platform provides video consultations, e-prescriptions, and an AI symptom checker for patients across the EU and US. It ensures strict data residency, regulatory compliance (GDPR/HIPAA/EU MDR), and high availability over unstable connections.

## Key Elements
* Patients and Clinicians (EU & US)
* Client Applications (Flutter / Web)
* UI Layer
* Local State & Storage Manager (Hive / SQLite with SQLCipher)
* Network & Sync Engine
* WebRTC Client SDK
* Localization & Accessibility Engine
* API Gateway (Envoy / Google Cloud Endpoints)
* Containerized SFUs (mediasoup)

## Relationships
* Patients and Clinicians -> Client Applications: Accesses platform capabilities [HTTPS / WebRTC]
* UI Layer -> API Gateway: Sends structured API requests [gRPC-Web / HTTPS]
* Network & Sync Engine -> API Gateway: Communicates with dynamic region endpoints [gRPC-Web / HTTPS with Certificate Pinning]
* WebRTC Client SDK -> Containerized SFUs (mediasoup): Streams video and audio [ICE / DTLS / SRTP]
* UI Layer -> Local State & Storage Manager: Reads and writes cached data [Encrypted Local I/O]

## Technology Stack
* Flutter / Web: Maximizes cross-platform reach for mobile and browser users while optimizing development costs.
* Hive / SQLite with SQLCipher: Secures cached PHI and consent preferences at rest using device-derived encryption keys.
* mediasoup SFU: Enables scalable, low-latency video consultations with adaptive codecs for connections below 300 kbit/s.
* OpenTelemetry & Crashlytics: Provides client-side observability with on-device PII/PHI scrubbing for telemetry data.

## Rationale
This architecture ensures regional compliance and robust offline resilience by combining encrypted local storage with dynamic jurisdiction routing. It maintains secure, low-bandwidth video sessions and traceable AI interactions to satisfy stringent healthcare regulations in both the EU and US.