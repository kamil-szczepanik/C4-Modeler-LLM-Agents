## Overview
The Library Management System is a comprehensive solution providing self-service portals and circulation management for academic and public libraries. It delivers secure, highly responsive patron and librarian interfaces while enforcing EU data residency constraints.

## Key Elements
- Web App / SPA (React/TypeScript, CDN)
- Routing & Authentication Module (React Router, OIDC client)
- Catalog Discovery Component (React, TanStack Query)
- Self-Service Circulation Component
- Librarian Management Dashboard
- State & Caching Layer (TanStack Query / Zustand)
- API Gateway (Envoy / Kong)
- External Identity Provider (IdP)
- Payment Gateway

## Relationships
- Library Patrons, Librarians, Administrators -> Web App / SPA: Accesses portal interfaces [HTTPS]
- Routing & Authentication Module -> External Identity Provider: OIDC/OAuth2 authentication [HTTPS]
- UI Components -> State & Caching Layer: In-memory state management [Direct Function Call]
- State & Caching Layer -> API Gateway: REST/JSON and WebSockets [HTTPS]

## Technology Stack
- React/TypeScript: Powers the single-page application for dynamic role-based rendering and WCAG 2.1 AA compliance.
- TanStack Query / Zustand: Manages in-memory state, caching, and offline resilience to meet performance goals.
- EU-Localized CDN: Ensures strict EU data residency, low-latency asset delivery, and automated cache invalidation.
- OIDC/OAuth2: Secures authentication with tokens stored strictly in volatile memory to prevent XSS.

## Rationale
This architecture decouples the responsive, accessible frontend from core backend services while utilizing localized CDN edge nodes to satisfy strict EU data residency. The in-memory caching layer directly supports the sub-800ms search performance requirement.