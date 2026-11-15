## Overview
The Library Management System is a comprehensive platform for public and academic libraries to catalogue physical and digital items, manage circulation, and provide secure self-service portals. It guarantees strict EU-only data residency and high-performance search SLAs.

## Key Elements
- Library Patrons & Staff
- EU-edge Reverse Proxy
- Self-Service Web App (React/Next.js SPA)
- Admin/Staff Portal (React Admin SPA)
- API Gateway (Nginx/Kong)
- Circulation & Cataloguing Service (Node.js/TypeScript)
- Core Search Engine (Elasticsearch)
- Database (PostgreSQL)
- Third-Party Digital Content Providers
- Payment Gateway
- Notification Service

## Relationships
- Library Patrons & Staff -> EU-edge Reverse Proxy [HTTPS/TLS 1.3, OIDC/OAuth2]
- EU-edge Reverse Proxy -> Self-Service Web App & Admin/Staff Portal [HTTPS]
- Self-Service Web App & Admin/Staff Portal -> API Gateway [HTTPS/REST with JWT]
- API Gateway -> Circulation & Cataloguing Service [gRPC/Internal, mTLS]
- Circulation & Cataloguing Service -> Core Search Engine [TCP over TLS]
- Circulation & Cataloguing Service -> Database [PostgreSQL Wire Protocol over TLS]
- Circulation & Cataloguing Service -> Third-Party Digital Content Providers [REST/JSON over HTTPS]
- Circulation & Cataloguing Service -> Payment Gateway [HTTPS/REST]
- Circulation & Cataloguing Service -> Notification Service [Webhooks/SMTP with HMAC]

## Technology Stack
- Node.js & TypeScript: Powers the Circulation & Cataloguing Service with structured schemas (Zod).
- PostgreSQL: Stores transactional data with AES-256 encryption at rest and a transactional outbox pattern.
- Elasticsearch: Delivers low-latency catalog search meeting the <800ms SLA.
- Nginx/Kong: Acts as the API Gateway for routing and JWT validation.
- React & Next.js: Provides frontend SPA experiences deployed on EU-edge static hosting.

## Rationale
This architecture ensures strict EU-only data residency through regional database and search deployments while isolating failures using circuit breakers and bulkhead patterns. The outbox pattern guarantees reliable audit logging and webhook dispatches without risking data loss.