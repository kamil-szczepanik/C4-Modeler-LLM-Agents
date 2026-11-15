## Overview
The Library Management System provides self-service portals and circulation management for public and academic libraries. It features an EU-hosted React single-page application enforcing strict data residency and accessibility.

## Key Elements
* Routing & Auth Module (React Router, OIDC client)
* Catalogue & Search Component (React, TanStack Query)
* Circulation Portal Component (React)
* Localization & Accessibility Module (React-i18next, Aria components)
* API Client Service (Axios)
* Web Server (Nginx)

## Relationships
* Library Patrons, Librarians, Administrators -> Web Application: Accesses portals [HTTPS, TLS 1.3]
* Web Application -> API Gateway: Sends REST/GraphQL API requests [HTTPS, TLS 1.3]
* Routing & Auth Module -> Keycloak/Auth0 EU tenant: Authenticates users [OIDC]

## Technology Stack
* React 18 & TypeScript: Core UI framework for type-safe component development
* TanStack Query: Server-state caching and search optimization for performance <800ms
* Nginx: Web server configured with CSP and HSTS headers for security hardening
* React-i18next & Aria components: Multi-language support and WCAG 2.1 AA compliance

## Rationale
This architecture decouples the frontend to deliver role-optimized portals while utilizing TanStack Query and in-memory token isolation to meet strict EU data security and search performance requirements.