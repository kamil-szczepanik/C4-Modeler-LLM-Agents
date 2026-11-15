## Overview
[The system is a Library Management System providing cataloging, circulation, and self-service portals for public and academic libraries. Its core purpose is to deliver secure, performant, and EU-compliant library operations.]

## Key Elements
- **Users**: Library Patron, Academic Researcher, Librarian / Administrator, Library Manager
- **External Systems**: EU-Compliant Payment Gateway, Third-Party Notification Service, External Identity Provider (IdP)
- **Containers**: Web Frontend (React, Nginx), API Gateway (Kong, Spring Cloud Gateway), Core Catalog Service (Spring Boot, PostgreSQL), Circulation & Search Service (FastAPI, Elasticsearch), Worker Service (Celery, RabbitMQ)
- **API Gateway Components**: Authentication & Authorization, Routing & Load Balancing, Rate Limiting & Throttling, Telemetry & Logging, Request Transformation, Circuit Breaker & Fallback

## Relationships
- Web Frontend -> API Gateway [HTTPS/REST]
- API Gateway -> Core Catalog Service [gRPC over Istio service mesh (mTLS)]
- API Gateway -> Circulation & Search Service [gRPC over Istio service mesh (mTLS)]
- API Gateway -> Worker Service [gRPC over Istio service mesh (mTLS)]
- API Gateway -> External Identity Provider (IdP) [OAuth2/OIDC JWT validation]

## Technology Stack
- **Kong / Spring Cloud Gateway**: API Gateway implementation for routing, plugins, and ingress security
- **Spring Boot & PostgreSQL**: Core Catalog Service for relational data storage and business logic
- **FastAPI & Elasticsearch**: Circulation & Search Service for high-performance searching meeting the <800ms SLA
- **Celery & RabbitMQ**: Worker Service for asynchronous background task execution
- **Istio & Redis**: Service mesh for mTLS enforcement and distributed state management for rate limiting

## Rationale
[This architecture enforces strict EU data residency constraints through localized deployments while utilizing high-performance components like Elasticsearch and gRPC to meet sub-800ms search response SLAs. Tiered rate-limiting, robust security controls, and circuit breakers ensure reliability and tailored user experiences across all patron and administrator personas.]