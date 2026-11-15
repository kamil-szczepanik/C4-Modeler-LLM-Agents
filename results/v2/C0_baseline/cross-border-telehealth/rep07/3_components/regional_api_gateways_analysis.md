## Overview
The Cross-Border Telehealth Platform provides video consultations, e-prescriptions, and an AI symptom checker for patients across the EU and US. It ensures strict data residency and regulatory compliance via isolated regional infrastructure.

## Key Elements
- Global External HTTP(S) Load Balancer: GCP Global Load Balancer routing traffic to regional zones.
- Regional API Gateways: Kong Enterprise deployed on GKE (`europe-west3`, `us-central1`).
- JWT & OAuth2 Validator Component: Validates incoming user tokens from Identity Providers via gRPC/JWKS.
- Cryptographic Consent Verifier Plugin: Custom Lua/Go plugin validating fine-grained consent tokens.
- Rate Limiting & Traffic Prioritization Component: Redis-backed token bucket component ensuring R-03 and R-01 prioritization.
- WAF & Payload Inspection Component: ModSecurity/Coraza integration sanitizing FHIR and JSON payloads.
- Localization & Fault Transformation Component: Translates backend errors into localized, patient-friendly JSON responses.
- Regional Router Component: Forwards validated traffic to internal services.

## Relationships
- Global External HTTP(S) Load Balancers -> Regional API Gateways: Routes traffic to regional deployment zones [HTTPS]
- Regional API Gateways -> Identity Providers: Authenticates users [OAuth2 / OIDC]
- Cryptographic Consent Verifier -> Consent Management Service: Verifies fine-grained permissions [gRPC over mTLS]
- Regional Router -> Consultation Service / AI Inference Orchestrator / Prescription & Interoperability Service: Forwards requests [gRPC over mTLS via SPIFFE/SPIRE]
- Localization & Fault Transformation -> Global External HTTP(S) Load Balancers: Returns localized error responses [HTTPS]

## Technology Stack
- Kong Enterprise: API Gateway core for high-performance routing and custom plugin execution.
- Google Kubernetes Engine (GKE): Container orchestration with ArgoCD for regional drift control.
- Redis / Cloud Memorystore: Distributed caching for rate limiting and cryptographic token replay protection.
- ModSecurity / Coraza: Web Application Firewall (WAF) for payload inspection and sanitization.
- gRPC over mTLS (SPIFFE/SPIRE): Secure, authenticated internal service-to-service communication.

## Rationale
This architecture uses regional Kong API gateways on GKE to strictly enforce GDPR and HIPAA data residency boundaries by keeping EU data in `europe-west3` and US data in `us-central1`. It incorporates Redis-backed traffic shaping, WAF protection, and cryptographic consent verification to guarantee high availability, security, and traceability for critical telehealth workflows.