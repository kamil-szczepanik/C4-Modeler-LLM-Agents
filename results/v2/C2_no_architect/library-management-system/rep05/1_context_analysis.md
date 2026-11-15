## Overview
The Library Management System provides self-service portals and circulation management for academic and public libraries. It ensures strict EU-only data residency and high-performance search capabilities.

## Key Elements
* Library Patrons (Students, Public Citizens)
* Librarians / Circulation Staff
* Library Administrators
* Library Management System
* Catalogue Database (Transactional & Read Replica)
* External Institutional BI Tools / Municipal Dashboards

## Relationships
* Library Patrons to Library Management System via HTTPS (TLS 1.3)
* Librarians/Administrators to Library Management System via OAuth2/OIDC with MFA
* Library Management System to Catalogue Database via AES-256 encrypted connections
* Library Management System to External BI Tools via mTLS API push with pseudonymized data

## Technology Stack
* TLS 1.3: Enforces secure external traffic encryption
* AES-256: Secures data at rest for the catalogue database and read replica
* OAuth2/OIDC: Manages token-based federation and authentication for staff
* Read Replica: Isolates heavy analytical queries to protect transactional performance

## Rationale
This architecture ensures strict GDPR compliance and EU data residency while protecting the critical R-05 search performance requirement through read replicas and strict trust boundaries.