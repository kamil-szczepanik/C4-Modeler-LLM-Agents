## Overview
The Core Services API is a Java/Spring Boot container that orchestrates library transactions, circulation management, and integration with external digital providers. It provides secure, low-latency business logic for patrons and staff while enforcing strict EU-only data residency requirements.

## Key Elements
- Core Services API (Java/Spring Boot container)
- Circulation Management Component
- Patron Account Component
- Integration Orchestrator Component
- Database (PostgreSQL with EU hosting)
- API Gateway (Envoy/Kong)
- Notification Gateway
- Digital Content Providers
- Observability & Logging Platform (Prometheus/Grafana)

## Relationships
- API Gateway -> Core Services API: Routes core requests [gRPC over mTLS with OAuth2 metadata headers]
- Circulation Management Component -> Database: Persists loans and audit events [PostgreSQL Wire Protocol over TLS 1.3]
- Patron Account Component -> Database: Validates memberships [PostgreSQL Wire Protocol over TLS 1.3]
- Integration Orchestrator Component -> Notification Gateway: Dispatches alerts [Asynchronous HTTPS/REST webhooks over TLS 1.3]
- Integration Orchestrator Component -> Digital Content Providers: Brokers external licensing [HTTPS/REST with mutual TLS]
- Core Services API -> Observability & Logging Platform: Emits sanitized distributed traces [OpenTelemetry over gRPC / TLS 1.3]

## Technology Stack
- Java/Spring Boot: Provides a robust framework for modular monolith decomposition and enterprise business logic.
- PostgreSQL with EU Hosting: Ensures persistent relational storage compliant with EU-only data residency mandates.
- gRPC over mTLS: Delivers high-performance, secure internal communication between the API Gateway and Core Services API.
- Resilience4j: Implements circuit breaking to isolate volatile external digital content vendors.
- OpenTelemetry: Captures distributed tracing to satisfy performance SLAs under load.

## Rationale
This modular architecture isolates volatile external dependencies to prevent thread pool exhaustion while maintaining strict transactional integrity. It guarantees high performance, secure token propagation, and strict adherence to EU data residency mandates.