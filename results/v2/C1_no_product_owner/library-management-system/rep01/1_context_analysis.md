## Overview
The Library Management System provides cataloging, circulation, and self-service portals for public and academic libraries. It is hosted exclusively within the EU to guarantee strict data residency compliance.

## Key Elements
- Library Patrons & Staff (Actors)
- Library Management System (Software System)
- External Payment Gateway (External System)
- Digital Repository / DRM Provider (External System)
- External Notification Service (External System)
- AWS CloudFront Frankfurt (CDN / Edge)

## Relationships
- Patrons & Staff $\rightarrow$ *AWS CloudFront Frankfurt* $\rightarrow$ *Library Management System* (HTTPS/TLS 1.3, OAuth 2.0/OIDC)
- *Library Management System* $\rightarrow$ *External Payment Gateway* (REST/TLS, PCI-DSS scoped)
- *Library Management System* $\rightarrow$ *Digital Repository* (Asynchronous REST/TLS)
- *Library Management System* $\rightarrow$ *External Notification Service* (mTLS and API keys)

## Technology Stack
- AWS Frankfurt Infrastructure: Selected to enforce EU-only data residency constraints.
- TLS 1.3 & AES-256 (CMK): Mandated for data-in-transit and EU-resident data-at-rest encryption.
- OAuth 2.0 / OpenID Connect (OIDC): Enforces perimeter authentication and MFA for staff.
- AWS CloudFront Frankfurt: Provides edge caching, WAF protection, and DDoS mitigation.
- OpenTelemetry: Utilized for standardized tracing and synthetic monitoring of external dependencies.

## Rationale
This architecture ensures strict EU data residency compliance while isolating third-party dependencies to protect core search performance. Decoupling external repositories and utilizing edge caching guarantees the 99th-percentile search response time remains below 800 ms.