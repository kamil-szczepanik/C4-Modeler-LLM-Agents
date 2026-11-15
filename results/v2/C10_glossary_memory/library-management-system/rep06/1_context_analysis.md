## Overview
The Library Management System provides cataloging, circulation, and self-service portals for public and academic libraries while strictly enforcing EU data residency. It delivers high-performance search capabilities and role-based access control for diverse user personas.

## Key Elements
* Library Patrons (Students, Public)
* Librarians / Circulation Staff
* Library Administrators
* Library Management System (LMS)
* EU Identity Provider (IdP)
* Payment Gateway
* Digital Content Providers

## Relationships
* Library Patrons, Librarians, Administrators $\rightarrow$ Library Management System via HTTPS (TLS 1.3)
* Library Management System $\rightarrow$ EU Identity Provider via OIDC over HTTPS
* Library Management System $\rightarrow$ Payment Gateway via REST/JSON over HTTPS
* Library Management System $\rightarrow$ Digital Content Providers via API over HTTPS

## Technology Stack
* TLS 1.3: Encrypts all data in transit to ensure robust network security.
* OIDC: Manages authentication and token exchange with the EU IdP.
* REST/JSON: Standardizes communication protocols for external integrations.

## Rationale
This architecture ensures strict compliance with EU data residency and high-performance standards like sub-800ms searches. It securely isolates user roles via boundary-level controls and resilient external integrations.