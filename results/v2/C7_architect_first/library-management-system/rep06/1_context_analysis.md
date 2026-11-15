## Overview
The Library Management System provides cataloging, circulation, and self-service portals for public and academic libraries within EU infrastructure. It ensures high-performance search capabilities and secure external integrations while maintaining strict EU-only data residency.

## Key Elements
- **Library Patrons:** End-users accessing public catalogs and self-service portals.
- **Library Staff:** Administrative users managing cataloging and circulation.
- **Library Management System:** Core software system handling business logic and data.
- **External Payment Gateway:** Third-party system for processing fines and fees.
- **Digital Content Repositories:** External systems for streaming and downloading digital items.

## Relationships
- **Patrons & Staff to Library Management System:** HTTPS/TLS 1.3 via dedicated Patron Self-Service and Staff Management interfaces.
- **Library Management System to External Payment Gateway:** mTLS over HTTPS for secure financial transactions.
- **Library Management System to Digital Content Repositories:** mTLS over HTTPS with OpenID Connect (OIDC) SSO handoffs.

## Technology Stack
- **EU-Region Cloud Infrastructure:** Mandated to strictly satisfy EU-only data residency and GDPR constraints.
- **TLS 1.3 & mTLS:** Utilized for all client-to-system and machine-to-machine communications to ensure data security in transit.
- **OpenID Connect (OIDC) / OAuth 2.1:** Implemented for federated authentication, multi-factor authentication (MFA), and seamless SSO integration.
- **AES-256:** Deployed for robust data encryption at rest within EU boundaries.
- **Edge WAF & Rate Limiting:** Deployed at the Patron interface to protect against volumetric spikes and meet the search performance requirement.

## Rationale
Separating the Patron and Staff ingress points structurally isolates high-throughput public searches from resource-heavy administrative batch tasks, safeguarding the p99 < 800ms search latency requirement. Enforcing strict EU-only cloud deployment, mTLS boundaries, and Zero Trust security controls ensures full compliance with data residency and privacy mandates.