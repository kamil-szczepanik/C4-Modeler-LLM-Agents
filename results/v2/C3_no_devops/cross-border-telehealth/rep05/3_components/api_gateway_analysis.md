## Overview
The Cross-Border Telehealth Platform provides secure video consultations, e-prescriptions, and an AI symptom checker for patients in the EU and US. The API Gateway manages and routes incoming client traffic regionally while enforcing strict compliance, security, and data residency mandates.

## Key Elements
- Edge Router (Envoy Proxy): Terminates TLS and enforces claims-based geo-routing.
- Auth/Policy Enforcement Filter (Envoy Wasm/Lua Plugin): Validates JWTs, verifies consent scopes, and injects secure headers.
- Rate Limiter & Circuit Breaker: Protects downstream services during unstable connection spikes.
- Telemetry & Usage Analytics Header Injector: Appends anonymized usage metrics without exposing PHI.
- Web Application Firewall (WAF): Inspects inbound HTTPS payloads for OWASP Top 10 vulnerabilities.
- SPIFFE/SPIRE Sidecar Integration: Manages automated short-lived mTLS certificate rotation.

## Relationships
- Client Apps -> Edge Router: Sends API requests and data over HTTPS / WebSockets.
- Edge Router -> Auth/Policy Enforcement Filter: Passes requests for JWT validation and scope verification.
- Auth/Policy Enforcement Filter -> Core Telehealth Service: Routes validated requests via gRPC with mTLS.
- Auth/Policy Enforcement Filter -> AI Symptom Checker Container: Routes symptom check requests via gRPC with mTLS.
- Auth/Policy Enforcement Filter -> Patient Consent Service: Routes consent and compliance queries via gRPC with mTLS.
- Auth/Policy Enforcement Filter -> Pharmacy Integration Gateway: Routes e-prescription requests via gRPC with mTLS.

## Technology Stack
- Google Cloud API Gateway / Envoy: Chosen for native extensibility (Lua/Wasm) and seamless GCP integration.
- SPIFFE/SPIRE: Selected for automated short-lived mTLS certificate rotation and secure service identity.
- gRPC with mTLS: Used for internal service-to-service communication to guarantee transport security.
- TLS 1.3: Enforced externally for maximum perimeter data protection.

## Rationale
This architecture enforces regional isolation and claims-based routing to satisfy strict GDPR and HIPAA data residency requirements. Furthermore, it incorporates robust security controls and telemetry filtering at the edge to protect PHI and maintain service availability for low-bandwidth users.