## Overview
The Library Management System provides cataloguing, circulation, and self-service portals for public and academic libraries. It ensures strict EU-only data residency while meeting high-performance search requirements.

## Key Elements
* Library Management System (Software System)
* Library Patron (Person)
* Librarian / Staff (Person)
* Payment Gateway (External System)
* National Library Registry (External System)
* Third-Party IdP / Academic SSO (External System)
* Notification System (External System)
* CDN / Edge Caching Layer (System Component)

## Relationships
* Library Patron & Librarian -> CDN (HTTPS, TLS 1.3)
* Library Management System <-> Third-Party IdP (SAML 2.0 / OIDC over HTTPS)
* Library Management System -> Payment Gateway (HTTPS/REST, tokenized PAN)
* Library Management System -> National Library Registry (HTTPS/REST)
* Library Management System -> Notification System (HTTPS/REST)

## Technology Stack
* OAuth 2.0 / OIDC / SAML 2.0: For federated authentication and MFA compliance
* TLS 1.3 / HTTPS: Mandatory encryption for all perimeter and external traffic
* CDN / Edge Caching: Implemented to achieve the < 800 ms p99 search response (R-05)
* W3C Trace Context: Mandated for distributed tracing across EU cloud regions

## Rationale
This architecture integrates federated identity and edge caching to satisfy user experience goals and the strict search performance requirement. Regional pinning and strict boundary controls ensure full compliance with EU-only data residency mandates.