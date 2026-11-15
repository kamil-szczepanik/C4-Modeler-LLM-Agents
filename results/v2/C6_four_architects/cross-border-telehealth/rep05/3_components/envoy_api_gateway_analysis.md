## Overview
The Cross-Border Telehealth Platform provides video consultations, e-prescriptions, and an AI symptom checker for patients across the EU and US while enforcing strict data residency and compliance. The architecture utilizes Envoy API Gateway components to manage secure routing, policy enforcement, rate limiting, and observability across GCP regions.

## Key Elements
- Listener & TLS Termination Component (Envoy TLS Filter / BoringSSL)
- Routing & Traffic Management Component (Envoy Router Filter)
- External Authorization Filter (Envoy Ext_Authz Filter + Open Policy Agent / OPA)
- Telemetry & Audit Logging Component (Envoy Access Log Service / ALS with OpenTelemetry OTel Filter)
- Rate Limiting & Circuit Breaking Component (Envoy Local/Global Rate Limit Filters & Memorystore for Redis)
- WAF & Threat Mitigation Component (Google Cloud Armor)
- Geo-Routing & Header Enforcement Filter (Envoy Header Mutation & Lua/Wasm Filter)
- Upstream Health Checking & Failover Component (Envoy Active/Passive Health Checking & Outlier Detection)
- Compression & Content Optimization Component (Envoy Compression Filter / Brotli & Gzip)
- mTLS & Upstream TLS Context Component (Envoy Upstream TLS Context / Secret Discovery Service)

## Relationships
- GCP Global HTTPS Load Balancer -> WAF & Threat Mitigation Component: Inspects incoming edge traffic [HTTPS]
- WAF & Threat Mitigation Component -> Listener & TLS Termination Component: Passes sanitized traffic to Envoy [HTTPS]
- Listener & TLS Termination Component -> Geo-Routing & Header Enforcement Filter: Evaluates client context [Internal HTTP]
- Geo-Routing & Header Enforcement Filter -> Routing & Traffic Management Component: Forwards tagged requests to regional upstreams [gRPC]
- Routing & Traffic Management Component -> External Authorization Filter: Queries for permission checks [gRPC]
- Routing & Traffic Management Component -> Rate Limiting Component: Evaluates traffic quotas and client health [gRPC/Internal]
- Rate Limiting Component -> Memorystore for Redis: Fetches distributed token buckets for rate limiting [RESP]
- Routing & Traffic Management Component -> Telemetry & Audit Logging Component: Emits span data and access logs [gRPC over OTel protocol]
- Routing & Traffic Management Component -> Upstream Health Checking Component: Queries endpoint health status [Internal gRPC]
- Upstream Health Checking Component -> Backend Service: Performs active health probes [HTTP/gRPC health checks]
- Routing & Traffic Management Component -> Compression Component: Passes outgoing response streams for encoding [Internal HTTP/2]
- Compression Component -> Listener & TLS Termination Component: Delivers compressed payloads back to the client [HTTPS]
- Routing & Traffic Management Component -> mTLS & Upstream TLS Context Component: Enforces cryptographic tunnel parameters [Internal gRPC]
- mTLS & Upstream TLS Context Component -> Backend Service & Consent & Policy Service: Establishes mutual TLS encrypted connections [gRPC over mTLS]

## Technology Stack
- Envoy Proxy & BoringSSL: Provides edge routing, security, TLS termination, and traffic manipulation.
- Open Policy Agent (OPA) with Ext_Authz: Enforces GDPR, HIPAA, and consent validation at the edge.
- Google Cloud Armor: Filters malicious payloads and provides perimeter security.
- Memorystore for Redis: Stores distributed token buckets for global rate limiting.
- OpenTelemetry (OTel): Propagates W3C Trace Context headers and logs telemetry asynchronously for EU MDR traceability.
- Brotli & Gzip: Compresses dynamic API responses for bandwidth-constrained connections.
- Istio mTLS: Secures service-to-service communication to regional backend microservices.

## Rationale
This architecture ensures strict regional data isolation and compliance (GDPR/HIPAA) through edge-based policy enforcement and geo-routing filters. It maintains high availability and low latency for rural users via compression, rate limiting, and proactive upstream health checking.