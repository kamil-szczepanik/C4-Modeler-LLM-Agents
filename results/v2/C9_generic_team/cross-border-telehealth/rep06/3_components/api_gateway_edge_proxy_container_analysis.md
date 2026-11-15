## Overview
Cross-Border Telehealth Platform providing video consultations, e-prescriptions, and an AI symptom checker for patients in the EU and US. It ensures regional data residency and compliance with GDPR, HIPAA, and EU MDR.

## Key Elements
- Patients and Licensed Clinicians
- API Gateway / Edge Proxy Container (GCP Cloud Load Balancing / Envoy)
- Integration & Translation Container (Node.js / GCP Cloud Run)
- State & Session Management Container (Redis / GCP Memorystore)
- Identity & Access Management (IAM) Container (OAuth2 / OpenID Connect / JWTs)
- Audit & Traceability Logging Container (GCP Pub/Sub / Cloud Logging)
- Data Persistence Container (Cloud SQL / Spanner)

## Relationships
- Patients and Licensed Clinicians -> API Gateway / Edge Proxy Container: Access telehealth services [HTTPS and WebRTC with HTTP/3]
- API Gateway / Edge Proxy Container -> Integration & Translation Container: Routes business logic requests [gRPC over mTLS with `X-Data-Region` header]
- API Gateway / Edge Proxy Container -> State & Session Management Container: Manages sessions and rate limits [gRPC over mTLS]
- API Gateway / Edge Proxy Container -> Identity & Access Management (IAM) Container: Validates tokens [gRPC over mTLS, JWT]
- API Gateway / Edge Proxy Container -> Audit & Traceability Logging Container: Transmits trace logs [GCP Pub/Sub]

## Technology Stack
- GCP Cloud Load Balancing & Envoy: Edge routing, HTTP/3, SNI inspection, and geo-based traffic steering to enforce data residency.
- GCP Cloud Run (Node.js): Scalable hosting for integration and business logic containers.
- GCP Memorystore (Redis): Distributed session storage and backing for gateway-level rate limiting.
- WebRTC: Adaptive bandwidth video consultations for rural, low-bandwidth connections.
- W3C Trace Context: Distributed tracing and request correlation for auditability.

## Rationale
The architecture enforces strict regional data boundaries via GCP edge routing while utilizing HTTP/3 and WebRTC to maintain resilient, low-bandwidth connections for rural users. Decoupling the API gateway from direct persistence layers ensures high security, scalability, and strict adherence to healthcare compliance frameworks.