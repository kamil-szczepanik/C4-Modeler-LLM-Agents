## Overview
The Patron BFF (Backend-for-Frontend) is a containerized microservice that serves public and academic library patrons, providing an aggregated, secure, and resilient interface for self-service portals. It ensures fast search discovery, personal loan management, and strict EU data residency compliance.

## Key Elements
* Library Patrons (Students, Researchers, Public)
* API Gateway / Ingress (Traefik or Envoy)
* Patron BFF Container (NestJS/TypeScript)
* Catalogue & Search Service Container (Java / Elasticsearch)
* Circulation & Loan Service Container (Spring Boot)
* Notification Dispatcher Container (Go / Temporal)
* Redis (EU-hosted, Session Cache)
* External Identity Provider (IdP)

## Relationships
* Library Patrons -> API Gateway / Ingress: Accesses portal [HTTPS]
* API Gateway / Ingress -> Patron BFF Container: Routes patron traffic [HTTP]
* Patron BFF Container (GraphQL/REST API Layer) -> External Identity Provider: Token validation and exchange [HTTPS]
* Patron BFF Container -> Catalogue & Search Service Container: Queries catalogue and search [gRPC over mTLS]
* Patron BFF Container -> Circulation & Loan Service Container: Fetches active loans and holds [gRPC over mTLS]
* Patron BFF Container -> Notification Dispatcher Container: Triggers asynchronous patron notices [gRPC over mTLS]
* Patron BFF Container -> Redis: Manages distributed patron session caching [RESP over TLS, EU-hosted]

## Technology Stack
* **NestJS (TypeScript)**: Chosen for modular architecture, dependency injection, and native support for pipes, guards, and interceptors.
* **GraphQL / REST**: Exposes optimized endpoints for UI clients to aggregate data in a single round-trip, supporting the <800 ms search performance requirement (R-05).
* **gRPC over mTLS**: Ensures high-performance, secure inter-container communication.
* **Kubernetes**: Deployed in EU-region clusters with Horizontal Pod Autoscalers (HPA) and Kubernetes Secrets CSI drivers for EU data residency and scaling.
* **OpenTelemetry**: Used for distributed tracing to isolate latency bottlenecks.

## Rationale
This architecture uses NestJS and GraphQL aggregation behind an API Gateway to meet strict performance SLAs (<800 ms search response) while enforcing EU-only data residency. Circuit breakers, JWT/ABAC middleware, and Redis session caching ensure high availability and robust security for 24/7 academic self-service portals.