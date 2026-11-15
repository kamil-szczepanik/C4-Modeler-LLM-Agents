## Overview
The Library Management System provides cataloguing, circulation, and self-service portals for public and academic libraries. It ensures EU-only data residency and sub-800ms search response times.

## Key Elements
- Library Patrons, Librarians, Library Administrators
- Librarian Back-office (Next.js Web App)
- Circulation Workspace Component, Cataloguing Management Component, Admin Dashboard Component, Auth Session Handler Component
- API Gateway (NGINX / Envoy)
- Catalogue Service (Java / Spring Boot), Circulation Service (Node.js / Express)
- PostgreSQL Database (EU-hosted), Elasticsearch (EU-hosted)
- External Identity Provider (IdP), Third-Party Payment Gateway

## Relationships
- Librarians / Administrators -> Librarian Back-office: Interacts with application [HTTPS]
- Auth Session Handler Component -> External IdP: Manages OIDC authorization code flow [HTTPS]
- Circulation Workspace Component -> API Gateway: Sends commands and real-time alerts [HTTPS/REST, WebSockets with token authentication]
- Cataloguing Management Component -> API Gateway: Uploads assets [HTTPS/Multipart REST]
- Admin Dashboard Component -> API Gateway: Fetches analytics and reports [HTTPS/REST]

## Technology Stack
- Next.js (React 18+) with Server Actions and App Router: Prevents PII leakage and secures session storage
- HTTP-only, Secure Cookies: Prevents XSS-based token theft
- PostgreSQL & Elasticsearch (EU-hosted): Guarantees data residency and sub-800ms search performance
- OAuth2/OIDC with JWTs: Enforces role-based access control

## Rationale
This architecture uses server-side rendering and isolated frontend components to guarantee strict EU data residency and robust security. It ensures sub-800ms search performance while maintaining strict administrative boundaries and compliance.