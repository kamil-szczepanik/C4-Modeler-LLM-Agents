## Overview
The Library Management System provides cataloging, circulation, and self-service portals for public and academic libraries within EU data residency constraints. The 'Web Application' container delivers a secure, accessible, offline-first user experience.

## Key Elements
- Library Member (Patron), Librarian / Library Staff, Library Administrator
- Web Application (React/TypeScript SPA with IndexedDB/Service Workers)
- API Gateway (NGINX / Spring Cloud Gateway)
- Routing & View Controller Component (React Router)
- State & Synchronization Manager Component (Redux Toolkit + IndexedDB)
- API Client Component (Axios / Fetch + WebSockets)
- Theme & Localization Manager Component
- Telemetry Client Component

## Relationships
- Library Member / Staff / Admin -> Web Application: Accesses portals [HTTPS / REST and WebSockets]
- Web Application -> API Gateway: Forwards user requests [HTTPS / REST and WebSockets]

## Technology Stack
- React/TypeScript: Powers the single-page application for responsive, multi-device UI.
- Redux Toolkit & IndexedDB: Manages local state and offline resilience with Web Crypto API encryption.
- React Router: Handles lazy-loaded view rendering and role-based UI structures.
- Axios / Fetch & WebSockets: Facilitates secure backend communication with OAuth 2.0 token injection.

## Rationale
This architecture ensures < 800ms search performance and WCAG 2.1 AA accessibility while meeting EU data privacy and offline requirements. Client-side component separation secures patron data against XSS and maintains strict trust boundaries.