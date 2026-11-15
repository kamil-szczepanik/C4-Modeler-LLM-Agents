## Overview
The Library Management System is a comprehensive digital solution for public and academic libraries to catalogue physical and digital items, manage circulation, and provide self-service patron portals with strict EU data residency. It delivers secure, high-performance patron interactions, including rapid catalogue searches and fine settlements.

## Key Elements
- Library Patrons & Staff [person]
- EU-edge Reverse Proxy [externalSystem]
- Self-Service Web App [container, React/Next.js SPA with BFF]
- Admin/Staff Portal [container, React Admin SPA]
- API Gateway [container, Nginx/Kong]
- Circulation & Cataloguing Service [container, Node.js/TypeScript]
- Core Search Engine [container, Elasticsearch]
- Database [container, PostgreSQL]
- Payment Gateway [externalSystem]
- Third-Party Digital Content Providers [externalSystem]
- Notification Service [externalSystem]

## Relationships
- Library Patrons & Staff -> EU-edge Reverse Proxy [HTTPS/TLS 1.3, OIDC/OAuth2]
- EU-edge Reverse Proxy -> Self-Service Web App [HTTPS]
- Self-Service Web App -> API Gateway [HTTPS/REST with HttpOnly Cookie-to-JWT translation]
- API Gateway -> Circulation & Cataloguing Service [gRPC/Internal, mTLS]
- Circulation & Cataloguing Service -> Core Search Engine [TCP]
- Circulation & Cataloguing Service -> Database [PostgreSQL Wire Protocol]
- Fine Payment Widget -> Payment Gateway [HTTPS, via isolated iframe tokenization]
- Circulation & Cataloguing Service -> Third-Party Digital Content Providers [REST/JSON over HTTPS]
- Circulation & Cataloguing Service -> Notification Service [Webhooks/SMTP with HMAC]

## Technology Stack
- React/Next.js SPA with BFF: Chosen for rapid UI rendering, client-side caching, and secure HttpOnly cookie session management.
- Nginx/Kong API Gateway: Selected for robust routing, rate limiting, and OAuth2/OIDC token validation.
- Elasticsearch: Deployed in EU regions to meet the 99th-percentile search response SLA under 800ms.
- PostgreSQL: Managed database with AES-256 encryption at rest to guarantee EU-only data residency.
- Node.js/TypeScript: Utilized for scalable circulation and cataloguing microservices.

## Rationale
This architecture combines an EU-pinned edge frontend with a secure BFF pattern to satisfy strict data residency and XSS/CSRF mitigation requirements. Decoupled microservices and an optimized search engine ensure high performance and low-latency patron interactions.