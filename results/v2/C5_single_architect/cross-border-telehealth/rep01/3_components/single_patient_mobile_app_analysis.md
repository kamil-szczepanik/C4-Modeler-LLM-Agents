## Overview
The Cross-Border Telehealth Platform provides video consultations, e-prescriptions, and an AI symptom checker for patients across the EU and US. It ensures strict data residency, regulatory compliance, and resilience for unstable network connections.

## Key Elements
- Single-Patient / Mobile App (Flutter / Dart container)
- UI Layer / Presentation Components
- Local Sync & State Management Component (Hive/SQLite with SQLCipher)
- API Client & Gateway Adapter Component
- WebRTC Client Component (LiveKit SDK)
- Security & Cryptography Component (`flutter_secure_storage`)
- Consent Enforcement Component
- External Systems: API Gateway, Identity Providers (OIDC), LiveKit SFU Media Server

## Relationships
- Single-Patient / Mobile App -> API Gateway: Communicates backend requests [HTTPS/mTLS and gRPC-Web]
- Single-Patient / Mobile App -> LiveKit SFU Media Server: Handles media streams [WebRTC/UDP]
- UI Layer & API Client -> Consent Enforcement Component: Queries consent flags prior to dispatch [Internal Dart Method Calls]
- Local Sync & State Management -> SQLCipher: Secures encrypted local caching [Local I/O]

## Technology Stack
- Flutter (Dart): Cross-platform UI development for mobile client applications.
- SQLCipher & Hive/SQLite: Encrypted local caching to support offline-first operations in rural areas.
- `flutter_secure_storage`: Secure local storage for OAuth tokens and credentials.
- LiveKit SDK: WebRTC client integration for adaptive bitrate streaming and degraded network recovery.

## Rationale
This architecture uses a modular Flutter client with local encryption and state management to guarantee offline resilience and strict privacy compliance. Enforcing client-side consent interception ensures regional data sovereignty before payloads reach the GCP backend.