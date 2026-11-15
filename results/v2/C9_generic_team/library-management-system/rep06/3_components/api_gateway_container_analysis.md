## Overview
The Library Management System provides cataloging, circulation, and self-service portals for public and academic libraries while enforcing EU-only data residency. The API Gateway Container manages perimeter security, routing, and resilience.

## Key Elements
- Patrons and Library Staff (Users)
- External Identity Providers (SSO/OAuth), Payment Gateways, External Archival/Reporting System (External Systems)
- Client-Side SPA/Mobile Container (Web/Mobile Technologies)
- API Gateway Container (NGINX / Kong)
- Core Business Logic / Circulation API Container (Microservice / API Runtime)
- Search Engine Container (Elasticsearch / OpenSearch)
- Data Access Layer / Persistence Container (PostgreSQL)
- Asynchronous Message Broker Container (RabbitMQ / Kafka)
- Background Workers Container (Background Worker Runtime)
- Configuration & Secrets Management Container (HashiCorp Vault)
- Centralized Observability Container (Observability Platform)

## Relationships
- Client-Side SPA/Mobile Container -> API Gateway Container: Sends API requests via HTTPS (REST/GraphQL)
- API Gateway Container -> Core Business Logic / Circulation API Container: Routes verified requests via internal gRPC/HTTP
- External Identity Providers (SSO/OAuth) -> API Gateway Container: Authenticates users via OAuth2/OIDC
- Payment Gateways -> API Gateway Container: Sends payment notifications via HTTPS Webhooks

## Technology Stack
- NGINX or Kong: Chosen for the API Gateway Container to handle TLS termination, rate limiting, and JWT validation.
- GitOps: Selected for declarative API Gateway configuration management to ensure environment consistency.
- W3C Trace Context: Implemented for distributed tracing propagation to ensure end-to-end observability.
- Redis: Utilized for partitioned rate-limit state caching to maintain performance.
- RFC 7807 Problem Details: Standardized format for consistent JSON error payloads.

## Rationale
This architecture utilizes an NGINX/Kong API Gateway to enforce security, token-based residency claims, and fail-open rate limiting at the perimeter. These mechanisms protect backend microservices, maintain < 800 ms search latency, and guarantee strict EU data residency compliance.