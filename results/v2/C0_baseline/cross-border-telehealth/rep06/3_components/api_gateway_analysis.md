## Overview
[Cross-Border Telehealth Platform providing video consultations, e-prescriptions, and an AI symptom checker for patients in the EU and US. Ensures GDPR and HIPAA compliance while maintaining strict regional data residency.]

## Key Elements
* Patients (EU & US) and Licensed Clinicians
* Regional API Gateways (Envoy) in `europe-west3` and `us-central1`
* Google Cloud Armor WAF
* Core Telehealth, Interoperability, Consent, and AI Orchestrator Services on GKE
* Redis Rate Limiting Store
* OpenTelemetry Collectors

## Relationships
* Patient/Clinician Apps -> Regional API Gateways: HTTPS/WSS (TLS 1.3, OAuth2/OIDC, DPoP token binding)
* Regional API Gateways -> Cloud Armor WAF: Traffic inspection [HTTPS]
* Regional API Gateways -> Downstream GKE Services: gRPC / mTLS via Istio Service Mesh
* Audit & Telemetry Interceptor -> Regional OpenTelemetry Collectors: OTLP / gRPC [Async]

## Technology Stack
* GCP (`europe-west3`, `us-central1`): Target cloud providing regional isolation for data residency compliance
* Envoy: API Gateway technology enabling edge routing, WASM/Lua filters, and compression
* Istio & SPIFFE/SPIRE: Service mesh providing mTLS and secure service-to-service communication
* Redis: Distributed cache supporting rate limiting and quota controls
* OpenTelemetry: Observability framework for distributed tracing and audit logging

## Rationale
[Regional API Gateways isolated in GCP enforce data residency by ensuring EU and US health data never cross boundaries. Asynchronous audit interceptors and rate limiting protect system availability and ensure regulatory traceability without degrading user experience.]