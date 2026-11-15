## Overview
The system is a multi-region cross-border telehealth platform providing video consultations, e-prescriptions, and an AI symptom checker for EU and US patients. Its core purpose is delivering secure, compliant telehealth services while enforcing strict regional data isolation.

## Key Elements
- Envoy Proxy
- Region-Isolated API Gateways and Backend Services
- Regional Memorystore for Redis
- Cloud SQL Auth Proxy
- GCP Pub/Sub Integration Bus
- OpenTelemetry Observability Agents

## Relationships
- Patients and Licensed Clinicians -> Envoy Proxy: Interacts via HTTPS
- Envoy Proxy -> Backend Services: Routes requests via gRPC/REST with schema validation
- Backend Services -> Regional Memorystore for Redis: Tracks idempotency keys and rate limits via internal TCP
- Backend Services -> Cloud SQL Auth Proxy: Connects to regional databases via TCP
- Backend Services -> GCP Pub/Sub Integration Bus: Publishes events via GCP Pub/Sub

## Technology Stack
- Envoy Proxy: Selected for edge routing, circuit breaking, rate limiting, and schema validation.
- GCP Memorystore (Redis): Chosen for low-latency, region-isolated idempotency and rate-limiting storage.
- OpenTelemetry: Implemented for distributed tracing and compliance logging.
- OpenAPI / Protobuf: Used for strict API contracts and automated schema validation.

## Rationale
This architecture isolates data regionally in `europe-west3` and `us-central1` to satisfy GDPR and HIPAA compliance. It also guarantees high availability and idempotency for rural users with unstable connections.