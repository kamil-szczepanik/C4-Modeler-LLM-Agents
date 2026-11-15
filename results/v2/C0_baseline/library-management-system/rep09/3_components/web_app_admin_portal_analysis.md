## Overview
[The system is a Library Management System providing cataloging, circulation management, and self-service portals for public and academic libraries. Its core purpose is to deliver secure, performant access for patrons and staff while adhering strictly to EU data residency constraints.]

## Key Elements
- Web App / Admin Portal (React, Node.js SSR container)
- SSR Router & Auth Middleware
- Patron Search Component (React)
- Dashboard & Circulation View (React)
- State & API Client (React Query/Axios)
- API Gateway
- EU Identity Provider (IdP)
- Centralized Log & Metrics Aggregator

## Relationships
- Library Patrons / Librarians / Administrators -> Web App / Admin Portal: Accesses via HTTPS/TLS 1.3
- SSR Router & Auth Middleware -> API Gateway: Forwards authenticated requests via HTTPS/REST [TLS 1.3]
- SSR Router & Auth Middleware -> Centralized Log & Metrics Aggregator: Streams anonymized telemetry via HTTPS/OTLP
- Patron Search Component & Dashboard Component -> State & API Client: Manages local data state via React state management

## Technology Stack
- React: Powers dynamic, role-based UI components for patrons and staff.
- Node.js SSR: Handles server-side rendering, session routing, and security enforcement.
- React Query/Axios: Manages client-side caching to meet sub-800ms search performance (R-05).
- HttpOnly, SameSite=Strict Cookies: Stores JWT sessions securely to mitigate XSS risks.
- OpenTelemetry: Captures structured logs and metrics for SLA monitoring with PII masking.

## Rationale
[This architecture satisfies EU data residency and strict security mandates by enforcing server-side token validation, PII masking, and isolated cookie storage. Furthermore, client-side caching and Node.js SSR optimization directly achieve the required 99th-percentile search response time of under 800 ms.]