## Overview
The Library Management System provides self-service portals, circulation management, and cataloguing for public and academic libraries. It ensures strict EU data residency and high-performance search capabilities.

## Key Elements
- Library Patrons & Staff
- EU-edge Reverse Proxy
- Self-Service Web App
- Admin/Staff Portal
- API Gateway
- Circulation & Cataloguing Service
- Core Search Engine
- Database
- Third-Party Digital Content Providers
- Payment Gateway
- Notification Service

## Relationships
- Library Patrons & Staff -> EU-edge Reverse Proxy (HTTPS/TLS 1.3, OIDC/OAuth2)
- EU-edge Reverse Proxy -> Self-Service Web App / Admin/Staff Portal (HTTPS)
- Self-Service Web App & Admin/Staff Portal -> API Gateway (HTTPS/REST with JWT)
- API Gateway -> Circulation & Cataloguing Service (gRPC/Internal, mTLS)
- Circulation & Cataloguing Service -> Core Search Engine (TCP)
- Circulation & Cataloguing Service -> Database (PostgreSQL Wire Protocol)
- Library Management System -> Third-Party Digital Content Providers (REST/JSON over HTTPS)
- Library Management System -> Payment Gateway (HTTPS/REST)
- Library Management System -> Notification Service (Webhooks/SMTP with HMAC)

## Technology Stack
- React/Next.js SPA & React Admin SPA: Frontend UI deployed on EU-edge static hosting
- Nginx/Kong: API Gateway for routing, rate limiting, and OAuth2/OIDC token validation
- Node.js/TypeScript: Circulation & Cataloguing Service for core business logic
- Elasticsearch: Core Search Engine hosted in EU regions to satisfy R-05 search SLA (<800ms)
- PostgreSQL: Managed database with AES-256 encryption at rest in EU region for data residency

## Rationale
This architecture uses stateless frontends and managed EU-hosted backend services to enforce strict data residency and security compliance. Dedicated search and caching layers guarantee high-performance search SLAs for patrons and staff.