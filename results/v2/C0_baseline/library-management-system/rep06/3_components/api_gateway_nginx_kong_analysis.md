## Overview
The Library Management System is a comprehensive platform for public and academic libraries to catalogue items, manage circulation, and provide self-service portals. It leverages a secure, high-performance API Gateway architecture to meet strict EU-only data residency and sub-800ms search response requirements.

## Key Elements
- **API Gateway (Nginx / Kong):** Central perimeter container managing routing, rate limiting, and security.
- **SSL/TLS Termination & Routing Engine (Nginx core):** Handles ingress traffic and internal gRPC/mTLS dispatch.
- **Auth & Security Plugin:** Validates JWTs, enforces RBAC, and interacts with the Identity Provider (IdP).
- **Rate Limiting & Throttling Filter:** Protects backend services and enforces request quotas.
- **Telemetry & Audit Interceptor:** Injects W3C Trace Context headers to the OpenTelemetry Collector.
- **Redis Cache (Local/Cluster):** Caches JWT tokens and session data via RESP over TLS.
- **External Services:** Identity Provider (IdP), Catalogue & Search Service, and Circulation Service.

## Relationships
- **Web Application (SPA) -> SSL/TLS Termination & Routing Engine:** Client requests via HTTPS [TLS 1.3]
- **Auth & Security Plugin -> Identity Provider (IdP):** Token validation and introspection via HTTPS/OIDC
- **SSL/TLS Termination & Routing Engine -> Catalogue & Search Service:** Internal routing via gRPC over mTLS
- **SSL/TLS Termination & Routing Engine -> Circulation Service:** Internal routing via gRPC over mTLS
- **Auth & Security Plugin -> Redis Cache:** Token and session verification via RESP over TLS

## Technology Stack
- **API Gateway:** Nginx / Kong deployed on a multi-AZ Kubernetes cluster with HPA for scalability.
- **Protocols:** HTTPS (TLS 1.3) for external traffic, gRPC over mTLS for internal microservices, and RESP over TLS for caching.
- **Security & Observability:** OAuth 2.0 / OIDC for authentication, JWT with RBAC, OpenTelemetry for tracing, and Prometheus for metrics.

## Rationale
This architecture ensures strict EU-only data residency compliance by enforcing perimeter security and geo-routing within the EU. Centralizing JWT validation, rate-limiting, and mTLS at the API Gateway safeguards backend microservices and guarantees the 99th-percentile search response SLA under 800ms.