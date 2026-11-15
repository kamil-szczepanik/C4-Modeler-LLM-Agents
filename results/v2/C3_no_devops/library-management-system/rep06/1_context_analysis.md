## Overview
The Library Management System provides cataloguing, circulation, and self-service portals for public and academic libraries. It ensures EU-only data residency and meets high-performance search requirements.

## Key Elements
- Library Patrons (Students, Public)
- Librarians / Circulation Staff
- Library Administrators
- Library Management System (Core System)
- EU Identity Provider (IdP)
- EU-compliant Payment Gateway
- EU Cloud Hosting Provider (Frankfurt)

## Relationships
- Patrons, Staff, Admins use HTTPS to interact with the Library Management System
- Library Management System communicates via HTTPS/OIDC with the EU Identity Provider
- Library Management System communicates via HTTPS/REST with the Payment Gateway
- Library Management System runs on the EU Cloud Hosting Provider

## Technology Stack
- Keycloak / OAuth2/OIDC for EU Identity Provider authentication
- TLS 1.3 for data in transit and AES-256 for data at rest
- HMAC signatures for webhook verification
- AWS or Azure Frankfurt Region for EU data residency compliance

## Rationale
This architecture enforces strict EU data residency and GDPR compliance using dedicated regional infrastructure. It secures financial and patron data while maintaining high performance for search operations.