## Overview
The Library Management System provides a catalogue, circulation, and self-service portal for libraries. The architecture ensures strict EU-only data residency and sub-800ms search performance.

## Key Elements
- Web Application (SPA) container (React/TypeScript)
- Router & Shell Component (`react-router`)
- Authentication State Component (Context API + `oidc-client-ts`)
- Catalogue & Search UI Component
- Circulation & Self-Service Component
- State Management & Caching Store (`TanStack Query`)
- Notification & Feedback Component (`React Toastify`)
- API Client / HTTP Interceptor Component (`Axios`)
- API Gateway (`Nginx / Envoy`)

## Relationships
- Library Patrons and Staff -> Web Application (SPA) via browser `[HTTPS]`
- API Client / HTTP Interceptor Component -> API Gateway via `[HTTPS/REST]`
- Authentication State Component -> API Gateway via `[HTTPS/REST]`
- Catalogue & Search UI Component -> API Gateway via `[HTTPS/REST]`

## Technology Stack
- React/TypeScript: Powers the frontend SPA for high interactivity
- TanStack Query: Optimizes data fetching and client-side caching for performance
- Axios: Centralizes HTTP requests and bearer token injection
- EU-Central CDN: Enforces strict EU data residency constraints

## Rationale
Client-side caching via TanStack Query and input debouncing achieve the 99th-percentile search response time under 800ms. Deploying exclusively to an EU-Central CDN satisfies mandatory EU data residency constraints.