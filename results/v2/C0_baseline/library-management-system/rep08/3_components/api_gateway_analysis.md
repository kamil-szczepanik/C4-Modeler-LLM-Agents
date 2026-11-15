## Overview
The Library Management System is a public and academic platform providing item cataloging, circulation management, and self-service portals, adhering strictly to EU data residency. The API Gateway serves as the secure, high-performance edge entry point.

## Key Elements
* API Gateway (Envoy Proxy)
* Edge TLS Terminator & Router Component
* JWT Authentication & RBAC Filter Component
* Request Validation & Versioning Filter Component
* Rate Limiting Filter Component
* Redis Cluster (EU-hosted)
* EU Identity Provider
* Catalog & Search Service (Kotlin / Spring Boot)
* Circulation & Payments Service (Java 17 / Spring Boot)
* Admin & Reporting Service (Python / FastAPI)
* EU-hosted Log & Telemetry Aggregator

## Relationships
* Library Member / Staff / Administrator -> API Gateway: Accesses portals and services via HTTPS (TLS 1.3)
* Edge TLS Terminator -> JWT Authentication Filter: Forwards requests via In-memory
* JWT Authentication Filter -> Request Validation & Versioning Filter: Passes validated claims via In-memory
* Request Validation & Versioning Filter -> Rate Limiting Filter: Evaluates quotas via gRPC
* Rate Limiting Filter -> Backend Services (Catalog, Circulation, Admin): Routes valid traffic via gRPC / mTLS (Istio)
* Envoy Proxy -> EU-hosted Log & Telemetry Aggregator: Exports access logs and traces via OTLP (OpenTelemetry Protocol)

## Technology Stack
* Envoy Proxy: Selected for edge routing, WAF integration, and native filter extensibility
* Envoy native `envoy.filters.http.jwt_authn`: Used for robust, secure JWT validation from the EU Identity Provider
* Redis Cluster: Backs the rate-limiting token bucket algorithm for performance and SLA protection
* Istio Service Mesh: Enforces mTLS and zero-trust security for all internal container communications
* OpenTelemetry (OTLP): Ensures telemetry compliance with EU-only data residency requirements

## Rationale
This architecture uses a decomposed Envoy-based API Gateway to offload cross-cutting security, rate-limiting, and validation concerns at the edge. This design protects backend services, guarantees strict EU data residency compliance, and ensures the search SLA (< 800 ms) under heavy load.