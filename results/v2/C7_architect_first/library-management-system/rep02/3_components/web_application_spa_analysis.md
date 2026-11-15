## Overview
The Library Management System provides a unified platform for public and academic libraries to manage item catalogues, circulation, and self-service portals. It enforces strict EU-only data residency and maintains high-performance search capabilities.

## Key Elements
- Web Application (SPA): React and TypeScript client-side interface served via CDN.
- Router & State Management: React Router and Zustand.
- Authentication Module: OpenID Connect/OAuth2 client.
- Catalog & Search UI & Self-Service & Circulation UI: React components.
- API Client: Axios/Fetch API.
- Offline Sync & Optimistic Cache Layer: IndexedDB repository pattern.
- Accessibility & Localization Core: React-Intl and ARIA-compliant primitives.

## Relationships
- Library Patron, Librarian / Staff, Library Administrator -> Web Application (SPA): Uses self-service portals, manages catalogue, and accesses dashboards [HTTPS]
- Web Application (SPA) -> API Gateway: Sends requests [HTTPS / JSON]
- Catalog & Search UI -> API Client: Queries search indices [HTTPS / JSON]
- Self-Service & Circulation UI -> Offline Sync & Optimistic Cache Layer: Persists transient actions [IndexedDB]
- Authentication Module -> API Client: Attaches volatile JWT headers [HTTPS]

## Technology Stack
- React / TypeScript: Core frontend framework for type safety and component reusability.
- EU-Hosted CDN Edge: Ensures zero-downtime releases, asset fingerprinting, and EU data residency compliance.
- Zustand: Manages volatile in-memory JWT tokens to mitigate XSS vulnerabilities.
- IndexedDB: Client-side storage for offline circulation resilience.
- Web Crypto API: Encrypts transient patron borrowing data at rest in the browser.

## Rationale
This architecture ensures robust client-side performance, offline resilience for circulation desks, and strict adherence to EU data residency and security constraints. The component decomposition directly supports low-latency search and role-based workflows for diverse library users.