## Overview
A secure, cloud-native Patron Self-Service Portal for the Library Management System enables public and academic library patrons to discover catalogue items, manage loans, and settle fines. The architecture guarantees EU-only data residency and maintains a 99th-percentile search response time under 800 ms.

## Key Elements
• Library Patrons (Person)
• Patron Self-Service Portal (React / TypeScript SPA/Mobile App)
• UI Routing & Layout Component
• Catalogue Search & Discovery Component
• Loan & Account Management Component
• Payment & Fine Settlement Component
• Digital Content Viewer Component
• API Gateway (NGINX / Kong)
• Circulation & Loan Service (Node.js / Express)
• Identity Provider (Keycloak / Auth0 EU)
• Payment Gateway (Adyen / Stripe EU)
• Digital Content Providers (External e-Book Vendors)

## Relationships
• Patron Self-Service Portal -> API Gateway: HTTPS / TLS 1.3
• Patron Self-Service Portal -> Identity Provider: OIDC / OAuth 2.0 over HTTPS with PKCE
• Payment & Fine Settlement Component -> Circulation & Loan Service: REST / HTTPS over TLS 1.3 via Gateway
• Digital Content Viewer Component -> Digital Content Providers: REST / HTTPS over TLS 1.3

## Technology Stack
• React / TypeScript: Powers the SPA components with client-side state management and WCAG 2.1 AA accessibility compliance.
• EU Edge CDNs: Implements immutable caching and strict cache-control headers for static SPA assets to meet performance and EU data residency constraints.
• Tokenized Payment Frames: Secures financial transactions by preventing cardholder data from touching the browser, ensuring PCI-DSS scope separation.
• Memory-Only Token Storage: Mitigates XSS risks by avoiding `localStorage` for JWT access tokens.

## Rationale
Decomposing the Patron Self-Service Portal into specialized React components ensures an intuitive, mobile-responsive user experience while strictly adhering to EU data residency. Routing payments and sensitive operations through backend services isolates PCI-DSS compliance and protects patron privacy.