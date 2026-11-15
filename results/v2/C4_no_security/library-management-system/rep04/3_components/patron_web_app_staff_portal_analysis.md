## Overview
The Library Management System provides cataloging, circulation management, and self-service portals for public and academic libraries. It features EU-hosted architecture designed to guarantee strict data residency and optimal search performance.

## Key Elements
- Library Patrons
- Librarians and Circulation Staff
- Library Administrators
- Patron Web App & Staff Portal (TypeScript/React SPAs)
- Patron SPA Component
- Staff SPA Component
- Session & Token Management Module
- API Client Component
- API Gateway (Nginx or Spring Cloud Gateway)
- Catalog & Search Service (Java/Spring Boot + Elasticsearch)
- Circulation Service (Java/Spring Boot + PostgreSQL)
- Identity Provider
- EU-hosted Log & Metrics Aggregator

## Relationships
- Library Patrons -> Patron Web App & Staff Portal: Accesses self-service portal via HTTPS/REST and WebSockets
- Librarians and Circulation Staff -> Patron Web App & Staff Portal: Accesses staff tools via HTTPS/REST and WebSockets
- Library Administrators -> Patron Web App & Staff Portal: Accesses management tools via HTTPS/REST and WebSockets
- Patron Web App & Staff Portal -> API Gateway: Sends client requests via HTTPS/REST and WebSockets
- Patron Web App & Staff Portal -> Identity Provider: Authenticates users via OIDC/OAuth2 over HTTPS

## Technology Stack
- TypeScript / React with Vite: Fast client-side builds and optimized SPA bundle delivery
- EU-hosted Object Storage and CDN: Enforces EU-only data residency and static asset hosting
- Axios / Fetch API Client: Manages request tracing, telemetry, and EU-header propagation
- OAuth2 / OIDC: Secures user authentication and token exchange

## Rationale
The component-level SPA breakdown with strict RBAC routing and session management supports rapid, secure self-service and administrative workflows. Client-side caching and RUM telemetry ensure compliance with the <800ms search performance requirement and EU data residency constraints.