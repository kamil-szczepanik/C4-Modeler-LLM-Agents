## Overview
[A secure, enterprise-grade Staff Web App built with Angular and TypeScript for librarians and library administrators. It provides robust administrative workflows, catalog management, and offline-resilient circulation desks while enforcing strict EU data residency.]

## Key Elements
- Librarians
- Library Administrators
- Staff Web App (Angular, TypeScript)
- Circulation Desk Component (Angular)
- Catalog Management Component (Angular)
- Admin Dashboard Component (Angular)
- Auth Guard & State Service (Angular)
- Core API Gateway (Envoy, Spring Cloud Gateway)
- EU Identity Provider (IdP) (OIDC)

## Relationships
- Librarians -> Staff Web App [HTTPS, TLS 1.3]
- Library Administrators -> Staff Web App [HTTPS, TLS 1.3]
- Staff Web App -> Core API Gateway [HTTPS, TLS 1.3]
- Auth Guard & State Service -> EU Identity Provider (IdP) [OIDC over HTTPS]
- Circulation Desk Component -> Circulation Service via Core API Gateway [HTTPS, TLS 1.3]
- Catalog Management Component -> Catalog & Search Service via Core API Gateway [HTTPS, TLS 1.3]

## Technology Stack
- Angular & TypeScript: Chosen for robust client-side routing, reactive forms, and modular enterprise architecture.
- Web Crypto API (AES-GCM): Used for secure encryption at rest of offline-buffered circulation data in IndexedDB.
- OIDC over HTTPS: Enforces token exchange and authentication with the EU Identity Provider.
- Envoy & Spring Cloud Gateway: Manages secure routing and API traffic boundaries.

## Rationale
[This architecture ensures high-performance administrative workflows and offline-resilient circulation operations while maintaining strict EU data security and compliance standards. Modular component design minimizes desk latency and administrative overhead.]