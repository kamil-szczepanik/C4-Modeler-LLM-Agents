## Overview
The system is a Library Management System designed for public and academic libraries to catalogue items, manage circulation, and provide self-service portals. It uses a Client-Side SPA/Mobile Container to deliver accessible portals for patrons and library staff while meeting strict EU data residency constraints.

## Key Elements
- Client-Side SPA/Mobile Container (Web/Mobile Technologies)
- Patrons and Library Staff (Users)
- API Gateway Container (NGINX / Kong)
- Core Business Logic / Circulation API Container
- Centralized Observability Container

## Relationships
- Patrons and Library Staff -> Client-Side SPA/Mobile Container: Interacts with self-service portals and staff apps [HTTPS]
- Client-Side SPA/Mobile Container -> API Gateway Container: Sends API requests with correlation IDs [HTTPS (REST/GraphQL)]

## Technology Stack
- OAuth 2.0 / OIDC: Token-based authentication with in-memory storage for XSS mitigation
- TypeScript: Contract-first development with shared OpenAPI/GraphQL schemas to prevent type mismatches
- Core Web Vitals & CI/CD Pipeline: Automated performance and bundle-size threshold monitoring for R-05 (<800ms search response)
- Content Security Policy (CSP): HTTP header delivery for script security and EU data residency enforcement

## Rationale
This architecture ensures secure, low-latency client interactions while strictly enforcing EU data residency rules. Modular design, automated checks, and robust state management guarantee maintainability and high performance for patrons and staff.