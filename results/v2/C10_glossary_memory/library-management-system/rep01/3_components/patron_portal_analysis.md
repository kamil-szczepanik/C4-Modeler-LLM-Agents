## Overview
[A cloud-native Library Management System providing public and academic libraries with item cataloging, circulation management, and self-service portals, adhering strictly to EU data residency constraints.]

## Key Elements
• Library Member (Patron)
• Patron Portal (Web/Mobile Container) (React/TypeScript)
• Catalog Discovery UI [component]
• Loan Management Dashboard UI [component]
• Digital Content Access Handler [component]
• Session & Auth State Manager [component]
• API Gateway / BFF (Nginx/Envoy)
• EU Identity Provider (IdP)
• Anycast CDN / DDoS Protection Service (EU-PoPs)
• EU Monitoring & APM Provider
• Third-Party Digital Content Providers (OverDrive/Libby)

## Relationships
• Library Member (Patron) -> Anycast CDN / DDoS Protection Service (EU-PoPs) [TLS 1.3, HTTPS]
• Anycast CDN / DDoS Protection Service (EU-PoPs) -> API Gateway / BFF [TLS 1.3, HTTPS]
• Catalog Discovery UI -> API Gateway / BFF [HTTPS/REST]
• Loan Management Dashboard UI -> API Gateway / BFF [HTTPS/REST, WSS]
• Session & Auth State Manager -> EU Identity Provider (IdP) [OIDC/OAuth2 via BFF]
• Digital Content Access Handler -> Third-Party Digital Content Providers (OverDrive/Libby) [Server-side OAuth2, HTTPS/REST via BFF]
• Patron Portal -> EU Monitoring & APM Provider [OTLP/HTTPS]

## Technology Stack
• React/TypeScript: Powers the Patron Portal SPA/PWA for mobile-first, WCAG 2.1 AA compliant UI components.
• Nginx/Envoy: Acts as the API Gateway / BFF for edge routing, rate limiting, and TLS termination.
• OIDC/OAuth2: Authenticates users securely via the EU Identity Provider (IdP) with HttpOnly, SameSite cookies.
• WSS (WebSockets): Enables real-time loan status updates with message-level authorization.
• Anycast CDN / DDoS Protection Service (EU-PoPs): Delivers static assets exclusively from EU points of presence.

## Rationale
[Decomposing the Patron Portal into distinct React components ensures high-priority user journeys remain performant and meet the sub-800ms search latency requirement. Enforcing strict EU edge caching, server-side token handoffs, and HttpOnly cookies guarantees compliance with EU-only data residency and rigorous security mandates.]