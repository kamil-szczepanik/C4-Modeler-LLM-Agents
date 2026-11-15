## Overview
The Cross-Border Telehealth Platform provides video consultations, e-prescriptions, and an AI symptom checker for EU and US patients on GCP. It enforces strict regional data residency, GDPR/HIPAA compliance, and auditability.

## Key Elements
* Consent Enforcement Middleware/Proxy Containers: Custom Middleware / Envoy Proxy
* Local Edge Cache: Redis
* External Systems: External Identity and Consent Provider, Regional Audit and Compliance Logging Subsystem
* Downstream Services: Stateless Core Application Containers, Video Streaming Gateway Containers, AI Inference & Audit Proxy Containers

## Relationships
* Client to Consent Middleware: Route requests with JWT tokens [HTTPS / gRPC]
* Consent Middleware to Redis Cache: Perform fast local lookups and cache-aside operations [Redis Protocol]
* Consent Middleware to External Identity Provider: Fallback validation and token retrieval [HTTPS / REST]
* Consent Middleware to Core Containers: Forward requests with enriched metadata headers (`X-Consent-Purpose`, `X-Data-Residency-Region`) [gRPC / HTTP]
* Consent Middleware to Telemetry Subsystem: Emit asynchronous structured audit logs [OpenTelemetry / gRPC]

## Technology Stack
* Envoy Proxy: Provides the ExtAuthz filter and ingress traffic routing
* Redis: Used for local edge caching of consent tokens to reduce latency
* GCP (europe-west3, us-central1): Cloud provider and target regions ensuring data residency compliance
* W3C Trace Context: Used for distributed tracing propagation (`traceparent` headers)

## Rationale
This architecture uses local caching and the ExtAuthz filter to enforce strict default-deny privacy controls without introducing latency bottlenecks during video consultations. Decoupling consent logic via proxies ensures regional data residency and GDPR/HIPAA compliance across cross-border boundaries.