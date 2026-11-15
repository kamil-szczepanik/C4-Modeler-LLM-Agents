## Overview
The Cross-Border Telehealth Platform provides secure video consultations, e-prescriptions, and an AI symptom checker for EU and US patients. It enforces strict regional data residency and regulatory compliance on Google Cloud Platform.

## Key Elements
- **Users**: Patient, Clinician
- **External Systems**: External Pharmacy Systems, AI Model Provider / LLM API, National Identity Providers, National Health Registries
- **Containers**: Web/Mobile Client SPA/PWA, Google Cloud API Gateway, Data Residency & Consent Router, Core Services Backend, AI Symptom Checker Service, Video Streaming Server, Interoperability Adapter, Cloud SQL PostgreSQL
- **Components (Web/Mobile Client)**: UI Presentation Layer, State & Sync Manager, Secure Local Repository, WebRTC Media Client

## Relationships
- Patient / Clinician -> Web/Mobile Client SPA/PWA: Interacts via [HTTPS/WSS]
- Web/Mobile Client SPA/PWA -> Google Cloud API Gateway: Sends API requests via [HTTPS / REST & gRPC-Web]
- WebRTC Media Client -> Video Streaming Server (LiveKit SFU): Streams consultations via [WebRTC over UDP with TURN/STUN fallback]
- Data Residency & Consent Router -> Cloud SQL PostgreSQL: Enforces region-locked persistence via [PostgreSQL Wire Protocol / TLS 1.3]

## Technology Stack
- **Client**: Flutter & React (SPA/PWA) for multi-platform UI consistency and offline-first capabilities.
- **Local Storage**: Encrypted SQLite and IndexedDB using AES-256 via Web Crypto API for secure PHI/PII caching.
- **Video**: LiveKit WebRTC SFU on GKE with adaptive bitrate scaling for unstable connections (<300 kbit/s).
- **Cloud Provider**: Google Cloud Platform in regions `europe-west3` and `us-central1`.

## Rationale
This architecture ensures strict GDPR and HIPAA compliance by isolating regional data infrastructure while maintaining high availability and low-bandwidth resilience. Distributed microservices and client-side encryption meet rigorous healthcare security, traceability, and interoperability demands.