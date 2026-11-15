## Overview
The Cross-Border Telehealth Platform provides video consultations, e-prescriptions, and an AI symptom checker for patients across the EU and US. It ensures strict data residency, regulatory compliance, and robust connectivity for rural users.

## Key Elements
- **Patients & Clinicians**: End users accessing telehealth services.
- **Web/Mobile Frontend App**: Flutter/React client application.
- **API Gateway**: Envoy/GCP API Gateway container comprising:
  - Authentication & Authorization Filter (Envoy Authz/Lua)
  - Region Routing Router (Envoy Route Configuration)
  - Rate Limiting & Resilience Component (Envoy Rate Limit Service)
  - Audit & Telemetry Interceptor (Envoy Access Log Service)
- **Core Telehealth Service**: Go/Spring Boot backend for platform logic.
- **AI Inference Service**: Python/FastAPI service for symptom checking.
- **Regional Data Stores**: GCP Cloud SQL/Spanner deployed in `europe-west3` and `us-central1`.

## Relationships
- **Web/Mobile Frontend App -> Authentication & Authorization Filter**: Sends requests with bearer tokens [HTTPS and WSS]
- **Authentication & Authorization Filter -> Region Routing Router**: Forwards validated requests internally [gRPC]
- **Region Routing Router -> Core Telehealth Service & AI Inference Service**: Routes traffic regionally [gRPC over mTLS]
- **Region Routing Router -> Audit & Telemetry Interceptor**: Emits request traces and audit events [gRPC]
- **Audit & Telemetry Interceptor -> Regional Data Stores**: Persists compliance logs regionally [gRPC]

## Technology Stack
- **GCP (`europe-west3`, `us-central1`)**: Target cloud infrastructure ensuring regional data isolation.
- **Envoy / GCP API Gateway**: Handles edge routing, security filters, and resilience.
- **gRPC / mTLS**: Provides high-performance, secure internal service communication.
- **HTTPS and WSS**: Secures client-facing transport channels.

## Rationale
This architecture enforces GDPR and HIPAA compliance by routing and storing regional health data strictly within GCP `europe-west3` and `us-central1`. Envoy-based gateway routing, robust rate-limiting, and distributed tracing ensure traceability for medical AI and resilience for unstable rural connections.