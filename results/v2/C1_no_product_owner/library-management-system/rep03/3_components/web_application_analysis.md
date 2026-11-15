## Overview
The Library Management System provides self-service portals and circulation management for public and academic libraries. The Web Application container delivers high-performance patron and staff user interfaces while enforcing strict EU data residency constraints.

## Key Elements
- Web Application (React 18, TypeScript, Vite, Nginx)
- Routing & Shell (React Router)
- State Management (Zustand / React Query)
- API Client Layer (Axios / Fetch)
- Feature Modules (Patron Portal & Staff Portal)
- API Gateway (Envoy)

## Relationships
- Library Patron -> Web Application: Accesses self-service portal [HTTPS]
- Librarian / Staff -> Web Application: Accesses management portal [HTTPS]
- Web Application -> API Gateway: Forwards authenticated client requests [HTTPS]
- Routing & Shell -> Feature Modules: Orchestrates UI layouts and roles
- Feature Modules -> State Management & API Client Layer: Retrieves and caches data

## Technology Stack
- React 18 & TypeScript: Provides type-safe component development
- Vite: Optimizes bundling for fast render cycles and performance <800ms
- Nginx: Serves static assets with custom cache headers and security policies
- Zustand / React Query: Manages server-state caching and UI state

## Rationale
Decoupling the Web Application into modular React components ensures rapid rendering and meets strict search performance targets. Self-hosting assets and observability within Nginx guarantees compliance with EU-only data residency requirements.