## Overview
The Library Management System provides item cataloguing, circulation management, and self-service portals for public and academic libraries. It ensures EU data residency compliance while delivering high-performance search capabilities.

## Key Elements
- Library Patrons, Library Staff, Library Administrators
- API Gateway Container (Kubernetes, Envoy/Istio, TLS 1.3)
- Patron Self-Service Portal Container, Staff Circulation & Cataloguing Container, Admin & Reporting Container, Notification Service Container
- External Identity Provider (IdP)
- EU Cloud Infrastructure Boundary
- In-Region APM and Log Aggregation Pipeline
- Audit and Compliance Trust Zone

## Relationships
- Library Patrons / Staff / Administrators -> API Gateway Container: Accesses services via HTTPS [TLS 1.3]
- API Gateway Container -> External Identity Provider (IdP): Validates OAuth2/OIDC tokens and fetches JWKS [OAuth2/OIDC]
- API Gateway Container -> Patron Self-Service Portal / Staff Circulation / Admin / Notification Containers: Routes traffic securely [mTLS over Kubernetes network policies]
- API Gateway Container -> In-Region APM and Log Aggregation Pipeline: Streams logs and OpenTelemetry metrics [Asynchronous sidecar collection]

## Technology Stack
- Kubernetes & Argo Rollouts: Container orchestration and zero-downtime canary deployments ensuring high availability.
- Istio / Envoy Service Mesh: Handles mTLS, circuit breaking, and Envoy-level rate limiting.
- Redis: Backs distributed rate-limiting tiers within the EU region.
- OAuth2/OIDC & JWT: Manages ingress authentication with local caching for low latency.
- TLS 1.3: Enforces modern transport-layer security exclusively.

## Rationale
This architecture uses local JWT validation, Redis-backed rate limiting, and sidecar telemetry to maintain sub-second search responses (< 800 ms) while strictly enforcing EU data residency. Envoy-based circuit breaking and zero-downtime deployments ensure operational resilience for peak academic usage.