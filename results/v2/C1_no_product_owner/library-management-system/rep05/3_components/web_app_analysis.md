## Overview
The Library Management System provides cataloguing, circulation, and self-service portals for public and academic libraries within EU-only data residency constraints. The Web App container is a secure, single-page application built for patrons and staff.

## Key Elements
- **Patron & Librarian/Staff**: End users accessing portals via browser.
- **Web App**: React/TypeScript SPA served by Nginx.
- **UI Router & State Management**: React Router and Zustand handling client-side routing, state, and in-memory JWT storage.
- **Catalogue & Circulation Modules**: Components handling item browsing, search, checkouts, and renewals.
- **API Client**: Axios-based client for Kong/Spring Cloud Gateway communication with interceptors and CSRF mitigation.
- **Telemetry & Error Boundary Module**: Component capturing performance metrics and sanitizing errors for Sentry.

## Relationships
- Patron / Librarian -> Web App: Accesses portals [HTTPS, TLS 1.3]
- Web App (Nginx) -> API Gateway (Kong): Sends API requests [HTTPS/JSON]
- UI Router -> Catalogue & Circulation Modules: Delegates views [In-memory / React Props]
- Modules -> API Client: Sends requests [In-memory]
- API Client -> API Gateway: Communicates with backend [HTTPS/JSON]
- Telemetry Module -> Sentry: Transmits sanitized telemetry [HTTPS/JSON, EU region only]

## Technology Stack
- **React / TypeScript / Vite**: Frontend framework for type-safe SPA development.
- **Nginx**: High-performance web server serving static assets with strict CSP and security headers.
- **Zustand**: Lightweight state management keeping JWTs strictly in-memory.
- **React Router**: Client-side routing with role-based guards.
- **Axios**: HTTP client for API integration with error interception.
- **Sentry SDK**: Error tracking and Real User Monitoring with PII sanitization.

## Rationale
This architecture ensures secure, low-latency delivery of the frontend while strictly adhering to EU data residency and XSS prevention mandates. In-memory token storage and strict Content Security Policies protect against client-side vulnerabilities.