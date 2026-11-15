## Overview
The Library Management System provides cataloguing, circulation, and self-service portals for public and academic libraries. The system enforces strict EU-only data residency and sub-800ms search performance SLAs.

## Key Elements
- Library Patrons & Staff [person]
- EU-edge Reverse Proxy [externalSystem]
- Self-Service Web App [container] (React/Next.js SPA)
- Admin/Staff Portal [container] (React Admin SPA)
- API Gateway [container] (Nginx/Kong)
- Circulation & Cataloguing Service [container] (Node.js/TypeScript)
- Core Search Engine [container] (Elasticsearch)
- Database [container] (PostgreSQL)
- Third-Party Digital Content Providers [externalSystem]
- Payment Gateway [externalSystem]
- Notification Service [externalSystem]

## Relationships
- Library Patrons & Staff -> EU-edge Reverse Proxy [HTTPS/TLS 1.3, OIDC/OAuth2]
- EU-edge Reverse Proxy -> Self-Service Web App [HTTPS]
- EU-edge Reverse Proxy -> Admin/Staff Portal [HTTPS]
- Self-Service Web App -> API Gateway [HTTPS/REST with JWT]
- Admin/Staff Portal -> API Gateway [HTTPS/REST with JWT]
- API Gateway -> Circulation & Cataloguing Service [gRPC/Internal, mTLS]
- Circulation & Cataloguing Service -> Core Search Engine [TCP]
- Circulation & Cataloguing Service -> Database [PostgreSQL Wire Protocol]

## Technology Stack
- React/Next.js SPA: Frontend implementation for rapid, responsive UI interactions
- React Admin SPA: High-density data grids and administrative workflows
- Nginx/Kong API Gateway: Centralized routing, rate limiting, and token validation
- Node.js/TypeScript: Type-safe core business logic and service orchestration
- Elasticsearch: High-performance catalog searching meeting the <800ms SLA
- PostgreSQL: Managed relational storage with AES-256 encryption at rest
- OIDC/OAuth2 with JWT: Secure, stateless authentication and authorization

## Rationale
This architecture uses decoupled frontend SPAs backed by a secure API Gateway and TypeScript services to guarantee low-latency workflows. Deploying all components within EU-hosted infrastructure strictly satisfies the mandatory data residency constraints.