## Overview
- The system is an API Gateway container for the Library Management System, providing secure ingress routing, traffic throttling, and protocol translation.
- Its core purpose is to enforce security policies and high-performance request dispatching to satisfy strict EU data residency and sub-800ms search latency requirements.

## Key Elements
- API Gateway (Spring Cloud Gateway, Java 21)
- Routing & Dispatcher Component (Spring Cloud Gateway Core)
- Authentication & Authorization Filter (Spring Security OAuth2 Resource Server)
- Rate Limiting & Throttling Filter (Redis-backed Token Bucket)
- Resilience & Circuit Breaker Filter (Resilience4j)
- Web Frontend, Catalogue Service, Circulation Service, Notification Service, IdP

## Relationships
- Web Frontend -> API Gateway: Sends API requests via [HTTPS/REST] with TLS 1.3
- Web Frontend -> Authentication & Authorization Filter: Validates user sessions via [HTTPS/REST]
- Authentication & Authorization Filter -> Routing & Dispatcher Component: Forwards validated requests via [Internal Java Method Call]
- Routing & Dispatcher Component -> Resilience & Circuit Breaker Filter: Passes requests for fault-tolerance checks via [Internal Java Method Call]
- Resilience & Circuit Breaker Filter -> Catalogue Service / Circulation Service / Notification Service: Routes protected calls via [gRPC with mTLS, propagated JWTs, OpenTelemetry headers]

## Technology Stack
- Spring Cloud Gateway (Java 21): Reactive model selected for non-blocking I/O and performance
- Spring Security OAuth2: Handles OIDC token validation and audience checks
- Redis: Localized cluster instance used for token-bucket rate limiting within EU nodes
- Resilience4j: Implements circuit breakers and bulkheading for downstream fault tolerance
- OpenTelemetry: Injects distributed trace contexts at the edge for latency tracking
- Kubernetes Secrets: Secures ingestion of IdP client secrets and mTLS certificates

## Rationale
- The reactive Spring Cloud Gateway architecture and non-blocking components minimize overhead to meet the <800ms search SLA.
- Localized Redis clustering, TLS 1.3 hardening, and strict PII masking in logs and rate limit keys ensure total EU data residency and privacy compliance.