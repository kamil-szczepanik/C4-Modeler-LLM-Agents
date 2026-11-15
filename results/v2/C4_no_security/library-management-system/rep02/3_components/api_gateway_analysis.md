## Overview
The Library Management System provides cataloging, circulation, and self-service portals for public and academic libraries. Its API Gateway handles edge routing, security, and traffic management while strictly enforcing EU data residency constraints.

## Key Elements
- **API Gateway**: Kong / Nginx deployed across multi-AZs with active-active scaling
- **Clients**: Patron Web/Mobile App (React / React Native), Staff Dashboard (Angular), Self-Service Kiosk (Electron / React)
- **Backend Services**: Core Domain Services (Java / Spring Boot), Search Engine (Elasticsearch)
- **Infrastructure & Storage**: Redis (rate limiting), Apache Kafka, Observability Stack (OpenTelemetry, Prometheus, Grafana), EU-Resident Log & Audit Sink, Fluentbit sidecar

## Relationships
- Patron Web/Mobile App -> API Gateway: Routes requests [HTTPS]
- Staff Dashboard -> API Gateway: Routes requests [HTTPS]
- Self-Service Kiosk -> API Gateway: Routes requests [HTTPS]
- API Gateway -> Core Domain Services: Routes traffic & versioned requests [gRPC / HTTPS]
- API Gateway -> Search Engine: Routes search queries [gRPC / HTTPS]
- API Gateway -> Observability Stack & Audit Sink: Forwards scrubbed metrics, traces, and logs [OpenTelemetry / Fluentbit]

## Technology Stack
- **Kong / Nginx**: API Gateway for reverse proxying, TLS/mTLS termination, and header/path-based API versioning
- **Kong OAuth2 Plugin**: Token validation and authentication at the edge
- **Redis**: Backend state store for Kong Rate Limiting Plugin to enforce dynamic request throttling
- **OpenTelemetry & Fluentbit**: Standardized telemetry collection, log scrubbing for PII, and sidecar buffering
- **Java / Spring Boot & Elasticsearch**: Core backend and search infrastructure to maintain <800ms search SLA

## Rationale
This architecture centralizes edge security and dynamic throttling to protect backend services from peak loads, directly supporting the 99th-percentile search response time under 800 ms. Additionally, strict localized telemetry routing and PII log scrubbing guarantee absolute compliance with EU-only data residency requirements.