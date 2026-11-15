## Overview
The Cross-Border Telehealth Platform provides video consultations, e-prescriptions, and an AI symptom checker for patients in the EU and US. It ensures strict data residency, regulatory compliance, and high availability across unstable networks.

## Key Elements
- **Session Cache Component**: Manages authentication tokens and active session states.
- **Distributed Rate Limiter Component**: Enforces API quotas and protects backend services.
- **Pub/Sub Broker Component**: Handles real-time signaling synchronization for video sessions.
- **Idempotency Store Component**: Prevents duplicate e-prescription submissions during retries.
- **Google Cloud Memorystore (Redis)**: Deployed regionally in `europe-west3` and `us-central1` with cross-region replication disabled.

## Relationships
- **Core Telehealth Service** -> **Session Cache Component**: Reads/writes session data via RESP3 over TLS 1.3.
- **API Gateway** -> **Distributed Rate Limiter Component**: Evaluates request rates via RESP3 over TLS 1.3.
- **Media Relay & Signaling Service** -> **Pub/Sub Broker Component**: Publishes signaling events via RESP3 Pub/Sub over TLS 1.3.
- **E-Prescription Integration Service** -> **Idempotency Store Component**: Checks transaction keys via RESP3 over TLS 1.3.

## Technology Stack
- **Google Cloud Memorystore (Redis)**: Provides managed, low-latency in-memory data storage.
- **RESP3 over TLS 1.3**: Secures all internal data transmission and protocol communication.

## Rationale
This architecture ensures strict geographic isolation of health data to comply with GDPR and HIPAA mandates. Furthermore, the component design supports low-latency operations and resilient handling of unstable rural network connections.