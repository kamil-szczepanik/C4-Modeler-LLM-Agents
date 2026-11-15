## Overview
[The Administration Console is a secure, React-based Single Page Application (SPA) that empowers Library Administrators to manage reporting, inventory, budgets, and vendor ROI analytics.]

## Key Elements
* Library Administrators [person]
* Administration Console (Web App) [container]
* Authentication Manager [component]
* Dashboard UI Module [component]
* Reporting Engine Client [component]
* Inventory & Budget Management Module [component]
* Vendor Analytics Module [component]
* Identity Provider (Keycloak/Auth0 EU) [externalSystem]
* API Gateway (NGINX / Kong) [container]
* Reporting & Analytics Service (Python / FastAPI) [container]

## Relationships
* Library Administrators -> Administration Console: HTTPS / WAF-protected API Gateway
* Administration Console -> Identity Provider: OIDC / OAuth 2.0 over HTTPS with PKCE
* Administration Console -> API Gateway: REST / HTTPS over TLS 1.3
* Administration Console -> Reporting & Analytics Service: REST / HTTPS over TLS 1.3 via API Gateway

## Technology Stack
* React SPA: Provides a responsive, component-driven user interface for administrative workflows.
* EU-Region Object Storage & CDN: Ensures low-latency delivery, immutability, and compliance with EU-only data residency constraints.
* OIDC / OAuth 2.0 with PKCE: Secures authentication and prevents token interception.
* HTTP-Only, SameSite=Strict Storage: Protects tokens against XSS-based theft.
* Transport Layer Security (TLS 1.3): Encrypts all data in transit across administrative interfaces.

## Rationale
[This architecture enforces strict EU-only data residency and zero-trust security controls while providing high-performance analytics and financial governance for library administrators. The component-driven SPA design combined with robust API boundaries ensures scalability, auditability, and operational resilience.]