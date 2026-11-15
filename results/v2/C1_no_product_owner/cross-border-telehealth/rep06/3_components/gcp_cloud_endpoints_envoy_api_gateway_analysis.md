## Overview
The Cross-Border Telehealth Platform provides video consultations, e-prescriptions, and an AI symptom checker for patients across the EU and US. It enforces strict regional data residency and compliance via GCP deployments in `europe-west3` and `us-central1`.

## Key Elements
- Envoy Proxy Core
- JWT/Auth Validation Filter
- Region Routing Module
- Rate Limiting & Throttling Module
- Telemetry & Audit Interceptor

## Relationships
- Clients -> Envoy Proxy Core: Sends requests [HTTPS (JSON/REST) and WSS (WebSockets/QUIC)]
- Envoy Proxy Core -> Rate Limiting Module: Checks limits [Local gRPC]
- Auth Validation Filter -> Telemetry Interceptor: Emits audit events [Internal channel]
- Region Routing Module -> Core Services Container: Routes internal logic [gRPC over mTLS via Anthos Service Mesh]
- Region Routing Module -> AI Symptom Checker Container: Routes AI checks [gRPC over mTLS via Anthos Service Mesh]

## Technology Stack
- GCP Cloud Endpoints / Envoy: Edge API routing, security, and traffic control
- Redis (Memorystore): Token bucket rate limiting for unstable rural connections
- OpenTelemetry & Fluent Bit: Regional distributed tracing and immutable log export without cross-border leaks
- SPIFFE/SPIRE: Automated 24-hour mTLS certificate rotation for zero-trust internal routing

## Rationale
Regionally isolated API Gateways enforce strict data residency for GDPR and HIPAA compliance. Dedicated local telemetry and rate limiting modules ensure reliability and auditability under unstable network conditions.