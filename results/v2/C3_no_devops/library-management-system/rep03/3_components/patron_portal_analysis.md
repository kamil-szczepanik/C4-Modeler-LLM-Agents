## Overview
[The Library Management System provides self-service portals, circulation management, and cataloging for public and academic libraries. It ensures EU data residency compliance and sub-800ms search responses.]

## Key Elements
* Library Patrons (Members)
* Patron Portal (React.js UI SPA & Node.js BFF Server)
* API Gateway (NGINX / Envoy)
* External Identity Provider (IdP)
* Third-Party Payment Gateway
* Catalogue Service & Circulation Service

## Relationships
* Library Patrons -> Patron Portal: Interacts with UI [HTTPS]
* Patron Portal UI -> BFF Server: Communicates via SPA [HTTPS]
* BFF Server -> API Gateway: Proxies API requests [HTTPS/REST, mTLS, OAuth2]
* BFF Server -> External IdP: Manages token exchange [OAuth2/OIDC]
* Patron Portal -> Third-Party Payment Gateway: Processes fines via tokenized iframes [HTTPS]

## Technology Stack
* React.js: UI SPA for patron-facing views ensuring mobile responsiveness
* Node.js / Express: Backend-for-Frontend (BFF) server for secure session management
* HTTP-only, SameSite Cookies: Token storage replacing vulnerable client-side storage
* Stripe Elements / iframes: PCI-DSS scope reduction for payments
* NGINX / Envoy: API Gateway for secure routing

## Rationale
[The BFF pattern secures authentication tokens against XSS while meeting performance and EU data residency constraints. This architecture successfully balances stringent security requirements with low-latency search demands.]