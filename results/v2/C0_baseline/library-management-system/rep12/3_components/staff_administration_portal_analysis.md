## Overview
The Library Management System provides cataloging, circulation, and self-service portals for public and academic libraries. The Staff Administration Portal container is designed for frontline librarians and administrators to manage operations securely within EU data residency constraints.

## Key Elements
- **Frontline Librarians & Library Administrators**: Primary users with distinct role-based access control.
- **Staff Administration Portal (Angular / TypeScript)**: Container housing internal Angular components (Circulation Management Module, Administration & Reporting Module, Core State & Auth Service, Client-Side Caching & Offline Fallback Service).
- **API Gateway (Nginx / Spring Cloud Gateway)**: Entry point for backend integration.
- **Identity Provider / SSO**: Manages OIDC/OAuth2 authentication.

## Relationships
- Library Staff -> Staff Administration Portal: Accesses portal via HTTPS.
- Circulation Management Module -> API Gateway: Communicates via HTTPS/REST and WebSockets with circuit breakers and IndexedDB fallback.
- Administration & Reporting Module -> API Gateway: Communicates via HTTPS/REST.
- Core State & Auth Service -> Identity Provider: Authenticates via OIDC/OAuth2 over HTTPS.

## Technology Stack
- **Angular / TypeScript**: Frontend framework chosen for modular component architecture and strict role-based routing.
- **IndexedDB with Web Crypto API (AES-GCM)**: Provides encrypted client-side caching for offline-resilient circulation workflows.
- **Nginx Alpine**: Containerization and static asset delivery behind an edge CDN.
- **OAuth2/OIDC**: Secures authentication tokens stored in secure, HttpOnly, SameSite=Strict cookies or in-memory.

## Rationale
The modular Angular architecture and offline resilience layers isolate heavy analytics from frontline workflows, ensuring the <800ms search SLA. Strict encryption and token handling mechanisms enforce compliance with EU-only data residency constraints.