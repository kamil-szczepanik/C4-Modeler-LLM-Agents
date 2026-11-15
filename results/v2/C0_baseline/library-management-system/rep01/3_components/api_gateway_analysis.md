## Overview
The system is an EU-compliant Library Management System providing cataloging, circulation, and self-service portals for academic and public libraries. Its core purpose is secure, high-performance item management with a strict <800ms search SLA.

## Key Elements
- **Users**: Library Patrons, Librarians, Library Administrators
- **API Gateway Container**: Kong/Nginx reverse proxy enforcing routing, rate limiting, and security boundaries
- **API Gateway Components**: WAF & Threat Protection (Coraza), JWT Validator, Access Control (ACL), Rate Limiting, Routing & Load Balancer
- **Data & Caching**: Distributed Redis Cluster (Multi-AZ, EU-only)
- **Downstream Services**: Catalog & Search Service, Circulation & Core Service, Notification Dispatcher, Audit Logging
- **External Systems**: External Identity Provider, Payment Gateway, Notification Service, Observability Platform

## Relationships
- Frontend Container -> API Gateway: Sends user requests [HTTPS / REST APIs]
- API Gateway (WAF) -> API Gateway (JWT Validator): Evaluates sanitized payloads [Internal Routing]
- API Gateway (JWT Validator) -> External Identity Provider: Validates token signatures [HTTPS / OIDC]
- API Gateway (Rate Limiting) -> Redis Cluster: Tracks distributed rate-limit counters [TCP / RESP over TLS]
- API Gateway -> Catalog & Search Service: Routes search queries [gRPC over mTLS]
- API Gateway -> Circulation & Core Service: Routes transactions [gRPC over mTLS]
- API Gateway -> Observability Platform: Streams logs and distributed traces [Fluentbit / W3C Trace Context]

## Technology Stack
- **API Gateway**: Kong / Nginx with Lua plugins for low-latency ingress control
- **WAF**: Coraza / ModSecurity plugin with OWASP Core Rule Set for injection defense
- **Caching & Rate Limiting**: Redis Cluster for distributed, sub-5ms counter tracking
- **Communication Protocols**: gRPC over mTLS for internal services; HTTPS/REST and RESP over TLS externally
- **Deployment & Scaling**: Kubernetes with KEDA-driven HPA and Blue-Green deployment strategy

## Rationale
This architecture uses an optimized Kong API Gateway with Redis caching to meet the <800ms search SLA while enforcing security and EU data residency constraints. Strict mTLS, localized JWT validation, and WAF protection safeguard patron data against breaches and traffic spikes.