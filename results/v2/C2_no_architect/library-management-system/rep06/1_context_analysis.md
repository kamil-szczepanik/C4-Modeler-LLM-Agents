## Overview
The Library Management System provides self-service portals and circulation management for public and academic libraries within an EU-only data residency constraint. It catalogues physical and digital items while guaranteeing a 99th-percentile search response under 800ms.

## Key Elements
* **People:** Library Patrons, Librarians/Circulation Staff, Library Administrators
* **Core Systems:** Library Management System (internal EU infrastructure)
* **External Systems:** EU-hosted Identity Provider (IdP), CDN/WAF Edge Services, Digital Content Vendors / Third-Party E-Resource Providers

## Relationships
* **Patrons, Staff, Administrators -> CDN/WAF:** Accesses portals via TLS 1.3
* **CDN/WAF -> Library Management System:** Forwards traffic via mutual TLS (mTLS)
* **Library Management System -> EU-hosted IdP:** Authenticates users via OpenID Connect (OIDC)
* **Library Management System -> Digital Content Vendors:** Integrates via OAuth2 bearer tokens and mTLS with asynchronous caching

## Technology Stack
* **Edge & Security:** CDN/WAF Edge Services, TLS 1.3, mutual TLS (mTLS), AES-256 (data at rest)
* **Authentication:** EU-hosted Identity Provider (IdP) using OpenID Connect (OIDC) with multi-factor authentication (MFA)
* **Integration:** OAuth2 bearer tokens for secure vendor API communication

## Rationale
* Enforces strict EU data residency compliance and robust perimeter defense via an EU-hosted IdP and CDN/WAF.
* Protects the 99th-percentile search response SLA (<800ms) using edge caching, asynchronous synchronization, and circuit breaking against vendor outages.