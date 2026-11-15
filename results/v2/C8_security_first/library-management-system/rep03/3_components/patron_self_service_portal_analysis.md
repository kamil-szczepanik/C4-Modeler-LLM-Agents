## Overview
The Patron Self-Service Portal is a secure, EU-hosted Single Page Application (SPA) providing public and academic library patrons with catalogue search, circulation management, and self-service capabilities. It ensures high performance, regulatory compliance, and seamless user engagement.

## Key Elements
- Patron Self-Service Portal (React / TypeScript SPA)
- Auth & Session Manager Component (TypeScript / OIDC Client)
- Dashboard & Notification UI Component (React)
- Catalogue & Search Client Component (React / Axios with Circuit Breaker)
- Checkout & Payment UI Component (React with Payment Gateway iFrame SDK)
- API Gateway (Kong / Envoy)
- External Academic Identity Providers & Payment Gateway
- EU-Hosted Content Delivery Network (AWS CloudFront / Cloudflare)

## Relationships
- Patrons -> EU-Hosted CDN: HTTPS [TLS 1.3]
- Auth & Session Manager -> Academic Identity Providers: OAuth 2.0 / OIDC [HTTPS]
- Catalogue & Search Client -> API Gateway: REST / JSON over HTTPS [TLS 1.3]
- Dashboard & Notification UI -> API Gateway: GraphQL / REST over HTTPS [TLS 1.3]
- Checkout & Payment UI -> External Payment Gateway: Tokenized iFrame SDK [HTTPS]
- API Gateway -> Search & Circulation Microservices (Java / Spring Boot): Internal API Routing

## Technology Stack
- React / TypeScript: Modern, component-based frontend framework for building the SPA.
- EU-Hosted CDN (AWS CloudFront / Cloudflare): Guarantees strict EU-only data residency and zero-downtime static asset delivery.
- OAuth 2.0 / OIDC: Secure authentication leveraging existing university credentials.
- HTTP-Only SameSite Cookies & Memory-Only Token Storage: Mitigates XSS and token-theft risks.
- Tokenized iFrame SDK (e.g., Stripe Elements): Isolates payment flows to reduce PCI-DSS scope.
- OpenTelemetry & Real User Monitoring (RUM): Captures 99th-percentile search latencies and browser errors.

## Rationale
This architecture enforces strict EU data residency via localized CDN delivery and encrypted transport layers while isolating untrusted browser clients through robust API Gateway boundaries and tokenized payment frameworks. The component decomposition ensures high performance, strict security compliance, and sub-800ms search responsiveness for patrons.