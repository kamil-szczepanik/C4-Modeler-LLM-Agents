## Overview
The Cross-Border Telehealth Platform provides secure video consultations, e-prescriptions, and an AI symptom checker for patients across the EU and US. The architecture enforces strict regional data residency on Google Cloud Platform while ensuring high availability for unstable rural connections.

## Key Elements
* Patients and Clinicians (Users)
* Stateless Core Application Containers (Containerized Microservices on GCP)
* Consent Enforcement Middleware/Proxy Containers (Custom Middleware / Envoy Proxy)
* External Identity and Consent Provider (OIDC)
* Regional Adapters (FHIR Translation Adapter for US, National E-Prescription Adapter for EU)
* AI Inference & Audit Proxy Containers (Python / gRPC)
* Regional Audit and Compliance Logging Subsystem

## Relationships
* Stateless Core Application Containers -> Consent Enforcement Middleware/Proxy Containers: Route traffic via gRPC/REST
* Stateless Core Application Containers -> External Identity and Consent Provider: Authenticate and verify consent using OpenID Connect (OIDC)
* Stateless Core Application Containers -> Regional Adapters: Transmit health data using HL7 FHIR (US) or National APIs (EU)
* Stateless Core Application Containers -> Regional Audit and Compliance Logging Subsystem: Log inputs, model versions, and consent tokens via OpenTelemetry

## Technology Stack
* Google Cloud Platform (`europe-west3`, `us-central1`): Core hosting environment ensuring data residency compliance.
* Envoy Proxy / Custom Middleware: Enforces zero-trust mTLS, fail-closed security, and consent checks.
* OpenTelemetry: Powers distributed tracing, telemetry export, and strict PII/PHI log redaction.
* OpenAPI / JSON Schema: Enforces payload sanitization, size limiting, and RFC 7807 problem details.

## Rationale
Strict region-bound container deployments and fail-closed security ensure uncompromised GDPR and HIPAA compliance without cross-border data leakage. Idempotent APIs, circuit breakers, and graceful shutdowns (`SIGTERM`) maintain resilient, degraded-mode availability for rural patients on unstable connections.