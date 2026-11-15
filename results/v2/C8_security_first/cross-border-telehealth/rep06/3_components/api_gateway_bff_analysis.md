## Overview
The Cross-Border Telehealth Platform provides secure video consultations, e-prescriptions, and an AI symptom checker for patients in the EU and US. It enforces strict regional data residency, GDPR/HIPAA compliance, and low-bandwidth resilience for rural users.

## Key Elements
- Patients (EU and US)
- Licensed Clinicians
- API Gateway & BFF (Go, Envoy Proxy)
- Geo-Enforcement & Routing Proxy (Envoy Proxy)
- Consent & Auth Middleware (Go)
- BFF Aggregator & Transformer (Go)
- Telemetry & Resilience Interceptor (Go)
- Downstream Containers: Video Consultation Container (MediaSoup), E-Prescription Integration Container (Node.js), AI Symptom Checker Container (Python)
- External Identity Providers (OAuth2/OIDC)
- Cloud SQL (PostgreSQL)
- Google Kubernetes Engine (GKE)

## Relationships
- Patients & Clinicians -> API Gateway & BFF: Accesses telehealth services [HTTPS / WebSocket over TLS 1.3]
- API Gateway & BFF -> External Identity Providers (OAuth2/OIDC): Validates user authentication tokens [OAuth2 / OIDC]
- API Gateway & BFF -> Cloud SQL (PostgreSQL): Caches user consent policies [mTLS / TCP]
- BFF Aggregator & Transformer -> AI Symptom Checker Container: Routes symptom check requests [gRPC over mTLS with W3C Trace Context]
- API Gateway & BFF -> E-Prescription Integration Container: Routes prescription data [mTLS over gRPC/REST]
- API Gateway & BFF -> Video Consultation Container: Routes session management [mTLS over gRPC/REST]

## Technology Stack
- Google Cloud Platform (GCP): Target cloud utilizing `europe-west3` and `us-central1` for strict data residency.
- Google Kubernetes Engine (GKE): Container orchestration with Horizontal Pod Autoscalers (HPA) and Argo Rollouts for progressive delivery.
- Envoy Proxy: Edge termination, TLS 1.3, regional geo-routing, rate limiting, and connection resilience.
- Go (Golang): Implementation language for Consent & Auth Middleware, BFF Aggregator, and Telemetry Interceptor.
- PASETO: Cryptographically signed internal headers for zero-trust context propagation.
- W3C Trace Context: Distributed tracing standard for monitoring rural network latencies.

## Rationale
Regional API Gateway deployments physically isolate EU and US health data to satisfy strict GDPR and HIPAA mandates. Built-in payload compression, circuit breaking, and telemetry ensure high availability and graceful degradation for rural patients on unstable connections.