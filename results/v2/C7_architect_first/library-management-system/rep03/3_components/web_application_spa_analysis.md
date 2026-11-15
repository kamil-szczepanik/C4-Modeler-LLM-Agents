## Overview
The Library Management System is a solution for public and academic libraries to catalogue physical and digital items, manage circulation, and provide self-service portals. It enforces strict EU-only data residency and maintains a 99th-percentile search response time under 800 ms.

## Key Elements
* **Web Application SPA**: React/TypeScript client application delivered via static CDN.
* **Routing & State Management Component**: React Router & Zustand managing navigation, roles, and in-memory state.
* **API Client Component**: Axios/Fetch with interceptors for Gateway communication.
* **Search & Catalog UI Component**: Reactive UI supporting WCAG 2.1 AA accessibility and <800ms search NFR.
* **Authentication & Session Component**: OIDC Client using Authorization Code Flow with PKCE.
* **Accessibility & Localization Provider**: Cross-cutting context for i18n and screen-reader compliance.
* **Telemetry & Resilience Middleware**: OpenTelemetry SDK and circuit-breaker integration.

## Relationships
* Library Patron & Librarian / Staff -> Web Application SPA: Accesses portals [HTTPS/WSS]
* Web Application SPA -> API Gateway: Sends API requests and JWT validation [HTTPS/WSS with JWT]
* Web Application SPA -> Third-Party IdP / Academic SSO: Authenticates via Authorization Code Flow with PKCE [HTTPS]
* Telemetry & Resilience Middleware -> EU-hosted API Gateway: Exports sanitized OpenTelemetry traces [HTTPS]

## Technology Stack
* **React/TypeScript**: Core UI framework for component development and type safety.
* **Zustand**: In-memory state management to prevent JWT token leakage in localStorage.
* **OpenTelemetry (OTel) Web SDK**: Standardized EU-compliant telemetry export.
* **CDN with SRI**: Cryptographically secure static asset delivery enforcing Subresource Integrity.

## Rationale
This architecture uses an in-memory SPA framework and static CDN delivery to strictly enforce EU data residency requirements at the edge. Client-side resilience mechanisms and strict API Gateway validation ensure high performance under 800ms while maintaining robust security and accessibility standards.