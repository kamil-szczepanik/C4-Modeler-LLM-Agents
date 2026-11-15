## Overview
The Library Management System is a public and academic platform providing cataloging, circulation, and self-service portals. It uses a Kong/NGINX API Gateway container to secure, route, and observe frontend traffic.

## Key Elements
- **API Gateway (Kong)**: Edge container handling ingress, routing, and security.
- **TLS Termination & SSL/TLS Certificate Manager**: Handles inbound HTTPS traffic.
- **Authentication Plugin (JWT/OAuth2 Validator)**: Validates tokens against the Third-Party Identity Provider.
- **Rate Limiting & ACL Plugin**: Enforces persona-based quotas for Patrons and Clerks.
- **Upstream Proxy & Circuit Breaker**: Routes to the Core API with health checks.
- **Telemetry & Log Exporter**: Exports Prometheus metrics and streams scrubbed logs.
- **Error Transformer Plugin**: Outputs standardized, localized error payloads.

## Relationships
- Self-Service Portal & Staff Dashboard -> TLS Termination: HTTPS/TLS
- Authentication Plugin -> Third-Party Identity Provider: OIDC/JWKS [HTTPS]
- Upstream Proxy & Circuit Breaker -> Core API Application: HTTP/REST [HTTPS]
- Telemetry & Log Exporter -> APM and Synthetic Monitoring Tool: Prometheus [HTTPS]
- Telemetry & Log Exporter -> Centralized Log/Audit Aggregator: Syslog/Fluentd [HTTPS]

## Technology Stack
- **Kong/NGINX**: Selected as the API Gateway container for edge routing, rate limiting, and plugin extensibility.
- **Prometheus**: Used for metrics exporting to meet observability requirements.
- **Fluentd/Syslog**: Used for asynchronous log shipping while enforcing EU data residency.
- **Kubernetes**: Multi-zone deployment platform utilizing Horizontal Pod Autoscalers.

## Rationale
This architecture ensures secure, low-latency request routing and strict compliance with EU data residency constraints. Edge-level authentication, rate-limiting, and circuit-breaking protect backend systems to support high-performance search SLAs under 800 ms.