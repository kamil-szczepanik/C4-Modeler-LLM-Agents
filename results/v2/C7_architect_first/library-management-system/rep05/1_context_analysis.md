## Overview
The Library Management System is a multi-tenant cloud SaaS platform designed to catalogue physical and digital items, manage circulation, and provide self-service portals for academic and public libraries. It ensures strict EU data residency and high-performance search SLAs (<800 ms).

## Key Elements
*   **System-of-Interest**: Library Management System (LMS) hosted in EU regions (Frankfurt/Dublin).
*   **Users**: Library Patron, Academic Researcher, Librarian / Administrator, Library Manager.
*   **External Systems**: EU-Compliant Payment Gateway, Third-Party Notification Service, External Identity Provider (IdP).
*   **Infrastructure**: Edge CDN, Global Geo-DNS, EU-centralized cloud nodes, Audit Log Sink.

## Relationships
*   **Users $\rightarrow$ LMS**: HTTPS (TLS 1.3) with OAuth 2.0 / OIDC and MFA for web portals and admin dashboards.
*   **LMS $\rightarrow$ Payment Gateway**: REST over mTLS with webhook signature verification and tokenized payments.
*   **LMS $\rightarrow$ Notification Service**: REST API over HTTPS with circuit-breaker pattern for due-date alerts.
*   **LMS $\rightarrow$ Identity Provider**: OIDC/OAuth 2.0 for user authentication and RBAC/ABAC mapping.

## Technology Stack
*   **Cloud Platform**: Multi-tenant EU-hosted SaaS with AES-256 encryption and customer-managed keys (CMK) for data at rest.
*   **Security Protocols**: TLS 1.3, mTLS, OAuth 2.0, OpenID Connect (OIDC).
*   **Performance & Routing**: Global load balancing with EU Geo-DNS and Edge CDN for static assets.
*   **Compliance & Observability**: Centralized audit log sink and automated synthetic monitoring across EU points-of-presence.

## Rationale
The architecture enforces strict EU data residency via regionally restricted cloud nodes and TLS transport. It guarantees sub-800ms search performance (R-05) through edge caching, global load balancing, and resilient third-party integrations.