## Overview
The Library Management System is a public and academic library solution for cataloging items, managing circulation, and providing self-service portals. It ensures EU-only data residency and meets performance requirements for rapid search responses.

## Key Elements
- Library Patron: External user accessing self-service features
- Librarian / Library Staff: External user managing inventory and circulation
- Web Application: Single-page application (React / TypeScript, EU CDN)
- Patron Portal Module: Component managing catalog browsing, reservations, and profiles
- Staff Dashboard Module: Component managing circulation, cataloging, and admin workflows
- API Client Layer: Component handling Axios HTTP communication, JWTs, and input sanitization
- State Management Core: Component (Zustand) managing localized UI state and session context
- API Gateway: Container (NGINX / Spring Cloud Gateway)
- Core Domain Service: Container (Spring Boot / Java)
- Search Service: Container (Elasticsearch / OpenSearch)
- Async Event Bus: Container (Managed Kafka)
- Database: Container (PostgreSQL)

## Relationships
- Library Patron -> Web Application: Accesses portal features [HTTPS]
- Librarian / Library Staff -> Web Application: Manages inventory and circulation [HTTPS]
- Web Application -> API Gateway: Makes API requests [HTTPS / TLS 1.3 / REST over JSON]
- Patron Portal Module -> API Client Layer: Dispatches requests [In-Memory Function Calls]
- Staff Dashboard Module -> API Client Layer: Dispatches requests [In-Memory Function Calls]

## Technology Stack
- React / TypeScript: UI framework for the Web Application SPA
- EU-localized CDN (AWS CloudFront EU / Cloudflare EU): Static asset delivery for EU data residency
- Zustand: State management for localized UI context
- Axios: HTTP communication layer supporting TLS 1.3
- Sentry EU: EU-hosted Real-User Monitoring and error tracking

## Rationale
The architecture uses a React SPA hosted on an EU CDN to satisfy EU data residency constraints. A decomposed component model with in-memory token storage provides security while maintaining architectural simplicity and performance targets.