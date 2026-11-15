## Overview
The API Gateway container for the Library Management System manages ingress routing, security enforcement, and caching for public and academic library portals. It ensures EU-only data residency, strict authentication, and low-latency search performance.

## Key Elements
- Routing & Load Balancing Component (Spring Cloud Gateway)
- Authentication & Authorization Filter
- Rate Limiting & Throttling Component (Redis)
- Caching & Compression Component
- Telemetry & Audit Interceptor
- Web Application Firewall (WAF) Layer
- Kubernetes Deployment Infrastructure

## Relationships
- Web Application SPA -> Authentication & Authorization Filter: Validates JWTs [HTTPS]
- Routing & Load Balancing Component -> Caching & Compression Component: Checks cached responses [Internal]
- Routing & Load Balancing Component -> Rate Limiting & Throttling Component: Checks request quotas [In-memory Redis protocol]
- Authentication & Authorization Filter -> Core Domain / Search Service: Propagates cryptographic assertion tokens [gRPC over HTTP/2 with mTLS]
- Kubernetes Cloud Load Balancer -> Routing & Load Balancing Component: Routes EU-only traffic [HTTPS]

## Technology Stack
- Spring Cloud Gateway: Dynamic request routing and load balancing
- Redis: Distributed token bucket rate limiting and pub/sub cache invalidation
- gRPC over HTTP/2 with mTLS: Zero-trust internal communication protocol
- OpenTelemetry: Distributed tracing and telemetry collection
- Kubernetes: Horizontal autoscaling and resource allocation

## Rationale
This architecture ensures secure, low-latency API routing while enforcing EU data residency constraints. Edge caching and rate limiting directly support the requirement for 99th-percentile search responses under 800 ms.