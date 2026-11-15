## Overview
The Cross-Border Telehealth Platform provides video consultations, e-prescriptions, and an AI symptom checker for patients across the EU and US. It enforces strict regional data residency, GDPR/HIPAA compliance, and auditability using Google Cloud Platform.

## Key Elements
- Patients (EU/US) and Licensed Clinicians
- API Gateway (Envoy, Go)
- Edge Route Router, Auth & Token Translation Filter, Consent Enforcement Interceptor, Telemetry & Audit Sidecar
- Identity Providers, Consultation Service, Clinical & Prescription Service, AI Symptom Checker, Consent & Policy Engine
- Immutable Audit Logging Service and Regional Message Broker (GCP Pub/Sub)

## Relationships
- Patients & Clinicians -> API Gateway: Accesses platform services [HTTPS (TLS 1.3), OAuth2/OIDC]
- API Gateway -> Identity Providers: Authenticates users [OAuth2/OIDC]
- API Gateway -> Downstream Microservices: Routes internal traffic [gRPC over mTLS via SPIFFE/SPIRE]
- API Gateway -> Immutable Audit Logging Service: Asynchronously forwards cryptographically verified access logs [gRPC]

## Technology Stack
- Google Cloud Platform (GCP): Target cloud provider utilizing regions `europe-west3` and `us-central1` for data residency compliance
- Envoy Proxy & Go: Core technology for the API Gateway, providing low latency and zero-trust mTLS routing
- OpenTelemetry Collector: Captures distributed traces and request metadata with persistent disk buffering
- OAuth2/OIDC & JWTs: Stateless authentication utilizing short-lived, cryptographically signed tokens with embedded region and consent scopes

## Rationale
This architecture ensures strict regional data residency by deploying regional gateway instances while maintaining low latency for unstable connections. It enforces real-time consent revocation and regulatory accountability through stateless JWTs and asynchronous audit logging.