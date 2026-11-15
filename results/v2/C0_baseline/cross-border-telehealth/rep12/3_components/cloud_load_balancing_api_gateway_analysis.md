## Overview
[A secure, cloud-native cross-border telehealth platform providing video consultations, e-prescriptions, and an AI symptom checker for EU and US patients. The system ensures strict data residency, privacy compliance, and high availability under unstable network conditions.]

## Key Elements
- Patients, Licensed Clinicians, Pharmacies, Compliance Officers/Auditors
- Global External HTTP(S) Load Balancer (GCP Anycast IP, Cloud Armor)
- API Gateway (Envoy-based)
- Distributed Rate Limiting & Quota Service (Cloud Memorystore for Redis)
- mTLS Termination & Upstream Router (Anthos Service Mesh)
- Video Consultation Service (LiveKit WebRTC SFU on GKE)
- AI Symptom Checker (Python / FastAPI on Cloud Run)
- Consent Management Service, Core Telehealth & E-Prescription, Patient Onboarding & Identity, Billing & Regional Monetization (Spring Boot / Cloud Run on GKE)
- External Systems: EU National E-Prescription Gateways, US Pharmacy Networks, External Identity Providers, Regional Payment Gateways

## Relationships
- Web/Mobile Client Applications -> Global External HTTP(S) Load Balancer: Sends geo-routed client traffic [HTTPS, WebSockets (WSS)]
- Global External HTTP(S) Load Balancer -> API Gateway (Envoy-based): Forwards inspected HTTP/HTTPS and WSS traffic [Internal HTTPS]
- API Gateway (Envoy-based) -> Distributed Rate Limiting & Quota Service: Evaluates traffic quotas and retry legitimacy [gRPC]
- API Gateway (Envoy-based) -> mTLS Termination & Upstream Router: Hands off validated, rate-limited requests [gRPC]
- mTLS Termination & Upstream Router -> Video Consultation Service / AI Symptom Checker / Core Telehealth: Routes backend requests [gRPC over mTLS with SPIFFE/SPIRE]
- Services -> Google Cloud Logging / BigQuery: Ingests sanitized audit logs and metrics [Cloud Pub/Sub, Cloud Logging API]

## Technology Stack
- Google Cloud Platform (GCP): Primary cloud provider spanning `europe-west3` and `us-central1` regions for regional data residency (R-05).
- Google Kubernetes Engine (GKE) & Cloud Run: Container orchestration for microservices and serverless components.
- LiveKit WebRTC SFU: Real-time video consultation engine supporting degraded network modes below 300 kbit/s (R-06).
- Envoy Proxy & Anthos Service Mesh: Edge routing, OAuth2/OIDC validation, and strict mTLS service-to-service communication.
- Cloud Memorystore for Redis: Multi-zone distributed caching supporting localized token-bucket rate limiting.
- Google Cloud KMS & Secret Manager: Cryptographic key management and dynamic mTLS certificate rotation.

## Rationale
[This architecture enforces regional data residency and compliance (GDPR and HIPAA) via GCP regional pinning and edge geo-routing while maintaining strict cryptographic controls. It guarantees high availability and traceability for critical health services through resilient edge routing, localized rate-limiting fallbacks, and W3C distributed tracing.]