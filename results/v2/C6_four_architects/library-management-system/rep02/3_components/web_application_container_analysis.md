## Overview
- Library Management System provides cataloging, circulation, and self-service portals for public and academic libraries within an EU-only data residency constraint.
- The Web Application Container acts as the frontend Single Page Application serving both patrons and librarians.

## Key Elements
- Web Application Container (React/TypeScript, Nginx)
- Router Component (React Router)
- State Management Component (Redux Toolkit / React Query)
- API Client Component (Axios)
- UI Component Library (Tailwind CSS / Radix UI)
- Authentication & Session Component (OIDC/OAuth2 Client)
- Localization (i18n) Component
- Error Boundary & Telemetry Component
- API Gateway Container (Kong/Envoy)

## Relationships
- Library Patron & Librarian / Staff -> Web Application Container: Accesses portals and manages operations via [HTTPS/REST and WebSockets]
- Router Component -> UI Component Library: Renders views via [TypeScript/React props]
- Router Component -> Authentication & Session Component: Enforces route guards via [TypeScript callbacks]
- State Management Component -> API Client Component: Synchronizes server state via [TypeScript function calls]
- Authentication & Session Component -> API Client Component: Injects Bearer tokens via [Axios interceptors]
- API Client Component -> API Gateway Container: Forwards API requests and frames via [HTTPS/REST and WebSockets]

## Technology Stack
- React/TypeScript: Core framework for component logic with type safety
- Nginx: Serves static assets locally to enforce EU data residency without external CDNs
- React Query & Redux Toolkit: Manages server-state caching and local state to meet <800ms search performance (R-05)
- Tailwind CSS & Radix UI: Provides accessible design system components
- Axios: Handles HTTP requests with automatic token refresh interceptors
- OIDC/OAuth2: Manages secure user authentication and JWT session tokens

## Rationale
- The modular component decomposition ensures a high-performance, responsive UI that easily meets the sub-800ms search response requirement.
- Local Nginx asset serving and strict routing through the API Gateway guarantee 100% compliance with EU-only data residency constraints.