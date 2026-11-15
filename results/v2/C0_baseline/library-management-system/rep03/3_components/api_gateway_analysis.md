## Overview
The API Gateway manages, secures, and routes all incoming ingress traffic for the Library Management System. It enforces rate-limiting, geo-compliance, caching, and authentication to ensure high-performance public and staff portals.

## Key Elements
- Routing & Load Balancing Engine (Envoy C++ Core)
- Authentication & Authorization Filter (Envoy WASM/Lua Plugin)
- Rate Limiting & Traffic Shaping Module (Envoy Rate Limit Service)
- Caching & Response Compression Component (Envoy HTTP Cache Filter)
- Response Transformation Component (Envoy Transformation Filter)
- Ingress Kubernetes Deployment across multiple Availability Zones

## Relationships
- Patron Portal & Staff Dashboard -> Authentication & Authorization Filter: Validates incoming requests [HTTPS (TLS 1.3)]
- Routing & Load Balancing Engine -> Core Business Service & Search Service: Forwards upstream traffic [gRPC/mTLS (Istio)]
- Routing & Load Balancing Engine -> Caching & Response Compression Component: Evaluates cache policies [Internal Memory/Redis]
- Authentication & Authorization Filter -> Third-Party Identity Provider: Verifies JWTs [OAuth2/OIDC]
- API Gateway -> Centralized Observability & SIEM Platform: Exports metrics and traces [Prometheus / OpenTelemetry]

## Technology Stack
- Envoy: Selected as the API Gateway container and routing engine for high performance and extensibility
- Envoy WASM/Lua: Used for custom authentication, authorization, and data residency filtering
- HashiCorp Vault: Manages dynamic TLS certificates and OAuth validation keys securely
- Redis: Backs the caching layer for rapid retrieval of public catalogue metadata
- OpenTelemetry & Prometheus: Powers distributed tracing and metrics export

## Rationale
This architecture meets the strict EU-only data residency constraint by inspecting headers at the ingress boundary. Furthermore, edge caching and Envoy routing optimizations directly support the 99th-percentile search response requirement under 800 ms.