## Overview
The Library Management System provides cataloging, circulation management, and self-service portals for public and academic libraries. The system ensures EU data residency compliance and strict performance SLAs for rapid item searches.

## Key Elements
- Patrons and Library Administrators / Staff (Users)
- Web App (SPA) (React, Nginx, CDN)
- API Gateway (Spring Cloud Gateway, OAuth2/OIDC)
- Core Services Container (Spring Boot)
- Search Container (Elasticsearch)
- Telemetry Container (Prometheus, Grafana, Fluentbit)
- Database (PostgreSQL, AES-256 encryption)

## Relationships
- Patrons & Staff -> Web App (SPA): Accesses portals and UI via HTTPS with TLS 1.3
- Web App (SPA) -> API Gateway: Sends API requests via HTTPS with TLS 1.3 and JSON
- State Management Layer -> API Client: Executes deduplicated HTTP calls
- Telemetry Wrapper -> Telemetry Container: Forwards anonymized performance metrics via HTTPS

## Technology Stack
- React: Provides a responsive, component-based frontend architecture
- Nginx: Serves static assets and enforces hardened security headers and CSP
- Content Delivery Network (CDN): Delivers EU edge caching and immutable assets
- React Query / Zustand: Implements in-memory state management and caching
- Sentry / Telemetry SDK: Tracks anonymized Real User Monitoring and Core Web Vitals

## Rationale
This architecture ensures high availability, strict EU data residency, and sub-800ms search performance through client-side caching and EU edge delivery. Hardened security measures and WCAG 2.1 AA compliance protect patron privacy while maximizing accessibility across user portals.