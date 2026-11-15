## Overview
The Library Management System provides cataloguing, circulation, and self-service portals for public and academic libraries. It ensures strict EU data residency compliance while delivering high-performance search responses under 800ms.

## Key Elements
* Library Patrons (Members)
* Librarians / Circulation Staff
* Library Administrators
* Library Management System (LMS)
* External Identity Provider (IdP)
* Third-Party Payment Gateway
* Digital Content Repositories

## Relationships
* Patrons, Staff, and Administrators interact with the LMS via HTTPS (TLS 1.3) and API Gateway using OAuth 2.0 / OIDC
* LMS authenticates users with the External IdP using OIDC over HTTPS
* LMS processes fines via Third-Party Payment Gateway using REST/HTTPS with mTLS
* LMS fulfills digital items via Digital Content Repositories using LTI/API

## Technology Stack
* OAuth 2.0 / OIDC: For secure patron and staff authentication and token introspection
* JWT (JSON Web Tokens): For short-lived session management with audience and scope validation
* TLS 1.3 and mTLS: For secure external integrations and transport-layer encryption
* AES-256: For encrypting PII at rest within session caches

## Rationale
This architecture uses an API Gateway and scoped JWTs to enforce strict security and RBAC while supporting offline fallback mechanisms. It meets performance and data residency constraints by keeping all operations and data storage within EU-hosted infrastructure.