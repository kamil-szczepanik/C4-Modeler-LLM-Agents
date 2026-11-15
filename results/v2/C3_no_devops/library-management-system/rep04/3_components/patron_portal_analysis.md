## Overview
The Library Management System provides cataloging, circulation management, and self-service portals for public and academic libraries. The system ensures EU-only data residency and sub-800ms search responses.

## Key Elements
* Library Patron (Member)
* Patron Portal (React SPA)
* API Gateway (Nginx/Kong)
* Identity Provider (IdP)
* Core Circulation & Cataloguing Service (Spring Boot)
* Search Service (Elasticsearch)
* Payment Gateway

## Relationships
* Library Patron -> Patron Portal: Accesses self-service portal [HTTPS (TLS 1.3)]
* Patron Portal -> API Gateway: Makes API requests [HTTPS (TLS 1.3)]
* Authentication & Session Manager -> Identity Provider: Manages OIDC tokens [HTTPS/OIDC]
* Account & Loan Dashboard -> Core Circulation Service: Manages loans and preferences [REST/JSON, HTTPS]
* Catalog & Search Interface -> Search Service: Queries item catalog [GraphQL/HTTPS]
* Billing & Payment Widget -> Payment Gateway: Processes self-service fine settlements [HTTPS/SDK]

## Technology Stack
* React SPA: Provides a modern, mobile-responsive self-accessible frontend interface.
* Material-UI / Radix UI: Guarantees built-in keyboard navigation and screen-reader support for WCAG 2.1 AA compliance.
* HttpOnly Cookies: Secures refresh tokens against XSS vulnerabilities.
* Nginx/Kong API Gateway: Enforces CORS, strict rate limiting, and EU data residency routing.

## Rationale
This architecture decouples the self-service patron UI from core services while maintaining strict EU data residency and PCI-DSS compliance. The React SPA ensures high performance and accessibility for diverse library patrons.