## Overview
The Cross-Border Telehealth Platform provides secure video consultations, e-prescriptions, and an AI symptom checker for EU and US patients. The architecture uses a centralized API Gateway deployed on GCP to handle geographic routing, security, and resiliency.

## Key Elements
- Patients and Licensed Clinicians (External Users)
- API Gateway (Google Cloud Platform, HTTPS/WSS, HTTP/2)
- Consent Enforcement Proxy (gRPC, REST)
- AI Symptom Checker Container (gRPC)
- Regional Databases (Cloud SQL / Spanner in `europe-west3` and `us-central1`)
- Audit Logging & Observability (OpenTelemetry, Structured JSON)

## Relationships
- Patients & Licensed Clinicians -> API Gateway: Client routing, authentication, and TLS termination [HTTPS/WSS, HTTP/2]
- API Gateway -> Consent Enforcement Proxy: Validates explicit user consent tokens for cross-region requests [gRPC/REST]
- API Gateway -> AI Symptom Checker: Forwards requests for urgency recommendations [gRPC]
- API Gateway -> Regional Databases: Processes e-prescriptions and health records locally [SQL over internal VPC]
- API Gateway -> Audit Logging: Emits regional structured access logs [OpenTelemetry / JSON]

## Technology Stack
- Google Cloud Platform (GCP): Target cloud provider utilizing `europe-west3` and `us-central1` regions to meet data residency constraints.
- API Gateway / Edge Proxy: Implements geographic routing, stateless JWT validation, idempotency keys, and RFC 7807 problem details for resilient edge handling.
- OpenTelemetry: Standardizes distributed tracing and context propagation to ensure AI symptom checker accountability.
- gRPC & HTTP/2: Enables low-overhead inter-service communication and multiplexing for unstable rural connections.

## Rationale
This architecture guarantees strict regional data residency (EU data in `europe-west3`, US data in `us-central1`) to satisfy GDPR and HIPAA compliance. Furthermore, edge routing, request validation, and connection draining ensure high availability and graceful degradation for rural users with unstable internet connections.