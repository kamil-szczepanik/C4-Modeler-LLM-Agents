## Overview
The Library Management System is an enterprise platform enabling public and academic libraries to catalogue physical and digital items, manage circulation, and provide self-service portals. It enforces strict EU-only data residency and sub-800ms search performance requirements.

## Key Elements
* Library Management System: Core enterprise software system hosted within an EU Cloud Hosting Provider.
* Library Staff: Person using the system for cataloging and circulation.
* Library Patrons: Person using the self-service portal for search and borrowing.
* Payment Gateway: External system processing tokenized fines and fees over HTTPS/REST.
* National Library Registry: External system syncing bibliographic data via SOAP/REST.
* Identity Provider: External/internal system handling centralized OIDC/OAuth 2.0 authentication.
* EU Cloud Hosting Provider: Infrastructure boundary utilizing ISO 27001-certified EU data centers.

## Relationships
* Library Staff -> Library Management System: HTTPS (Web UI) with OAuth 2.0/OpenID Connect MFA.
* Library Patrons -> Library Management System: HTTPS (Mobile/Web App) via OIDC.
* Library Management System -> Payment Gateway: HTTPS/REST (tokenized, EU-hosted region).
* Library Management System -> National Library Registry: SOAP/REST with mTLS and circuit breakers.
* Library Management System -> Identity Provider: HTTPS/OIDC for token validation.

## Technology Stack
* TLS 1.3 and mTLS: Mandated for all external and inter-system API transport security.
* AES-256: Enforced for data at rest using an EU-hosted KMS for patron PII and tokens.
* OAuth 2.0 / OpenID Connect: Centralized authentication with RBAC and MFA.
* ISO 27001-certified EU Cloud Hosting: Ensures strict EU-only data residency compliance.

## Rationale
This architecture guarantees strict compliance with EU data residency laws while isolating external system dependencies via circuit breakers to protect core search performance. Security is enforced through robust transport encryption, centralized identity management, and tokenized payment flows.