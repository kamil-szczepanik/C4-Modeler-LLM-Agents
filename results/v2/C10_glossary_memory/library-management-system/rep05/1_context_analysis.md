## Overview
The Library Management System provides self-service portals, circulation management, and cataloguing for public and academic libraries. It guarantees EU-only data residency and meets strict performance SLAs for search.

## Key Elements
* **Library Patrons & Staff:** Actors interacting via HTTPS/TLS.
* **Library Management System:** Core software system boundary.
* **EU-Hosted Cloud Infrastructure:** AWS Frankfurt/Dublin region-pinned deployment environment.
* **Third-Party Digital Content Providers:** External system integrated via REST APIs.
* **Payment Gateway:** External system for processing fines and fees.
* **Notification Service:** External system for patron alerts via Webhooks/SMTP.
* **EU-edge Reverse Proxy:** Edge-caching and CDN layer with WAF and rate limiting.

## Relationships
* **Patrons/Staff to Edge Proxy:** HTTPS/TLS 1.3, OIDC/OAuth2 authentication (with MFA for staff).
* **System to Content Providers:** REST/JSON over HTTPS with circuit breakers and fallback caching.
* **System to Payment Gateway:** HTTPS/REST for secure financial transactions.
* **System to Notification Service:** Webhooks/SMTP with HMAC cryptographic message signing.

## Technology Stack
* **AWS Frankfurt/Dublin:** Region-pinned cloud infrastructure to enforce EU-only data residency.
* **OIDC/OAuth2:** Perimeter authentication protocol for all actors.
* **TLS 1.3 / mTLS:** Transport encryption protocols across all context boundaries.
* **EU-edge Reverse Proxy:** CDN and caching layer for static assets and search queries to achieve <800ms 99th-percentile SLA (R-05).

## Rationale
The architecture strictly enforces EU data residency and robust security controls through regional cloud pinning and TLS/OAuth2 standards. Distributed tracing, edge caching, and circuit-breaker patterns ensure high availability and meet the sub-800ms search performance requirement.