## Overview
The API Gateway serves as the single secure entry point for the Library Management System, providing request routing, security enforcement, and rate limiting. It ensures EU data residency while routing traffic to downstream core and search services.

## Key Elements
- Web App (React/TypeScript, Nginx)
- API Gateway (Kong / Spring Cloud Gateway)
- WAF / Input Sanitization Plugin (OWASP CRS)
- Authentication Filter / Interceptor (OAuth2/JWT Plugin)
- Routing Engine & Request Transformation Module
- Rate Limiting & Throttling Module (Redis-backed)
- Core Domain Service & Search Service (Elasticsearch)

## Relationships
- Web App -> WAF: Ingress inspection [HTTPS/JSON]
- WAF -> Authentication Filter: Sanitized payload forwarding
- Authentication Filter -> Routing Engine: Forwards validated requests
- Routing Engine -> Core Domain Service / Search Service: Proxies traffic with W3C Trace Context headers [gRPC over mTLS]

## Technology Stack
- Kong / Spring Cloud Gateway: Chosen for dynamic routing, low latency, and plugin extensibility
- Redis: Backs distributed rate-limiting with strict EU-only deployment for compliance
- OAuth2/JWT & OWASP CRS: Enforces perimeter security, input sanitization, and token validation
- gRPC over mTLS: Ensures encrypted, high-performance internal communication

## Rationale
This architecture guarantees strict EU data residency via local Redis and infrastructure deployment while meeting the <800ms search SLA through gRPC, distributed tracing, and Redis-backed rate limiting. Edge security controls protect downstream services from volumetric and malicious attacks.