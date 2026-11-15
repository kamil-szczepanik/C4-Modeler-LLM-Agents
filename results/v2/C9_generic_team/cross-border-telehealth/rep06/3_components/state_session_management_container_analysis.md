## Overview
The Cross-Border Telehealth Platform provides video consultations, e-prescriptions, and an AI symptom checker for patients in the EU and US. It enforces strict regional data residency and high availability under unstable network conditions.

## Key Elements
- Patients and Licensed Clinicians
- API Gateway / Edge Proxy Container (GCP Cloud Load Balancing / Envoy)
- State & Session Management Container (Redis / GCP Memorystore)
- Integration & Translation Container (Node.js / GCP Cloud Run)
- Config & Feature Management Container (GCP Cloud Config)
- Audit & Traceability Logging Container (GCP Pub/Sub / Cloud Logging)
- Identity & Access Management (IAM) Container (OAuth2 / OpenID Connect / JWTs)
- Health & Resilience Monitoring Container (GCP Cloud Monitoring / Prometheus)
- Secrets & Certificate Management Container (GCP Secret Manager)
- Data Persistence Container (Cloud SQL / Spanner)

## Relationships
- API Gateway / Edge Proxy Container -> State & Session Management Container: Manages user sessions [gRPC over mTLS]
- State & Session Management Container -> GCP Memorystore (europe-west3 / us-central1): Persists regional session state [Redis Protocol]
- API Gateway / Edge Proxy Container -> Integration & Translation Container: Routes API traffic and translation [HTTP/2]

## Technology Stack
- GCP Memorystore (Redis): Regional in-memory data store for low-latency session persistence and pub/sub messaging.
- GCP Cloud Run (Node.js): Serverless execution for integration and translation containers.
- OpenTelemetry: Distributed tracing propagation for cross-service observability without exposing PHI/PII.
- GCP Secret Manager & CMEK: Key-level encryption ensuring regional data compliance (GDPR/HIPAA).

## Rationale
The architecture guarantees GDPR and HIPAA compliance by strictly segregating EU and US regional deployments on GCP. It maintains high availability for rural patients on unstable connections via heartbeat leases, token bucket rate limiting, and bulkhead patterns.