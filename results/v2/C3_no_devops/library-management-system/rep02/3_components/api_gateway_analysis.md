## Overview
The Library Management System provides cataloging, circulation, and self-service portals for libraries while strictly enforcing EU data residency. It uses a secure API Gateway to route and protect internal services.

## Key Elements
- **Users**: Library Member (Patron), Librarian / Library Staff, Library Administrator
- **External Systems**: Payment Gateway, Digital Content Providers, Notification System
- **Containers**: Web Application (React/TypeScript), API Gateway, Core Business Services (Spring Boot), Search Engine (Elasticsearch / OpenSearch), Database (PostgreSQL), Analytics Worker (Python/Spring)
- **Gateway Components**: Routing & Load Balancer, Authentication & Authorization Filter, Rate Limiting & Throttling Component (Redis-backed), WAF / Payload Inspection Filter, API Analytics Emitter

## Relationships
- Web Application -> API Gateway: Sends user requests [HTTPS / REST and WebSockets]
- API Gateway -> Core Business Services: Forwards core API requests retaining signed JWT [gRPC / internal REST with mTLS]
- API Gateway -> Search Engine: Queries search index [gRPC / internal REST with mTLS]
- Analytics Emitter -> Analytics Worker: Streams usage metrics [Apache Kafka / RabbitMQ]

## Technology Stack
- API Gateway: NGINX / Spring Cloud Gateway for performant routing
- Security: OAuth 2.0 / OpenID Connect with JWT, Spring Security, ModSecurity WAF for perimeter defense
- Throttling: Redis-backed token bucket for user-persona quotas
- Transport: mTLS with short-lived certificates for internal zero-trust communication

## Rationale
This architecture ensures secure, low-latency request routing and strict EU data residency enforcement at the perimeter. Asynchronous analytics and optimized token propagation safeguard the 99th-percentile search response time under 800 ms.