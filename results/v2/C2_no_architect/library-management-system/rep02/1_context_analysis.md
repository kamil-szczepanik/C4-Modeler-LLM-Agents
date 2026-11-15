## Overview
The Library Management System provides cataloguing, circulation, and self-service portals for public and academic libraries. It guarantees strict EU-only data residency and high-performance search capabilities.

## Key Elements
* Library Patrons (Students, Public)
* Librarians / Circulation Staff
* Library Administrators
* Library Management System (Core System)
* External Identity Provider (SSO)
* External Payment Gateway
* Interlibrary Loan (ILL) Network

## Relationships
* Patrons and Staff interact with the Library Management System via HTTPS using TLS 1.3 and OAuth 2.0 / OpenID Connect.
* Core System integrates with external Payment Gateways and SSO Providers using automated secrets management within the EU perimeter.
* Core System connects to the Interlibrary Loan (ILL) Network using mutual TLS (mTLS), API signature validation, and circuit breakers.

## Technology Stack
* Hosting Infrastructure: EU-Central AWS/Azure regions provisioned via Infrastructure as Code (IaC) for repeatable deployments.
* Security & Auth: OAuth 2.0 / OpenID Connect for authentication; AES-256 for data at rest; EU-hosted Key Management Service (KMS).
* Observability & Monitoring: Centralized APM strategy to track 99th-percentile search performance (<800ms) and SIEM integration for audit logging.

## Rationale
This architecture enforces strict regional boundaries and robust data protection to ensure full GDPR compliance for EU public and academic sectors. Circuit breakers, TLS 1.3, and automated secrets management protect system performance and security against external dependencies.