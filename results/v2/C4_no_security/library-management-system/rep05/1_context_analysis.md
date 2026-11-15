## Overview
The Library Management System provides catalogue management, circulation, and self-service portals for public and academic libraries. It ensures high-performance operations and compliance with strict regulatory constraints.

## Key Elements
* Library Patrons (Students, Public users)
* Librarians and Circulation Staff
* Library Administrators
* Core Library Management System-of-Interest
* Payment Gateway (Stripe/Adyen)
* Notification Service (SendGrid/Twilio)
* Identity Provider (Keycloak / OAuth2/OIDC)
* External Academic Identity Federation (SAML/EduPerson)
* Digital Content Repositories and Publishers
* Centralized Observability Platform (Prometheus/Grafana/Loki)

## Relationships
* Patrons and Staff interact with the System-of-Interest via HTTPS/REST for self-service and cataloging.
* System-of-Interest connects to the Payment Gateway via HTTPS/REST for fine processing.
* System-of-Interest utilizes the Notification Service via HTTPS/REST for alerts.
* System-of-Interest integrates with the Identity Provider and Academic Identity Federation via OAuth2/OIDC/SAML for authentication.
* System-of-Interest fetches digital content via HTTPS/REST from Publishers.

## Technology Stack
* OAuth2/OIDC & SAML: Centralized authentication and institutional single-sign-on.
* Prometheus/Grafana/Loki: Centralized observability stack deployed in EU infrastructure.
* HTTPS/REST: Standard secure protocol for all external and internal API communications.

## Rationale
This architecture uses dedicated identity providers and caching layers to meet stringent performance SLAs. Enforcing EU-region routing across all external APIs guarantees compliance with data residency constraints.