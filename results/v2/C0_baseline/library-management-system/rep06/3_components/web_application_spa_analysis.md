## Overview
The Library Management System provides cataloging, circulation, and self-service portals via a secure React Single-Page Application (SPA). It ensures EU-only data residency and sub-800ms search responses.

## Key Elements
- Web Application (SPA) (React / TypeScript)
- Authentication & Session Manager (`react-oidc-context`)
- Role-Based UI Router (`React Router`)
- API Client Layer (`TanStack Query` / `Axios`)
- Localization & Accessibility Engine (`react-i18next`)
- Offline & State Persistence Manager (`IndexedDB` with `Zustand`)
- API Gateway (Nginx / Kong)
- EU Cloud/CDN Provider

## Relationships
- Library Patrons, Librarians, Administrators -> Web Application (SPA): Accesses portals [HTTPS (TLS 1.3)]
- Web Application (SPA) -> API Gateway (Nginx / Kong): Sends client requests and queries [HTTPS (TLS 1.3)]
- Web Application (SPA) -> EU Cloud/CDN Provider: Serves static assets and enforces CSP [HTTPS (TLS 1.3)]

## Technology Stack
- React / TypeScript: Type-safe, component-driven frontend architecture
- TanStack Query: Client-side data fetching and caching to meet sub-800ms search targets
- `react-oidc-context`: In-memory token management using Authorization Code Flow with PKCE
- `IndexedDB` with `Zustand`: Secure, non-PII offline state caching for patchy Wi-Fi degradation
- OpenTelemetry: Real-user monitoring (RUM) and error boundary tracking

## Rationale
The architecture decouples the frontend to deliver persona-specific, accessible (WCAG 2.1 AA) interfaces while strictly maintaining EU data residency. Client-side caching and in-memory token security optimize performance and protect patron privacy.