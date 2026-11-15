## Overview
The Cross-Border Telehealth Platform provides secure video consultations, e-prescriptions, and an AI symptom checker for patients across the EU and US. The API Gateway Container enforces regional data residency, consent management, and rural network resilience at the perimeter.

## Key Elements
- API Gateway Container (Istio Service Mesh, Consent Management, ABAC, OAuth2/OIDC JWT)
- Regional GKE Clusters (`europe-west3`, `us-central1`)
- WebRTC SFU Media Servers
- AI Symptom Checker Container
- GCP Cloud Armor and Cloud CDN
- Localized Redis Token Blacklist Cache

## Relationships
- GCP Cloud Armor and Cloud CDN -> API Gateway Container: Routes inspected and cached edge traffic via HTTPS and Istio mTLS
- API Gateway Container -> WebRTC SFU Media Servers: Connects authenticated users for video consultations via WebRTC and Istio mTLS
- API Gateway Container -> AI Symptom Checker Container: Routes symptom checking requests via Istio mTLS
- API Gateway Container -> Localized Redis Cache: Validates token blacklists and consent scopes with sub-second latency

## Technology Stack
- Google Kubernetes Engine (GKE): Regional container orchestration for isolated `europe-west3` and `us-central1` deployments
- Istio Service Mesh: Manages mTLS, traffic routing, circuit breaking, and liveness probes
- OAuth2/OIDC with DPoP/MTLS: Secures user authentication and token binding
- Redis: Provides low-latency caching for dynamic JWT revocation and consent states
- OpenTelemetry & W3C Trace Context: Enforces distributed tracing and audit logging

## Rationale
This architecture ensures strict GDPR and HIPAA data residency compliance by isolating traffic regionally at the API Gateway perimeter. It guarantees rural accessibility and high availability through payload compression, graceful stream draining, and token-bucket rate limiting.