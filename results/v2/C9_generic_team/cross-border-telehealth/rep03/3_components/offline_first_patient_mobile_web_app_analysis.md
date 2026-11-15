## Overview
The Cross-Border Telehealth Platform provides video consultations, e-prescriptions, and an AI symptom checker for patients across the EU and US. It utilizes GCP (`europe-west3`, `us-central1`) with strict data residency, localized encryption, and robust offline synchronization.

## Key Elements
* **Offline-First Patient Mobile/Web App**: Client container featuring local SQLite/IndexedDB, Transactional Outbox, and state machine architecture.
* **API Gateway / Region Router**: Manages multi-region entry points and enforces regional routing constraints.
* **Regional Containers & Services**: GCP regional containers for core logic, WebRTC video, consensus, and traceability logging.
* **Storage & Security Subsystems**: Android Keystore/iOS Keychain for cryptographic envelope encryption and client-side PII redactors.

## Relationships
* **Client App to API Gateway**: Synchronizes state and sends mutation queues with idempotency keys via [REST/gRPC over HTTPS].
* **Client App to Regional Services**: Streams video consultations and syncs clinical payloads using [WebRTC / gRPC].
* **Regional API Gateway to Pub/Sub**: Dispatches asynchronous integration events across regional boundaries using [GCP Pub/Sub].

## Technology Stack
* **Client Storage**: SQLite (mobile) and IndexedDB (web) for resilient local-first persistence during offline periods.
* **Serialization & Protocol**: Protocol Buffers for compact binary payload compression over low-bandwidth links.
* **Security**: Client-side cryptographic envelope pattern backed by Android Keystore and iOS Keychain for data-at-rest protection.
* **Network Resilience**: Service Workers with stale-while-revalidate strategies, circuit breakers, and Token Bucket rate limiting.

## Rationale
This architecture ensures strict GDPR and HIPAA data residency compliance by anchoring regional payloads locally and encrypting data at rest via hardware-backed enclaves. Furthermore, the local-first outbox pattern, binary serialization, and finite state machines guarantee high availability and fault tolerance for patients in unstable rural environments.