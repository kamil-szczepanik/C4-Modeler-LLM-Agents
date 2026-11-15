## Overview
The Librarian Dashboard is a secure, high-performance React-based Single Page Application (SPA) providing library staff with tools for catalog management, circulation, and administrative analytics. It connects exclusively via an API Gateway to backend microservices while adhering to strict EU data residency requirements.

## Key Elements
- Librarian Dashboard (React SPA container)
- Authentication Wrapper (React Context / OIDC Client component)
- Catalog Management Module (Lazy-loaded React component)
- Circulation & Overdue Handler (React component)
- Analytics & Admin Console (React component)
- API Client Layer (Axios/Fetch wrapper component)
- State & Routing Management (React Router & Zustand/Context)
- API Gateway (Kong/Envoy)

## Relationships
- Librarians, Catalogers, and Library Administrators -> Librarian Dashboard: Manages catalog, circulation, and configurations [HTTPS]
- Librarian Dashboard -> API Gateway: Makes API requests with short-lived tokens and idempotency headers [HTTPS (REST/GraphQL)]
- Librarian Dashboard -> EU-restricted CDN (e.g., AWS CloudFront): Serves static immutable assets [HTTPS]

## Technology Stack
- React: Powers the component-based user interface for rapid bundle optimization
- OAuth 2.0 / OIDC: Secures user sessions with in-memory token storage
- Zustand / React Router: Manages local application state and role-based route guards
- Axios / Fetch: Handles API requests with centralized error handling and exponential backoff retry logic
- AWS CloudFront (EU edge-node restricted): Deploys static SPA assets to satisfy data residency constraints

## Rationale
The component-based React architecture ensures rapid, lazy-loaded workflow efficiency and WCAG 2.1 AA accessibility for power users. Deploying via an EU-restricted CDN with in-memory token handling and strict API Gateway integration fulfills regional data protection mandates and sub-second performance goals.