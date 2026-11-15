## Overview
The Patron Web Application is a React-based self-service portal empowering library patrons to discover, borrow, and manage items. It ensures high performance and strict EU-only data residency compliance.

## Key Elements
- Patron Web Application (React / TypeScript SPA)
- Search & Discovery Component (React / TypeScript)
- Account & Circulation Component (React / TypeScript)
- Authentication Boundary Component (React / TypeScript / OIDC Client)
- Digital Checkout & Reader Component (React / TypeScript / PDF.js)
- Notification & Feedback Component (React / TypeScript)
- External Systems: API Gateway, Identity Provider, CDN, Logging & APM

## Relationships
- Library Patron -> Patron Web Application: Accesses portal [HTTPS]
- Search & Discovery Component -> API Gateway: Queries catalogue [HTTPS / REST]
- Account & Circulation Component -> API Gateway: Manages loans and holds [HTTPS / REST]
- Digital Checkout & Reader Component -> API Gateway: Streams digital assets [HTTPS / REST]
- Notification & Feedback Component -> API Gateway: Receives live alerts [WebSocket / WSS]
- Authentication Boundary Component -> Identity Provider: Authenticates patrons [HTTPS / OIDC]

## Technology Stack
- React / TypeScript: Chosen for dynamic, component-based UI development and high client-side interactivity
- OIDC / OAuth 2.0: Ensures secure, standards-based authentication and token exchange
- TLS 1.3: Enforces encrypted data in transit with strong cipher suites
- PDF.js: Renders digital media securely within volatile browser memory
- WebSocket / WSS: Enables real-time patron alerts and notifications

## Rationale
This architecture isolates state-heavy circulation logic from high-frequency search rendering to meet the <800ms search SLA. It also enforces strict EU data residency and robust in-memory token security.