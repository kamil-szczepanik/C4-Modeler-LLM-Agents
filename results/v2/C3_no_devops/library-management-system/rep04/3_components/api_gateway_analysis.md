## Overview
The Library Management System is a solution for public and academic libraries to catalogue items, manage circulation, and provide self-service portals. It ensures EU-only data residency and meets strict performance constraints.

## Key Elements
- API Gateway (Kong configured with Redis)
- Routing Engine (Lua/Kong Router)
- Authentication & Authorization Plugin (OAuth2/JWT)
- Rate Limiting & Throttling Module (Redis-backed)
- SSL Termination Module with WAF / OWASP Core Rule Set (OpenSSL/Nginx core)
- Analytics & Transformation Plugin (Lua/Kong)
- Core Circulation & Cataloguing Service (Spring Boot)
- Search Service (Elasticsearch)
- Identity Provider (IdP)
- Reporting Service (Python/FastAPI)

## Relationships
- Patron Portal -> API Gateway: Makes API requests [HTTPS (TLS 1.3)]
- Staff Dashboard -> API Gateway: Makes API requests [HTTPS (TLS 1.3)]
- API Gateway -> Identity Provider: Validates JWT tokens [HTTPS]
- Routing Engine -> Core Circulation & Cataloguing Service: Proxies requests [gRPC over mTLS]
- Routing Engine -> Search Service: Proxies search queries [gRPC over mTLS]
- Analytics & Transformation Plugin -> Reporting Service: Publishes anonymized usage metrics [HTTP/REST over TLS 1.3]

## Technology Stack
- Kong API Gateway: Chosen for declarative configuration and native plugins to reduce overhead
- Redis: Used for caching and rate-limiting to protect availability and support performance goals
- gRPC over mTLS: Used for secure, low-latency internal communication between the gateway and microservices
- OAuth 2.0 / JWT: Used for localized token validation at the gateway layer

## Rationale
This architecture ensures high performance with search responses under 800ms by offloading cross-cutting concerns and using asynchronous analytics. It also enforces strict EU data residency and security controls through perimeter WAF protection and internal mTLS.