## Overview
A cloud-hosted SaaS Library Management System (LMS) providing item cataloguing, circulation management, and self-service portals. It guarantees EU-only data residency and sub-800ms search performance.

## Key Elements
- **Library Patrons:** Students and public users accessing self-service portals.
- **Librarians / Circulation Staff:** Users managing inventory cataloguing and circulation.
- **Library Administrators:** Users handling reporting, analytics, and compliance.
- **Library Management System (LMS):** Core cloud-hosted SaaS system containing microservices (API Gateway, Web Frontend, Search Service, Core Circulation Service).
- **Payment Gateway:** Stripe EU / SEPA.
- **Identity Provider:** EU Shibboleth / OAuth2.
- **Notification Service:** SendGrid EU / Twilio.

## Relationships
- **Patrons, Librarians, Administrators to LMS:** HTTPS (TLS 1.3) via web/mobile clients.
- **LMS to Payment Gateway:** HTTPS/REST (PCI-DSS compliant EU endpoints).
- **LMS to Identity Provider:** OIDC / SAML 2.0 over HTTPS.
- **LMS to Notification Service:** HTTPS/REST API.

## Technology Stack
- **Hosting/Deployment:** EU cloud regions ensuring data residency and GDPR compliance.
- **Security Protocols:** TLS 1.3 for transit, mTLS for internal container communication, OAuth2/OIDC for SSO.
- **Encryption:** Cloud KMS with EU-managed cryptographic keys for encryption-at-rest.
- **Search & Core Services:** Microservices architecture optimized for <800ms search response times.

## Rationale
The microservices architecture deployed exclusively within EU regions guarantees the strict data residency constraint while supporting high-performance search capabilities. Comprehensive security controls, including tokenized payments and mTLS, protect sensitive patron and financial data.