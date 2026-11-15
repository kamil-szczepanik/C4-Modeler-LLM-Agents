## Overview
The Library Management System is a solution for public and academic libraries to catalogue items and manage circulation. It provides self-service portals while enforcing strict EU-only data residency.

## Key Elements
* Patrons and Library Staff (Human Users)
* Library Management System (System-of-Interest)
* External Identity Providers (SSO/OAuth)
* Payment Gateways
* External Archival/Reporting System

## Relationships
* Patrons and Staff interact via HTTPS/API Gateway
* Library Management System authenticates via OIDC/OAuth with External Identity Providers
* Library Management System processes fees via HTTPS with Payment Gateways
* Library Management System exports compliance data via secure batch transfers to External Archival/Reporting System

## Technology Stack
* HTTPS/REST APIs for inbound traffic and boundary entry points
* OAuth 2.0 / OIDC for external identity federation
* Decoupled search indexing architecture to meet the < 800 ms p99 search requirement

## Rationale
This architecture strictly bounds external dependencies to enforce EU-only data residency compliance. Decoupling search and transactional operations ensures the system meets high-performance search requirements.