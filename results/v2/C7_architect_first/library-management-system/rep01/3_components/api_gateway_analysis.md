## Overview
The Library Management System provides cataloging, circulation, and self-service portals for public and academic libraries. The architecture enforces strict EU-only data residency and sub-800ms search latency.

## Key Elements
- **Users**: Library Patrons & Staff
- **External Systems**: CDN / Edge Layer, Identity Provider, External Payment Gateway, National Library Database, Centralized Observability Platform
- **Containers**: Web Application (SPA) (React), API Gateway (Kong), Core Domain Service (Node.js / NestJS), Search Service (Java / Elasticsearch), Database (PostgreSQL), Async Worker (Python / Celery), Telemetry Sidecar / OTEL Collector (OpenTelemetry)
- **API Gateway Components**: Ingress Listener (Kong Proxy), Security & Auth Plugin, Rate-Limiting & Quota Component, Routing & Upstream Balancer, Transform & Error Mapping Component, Telemetry Exporter

## Relationships
- **Web Application (SPA) -> API Gateway**: Sends API requests via [HTTPS/REST with TLS 1.3]
- **API Gateway -> Core Domain Service**: Routes core business requests via [gRPC over mTLS]
- **API Gateway -> Search Service**: Routes search queries via [gRPC over mTLS]
- **API Gateway -> Centralized Observability Platform**: Forwards access logs and metrics via [OTLP]

## Technology Stack
- **API Gateway**: Kong configured as a DB-less Kubernetes Ingress Controller via GitOps (ArgoCD) for EU data residency compliance.
- **Frontend**: React for the Web Application SPA.
- **Backend Services**: Node.js / NestJS (Core Domain) and Java / Elasticsearch (Search Service).
- **Data & Caching**: PostgreSQL for persistence, Redis (high-availability cluster with local caching) for sliding-window rate-limiting.
- **Security & Observability**: OpenTelemetry (OTLP), JWT/OIDC authentication, mTLS, and Coraza WAF.

## Rationale
This decoupled, containerized architecture ensures strict adherence to EU-only data residency through DB-less edge configuration and local JWT caching. The chosen technology stack guarantees high performance, meeting the sub-800ms search latency SLA under peak workloads.