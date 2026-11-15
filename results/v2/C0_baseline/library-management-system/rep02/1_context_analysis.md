## Overview
The Library Management System provides cataloguing, circulation management, and self-service portals for public and academic libraries. It is architected within an EU-only data residency boundary to ensure strict regulatory compliance.

## Key Elements
- **Users**: Library Patrons, Librarians/Circulation Staff, Library Administrators
- **Clients**: Web and Mobile Clients
- **Infrastructure**: CDN with EU edge caching, WAF, and DDoS protection
- **Core System**: Library Management System (LMS)
- **External Systems**: EU Identity Provider (Keycloak/Auth0), EU Payment Gateway (Stripe EU), EU Notification Service (SendGrid EU)

## Relationships
- Patrons, Librarians, and Administrators interact with Web/Mobile Clients via HTTPS
- Web/Mobile Clients connect to LMS via CDN using TLS 1.3
- LMS integrates with EU Identity Provider via OAuth2/OIDC
- LMS integrates with EU Payment Gateway and EU Notification Service via REST and mTLS

## Technology Stack
- **Authentication**: OAuth2/OIDC via EU Identity Provider for secure role-based access control
- **Edge Security**: WAF and DDoS protection for perimeter defense
- **Delivery**: CDN with EU edge caching for high-performance static asset delivery and low-latency search
- **Encryption**: TLS 1.3 for client connections and mTLS for system-to-system integrations

## Rationale
This architecture guarantees strict EU data residency compliance while supporting high-performance search requirements through edge caching. It secures user interactions and external integrations using robust perimeter controls and modern cryptographic protocols.