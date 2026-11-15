## Overview
[A responsive web application enabling library patrons to search catalogs, manage accounts, and handle self-service circulation securely. It provides high-performance client-side rendering while enforcing strict EU data residency and security controls.]

## Key Elements
- Library Patrons [Person]
- Patron Web App [Container] (React, TypeScript)
- Search & Discovery UI [Component]
- Account & Circulation Portal [Component]
- Payment Integration Client [Component]
- Auth Client Module [Component] (OIDC Client)
- Core API Gateway [Container] (Envoy, Spring Cloud Gateway)
- EU Identity Provider (IdP) [External System] (OIDC)
- Payment Gateway [External System] (REST/JSON)

## Relationships
- Library Patrons -> Patron Web App [HTTPS, TLS 1.3]
- Search & Discovery UI -> Core API Gateway [HTTPS (TLS 1.3), JSON]
- Account & Circulation Portal -> Core API Gateway [HTTPS (TLS 1.3), JSON]
- Payment Integration Client -> Core API Gateway [HTTPS (TLS 1.3), JSON]
- Auth Client Module -> EU Identity Provider (IdP) [OIDC over HTTPS, TLS 1.3 with PKCE]

## Technology Stack
- React and TypeScript: Chosen for fast, responsive client-side rendering of the self-service portal.
- OIDC with PKCE: Ensures secure authentication and token exchange without credential storage in browser storage.
- HTTPS (TLS 1.3) and JSON: Standardized protocols for secure data in transit across browser and API boundaries.
- Geo-distributed CDN: Enforces EU-only data residency and low-latency static asset delivery.

## Rationale
[This architecture separates concerns into modular UI components while enforcing strict trust boundaries and EU data residency at the edge and gateway layers. It guarantees sub-800ms search responsiveness and secure, PCI-compliant payment workflows for library patrons.]