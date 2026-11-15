## Overview
The Library Management System provides a cataloguing, circulation, and self-service platform for public and academic libraries. It enforces strict EU-only data residency and sub-800ms search performance.

## Key Elements
*   Librarian/Circulation Staff & Library Administrator (Users)
*   Staff Dashboard (Angular SPA Container)
*   Circulation Module (Angular Feature Module)
*   Catalogue & Inventory Module (Angular Component)
*   Admin & Reporting Module (Angular Component)
*   API Client Service (Angular Service)
*   API Gateway (Nginx/Kong)
*   External Identity Provider (IdP)

## Relationships
*   Librarian/Circulation Staff -> Staff Dashboard: Accesses system [HTTPS (TLS 1.3)]
*   Library Administrator -> Staff Dashboard: Administers system [HTTPS (TLS 1.3)]
*   Staff Dashboard -> API Gateway: Routes all API requests [HTTPS (TLS 1.3)]
*   Staff Dashboard -> External Identity Provider: Authenticates via OIDC

## Technology Stack
*   Angular SPA: Chosen for reactive forms, lazy-loading, and high-throughput staff operations.
*   HTTPS (TLS 1.3): Enforces secure data transmission across network boundaries.
*   OpenID Connect (OIDC) & JWT: Manages secure, in-memory staff authentication and short-lived sessions.

## Rationale
Centralizing all traffic through the API Gateway simplifies cross-cutting security, enforces the EU data residency constraint, and ensures a single trust boundary. Decomposing the Angular SPA into optimized feature modules supports sub-5-second checkouts and strict RBAC auditability.