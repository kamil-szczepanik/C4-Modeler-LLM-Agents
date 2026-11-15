## Overview
The Cross-Border Telehealth Platform provides secure video consultations, e-prescriptions, and an AI symptom checker for patients across the EU and US. The architecture enforces strict regional data residency and compliance via dedicated, stateless regional API gateways.

## Key Elements
* Patients (EU and US) and Licensed Clinicians
* External Pharmacies and Regional Payment Gateways
* `EU API Gateway` (Envoy / GCP Cloud Endpoints in `europe-west3`)
* `US API Gateway` (Envoy / GCP Cloud Endpoints in `us-central1`)
* Regional Memorystore (Redis) for Idempotency
* IAM & Consent Service
* Core Services Container and AI Symptom Checker Container
* Istio Service Mesh

## Relationships
* Web & Mobile App -> API Gateway: Sends API requests and mutations over [HTTPS/TLS 1.3]
* API Gateway -> Regional Memorystore: Checks request deduplication via [Redis Protocol / TLS with connection pooling]
* API Gateway -> Core Services / AI Symptom Checker / IAM: Routes valid requests via [gRPC with mTLS via Istio]
* API Gateway -> Audit Sinks: Exports compliance and consent telemetry asynchronously

## Technology Stack
* Envoy / GCP Cloud Endpoints: Perimeter routing, TLS 1.3 termination, rate limiting, and circuit breaking
* GCP Cloud Memorystore (Redis): Regional idempotency cache preserving stateless gateway design
* Istio Service Mesh: Internal mTLS communication, canary deployments, and traffic shedding
* OAuth2 / OIDC: Token-based authentication embedding consent scopes for local gateway validation
* OpenTelemetry: Distributed tracing and structured access logging routed to region-locked audit sinks

## Rationale
Decomposing the API Gateway into region-specific, stateless instances guarantees that health data residency is strictly enforced within `europe-west3` and `us-central1` per GDPR and HIPAA. Incorporating local JWT consent validation, rate limiting, and Redis idempotency protects rural mobile users from retry storms while maintaining high availability and security.