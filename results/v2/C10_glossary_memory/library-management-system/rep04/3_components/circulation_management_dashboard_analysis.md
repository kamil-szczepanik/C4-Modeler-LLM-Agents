## Overview
The Circulation Management Dashboard is a secure React SPA that empowers librarians and staff to execute rapid check-outs, returns, and exception management. It relies on the API Gateway and downstream services while supporting encrypted offline operations for high-availability desk workflows.

## Key Elements
- Librarians / Circulation Staff [person]
- Circulation Management Dashboard [container] (React / TypeScript SPA)
- API Gateway [container] (NGINX / Kong)
- Circulation & Loan Service [container] (Node.js / Express)
- Identity Provider [container] (Keycloak/Auth0 EU)
- IndexedDB Local Cache [component]
- Sync Manager [component]
- Loan Processing Component [component]
- Exception Management Component [component]

## Relationships
- Librarians / Circulation Staff -> Circulation Management Dashboard: Interacts with circulation workflows [HTTPS]
- Circulation Management Dashboard -> API Gateway: Routes synchronous operational commands and flushes queued offline transactions [REST / JSON over HTTPS / TLS 1.3]
- Circulation Management Dashboard -> Identity Provider: Manages session tokens and authentication [OIDC / OAuth 2.0 over HTTPS with PKCE]
- Circulation Management Dashboard -> Circulation & Loan Service: Processes loans and resolves exceptions (via API Gateway) [REST / JSON over HTTPS / TLS 1.3]

## Technology Stack
- React / TypeScript: Chosen for building a high-performance, responsive Single Page Application.
- IndexedDB with Web Crypto API: Provides encrypted client-side storage to safely buffer offline transactions at rest.
- OpenTelemetry & RUM: Implemented for end-to-end tracing and Core Web Vitals monitoring.
- Globally Distributed CDN: Serves static assets from EU-only edge nodes to enforce data residency and minimize load times.

## Rationale
This architecture ensures sub-3-second transaction times and continuous desk operations through robust client-side caching and offline queue management. Strict token handling, encryption-at-rest, and API Gateway routing maintain enterprise security and EU data residency compliance.