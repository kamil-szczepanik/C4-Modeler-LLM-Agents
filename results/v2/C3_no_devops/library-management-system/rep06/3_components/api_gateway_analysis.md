## Overview
The Library Management System is a comprehensive platform for public and academic libraries to catalogue items, manage circulation, and provide secure self-service portals. It enforces strict EU-only data residency and high-performance search SLAs.

## Key Elements
- Library Patrons, Librarians / Circulation Staff, Library Administrators (Users)
- EU Identity Provider (IdP) & EU-compliant Payment Gateway (External Systems)
- Frontend Container: React/TypeScript Single Page Application (SPA)
- API Gateway: Nginx/Kong with JWT Validation, WAF, and Redis Cache plugins
- Catalogue & Search Service: Spring Boot / Java with Elasticsearch
- Circulation & Member Service: Node.js / NestJS
- Analytics & Reporting Container: Python / FastAPI
- Message Broker: Apache Kafka / RabbitMQ
- Databases: EU-hosted PostgreSQL with AES-256 encryption-at-rest

## Relationships
- Frontend Container -> API Gateway: Sends API requests [HTTPS/REST, TLS 1.3]
- API Gateway -> EU Identity Provider (IdP): Validates tokens and checks revocation [OAuth2/OIDC]
- API Gateway -> Catalogue & Search Service / Circulation & Member Service / Analytics & Reporting Container: Routes requests [gRPC over mTLS]
- API Gateway -> Redis Cache: Checks token blacklist and rate limits [RESP]
- API Gateway -> Message Broker: Publishes API usage telemetry [AMQP / Kafka]

## Technology Stack
- Kong / Nginx: API Gateway edge routing, WAF, payload limiting, and security headers for high-performance proxying.
- Redis: Low-latency distributed cache for token blacklisting, rate limiting, and persona-based quotas to meet <800ms search SLA.
- gRPC over mTLS: Zero-trust internal communication protocol between API Gateway and microservices.
- TLS 1.3: Enforced cipher suites for secure incoming frontend traffic.

## Rationale
This architecture ensures strict compliance with EU-only data residency and GDPR mandates via localized token validation and Redis blacklisting. It meets the rigorous <800ms search performance SLA by offloading rate limiting, caching, and secure edge routing to the Kong/Nginx API Gateway.