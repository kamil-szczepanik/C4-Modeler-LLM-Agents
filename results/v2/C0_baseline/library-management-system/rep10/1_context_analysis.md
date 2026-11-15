## Overview
The Library Management System provides cataloging, circulation, and self-service portals for public and academic libraries. It enforces strict EU-only data residency and high-performance search capabilities.

## Key Elements
* Library Patrons (Students, Public Citizens)
* Librarians and Circulation Staff
* Library Administrators
* Library Management System (Core Software System)
* External Notification Service (EU-hosted)
* External Payment Gateway (EU-compliant)
* External Identity Provider (IdP)
* Interlibrary Loan (ILL) Network
* Observability Platform & SIEM

## Relationships
* Patrons, Librarians, and Administrators interact with the Library Management System via HTTPS (Web/Mobile Clients) using OIDC/OAuth 2.0.
* Library Management System integrates with the Notification Service and Payment Gateway via REST/JSON over TLS 1.3.
* Library Management System queries the ILL Network via HTTPS/REST for cross-library catalog searches.
* Security events and telemetry stream to the Observability Platform and EU-resident SIEM.

## Technology Stack
* OpenID Connect (OIDC) / OAuth 2.0: For centralized authentication and RBAC token issuance.
* TLS 1.3 / mTLS: For secure data-in-transit across all external integrations and internal service communications.
* AES-256: For encrypting patron PII and financial records at rest within EU-based storage regions.
* EU Cloud Infrastructure (Frankfurt/Ireland) with CDN: To satisfy data residency and achieve <800ms search latency.

## Rationale
This architecture uses dedicated regional infrastructure and strict protocol controls to guarantee GDPR compliance and EU data residency. It incorporates resilient third-party integrations and robust security patterns to meet stringent performance and availability demands.