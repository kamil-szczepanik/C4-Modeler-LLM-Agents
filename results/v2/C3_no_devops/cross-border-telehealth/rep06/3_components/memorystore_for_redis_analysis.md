## Overview
The Cross-Border Telehealth Platform provides secure video consultations, e-prescriptions, and an AI symptom checker for patients across the EU and US. It enforces strict regional data residency and low-latency session management to support patients with unstable internet connections.

## Key Elements
- Patients and Licensed Clinicians (Users)
- Core Telehealth Service and Regional API Gateways (Containers)
- Session Cache Store and Rate Limiter & Transient Store (Memorystore for Redis components)
- Cloud KMS (Security/Encryption)

## Relationships
- Core Telehealth Service -> Session Cache Store: Caches user tokens and WebRTC signaling state via RESP over TLS 1.3
- Regional API Gateways -> Rate Limiter & Transient Store: Evaluates sliding-window rate limits via RESP over TLS 1.3
- Memorystore instances -> Cloud KMS: Applies region-aligned encryption-at-rest keys within `europe-west3` and `us-central1`

## Technology Stack
- Google Cloud Memorystore for Redis (Redis OSS): Managed in-memory store for session caching and rate-limiting
- RESP over TLS 1.3: Protocol for encrypted communication between services and cache stores
- GCP IAM & VPC Network Peering: Secures private network isolation and authentication
- Cloud KMS: Enforces regional encryption-at-rest for GDPR and HIPAA compliance

## Rationale
Isolated regional Redis deployments ensure that patient health data never crosses EU and US boundaries, satisfying strict GDPR and HIPAA mandates. Low-latency in-memory state management combined with graceful session eviction policies maintains critical video consultation continuity for rural users with unstable internet.