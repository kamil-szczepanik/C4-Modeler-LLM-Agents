## Overview
The Cross-Border Telehealth Platform provides secure video consultations, e-prescriptions, and AI symptom checking for patients across the EU and US. The architecture enforces strict regional data residency, regulatory compliance, and resilient access for unstable network connections.

## Key Elements
* Regional GCP API Gateway (`europe-west3`, `us-central1`)
* Auth Interceptor & Token Validator Component
* Request Validator & Schema Validation Component
* Context & Consent Injector Component
* Core Services GKE Clusters with Istio Service Mesh
* Cloud Armor (Rate Limiting & DDoS Protection)
* Cloud Logging with automated log-masking

## Relationships
* Web & Mobile Apps -> Regional GCP API Gateway: HTTPS/WSS with regional DNS routing and TLS 1.3
* Regional GCP API Gateway -> Core Services GKE Clusters: gRPC over mTLS using SPIFFE/SPIRE workload identities
* Regional GCP API Gateway -> Cloud Armor: HTTPS for rate limiting and threat protection

## Technology Stack
* GCP API Gateway / Cloud Endpoints: Regional edge routing and schema validation
* Google Kubernetes Engine (GKE): Regional container orchestration for core backend services
* Istio Service Mesh: Strict mTLS enforcement and service-to-service security
* Cloud IAM & Firebase Auth: Identity verification and JWT/OAuth2 token management
* OpenTelemetry, Cloud Trace & Cloud Logging: End-to-end distributed tracing and audit logging

## Rationale
Regional API gateways guarantee GDPR and HIPAA data residency by isolating EU and US traffic within `europe-west3` and `us-central1`. Edge validation, consent injection, and mTLS ensure high security, low latency, and robust accountability for AI diagnostics and degraded mobile connections.