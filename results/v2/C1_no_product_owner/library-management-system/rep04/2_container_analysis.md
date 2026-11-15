## Overview
The Library Management System provides cataloging, circulation, and self-service portals for public and academic libraries. It is engineered to satisfy EU-only data residency and sub-800ms search performance requirements.

## Key Elements
- Library Patron and Librarian (Users)
- Identity Provider (IdP), Payment Gateway, and Notification Provider (External Systems)
- Web Frontend: React SPA served via Nginx
- API Gateway: Spring Cloud Gateway
- Microservices: Catalogue Service, Circulation Service, and Notification Service (Spring Boot / Java 21)
- Data & Messaging: PostgreSQL, Elasticsearch, and RabbitMQ
- Infrastructure: Istio service mesh and HashiCorp Vault

## Relationships
- Library Patron/Librarian to Web Frontend via HTTPS/REST and WebSockets
- Web Frontend to API Gateway via HTTPS/REST
- API Gateway to Microservices via internal gRPC with mTLS and propagated JWTs
- Microservices to PostgreSQL and Elasticsearch via encrypted database protocols (AES-256)
- Microservices to RabbitMQ via AMQP over TLS
- External integrations (IdP, Payment Gateway, Notification Provider) via TLS 1.3

## Technology Stack
- Java 21 / Spring Boot: Standardized backend runtime to reduce operational and polyglot complexity
- Spring Cloud Gateway: Handles ingress routing, rate limiting, and OAuth2/OIDC validation
- PostgreSQL: Relational data store for structured catalogue and circulation data
- Elasticsearch: Dedicated search engine ensuring 99th-percentile search responses under 800ms
- RabbitMQ: Asynchronous message broker with dead-letter exchanges
- Istio / Envoy: Service mesh enforcing automated mTLS and distributed trace propagation via OpenTelemetry

## Rationale
Standardizing on a unified Java 21 Spring Boot stack simplifies operational pipelines while satisfying the strict EU data residency constraint. Furthermore, the combination of Elasticsearch, gRPC, and an Istio service mesh directly addresses high-performance search SLAs and zero-trust security mandates.