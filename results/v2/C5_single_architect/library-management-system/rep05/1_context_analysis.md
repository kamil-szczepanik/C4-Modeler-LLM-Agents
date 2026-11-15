## Overview
The Library Management System provides cataloging, circulation management, and self-service portals for public and academic libraries. It ensures strict compliance with EU-only data residency constraints while delivering high-performance search capabilities.

## Key Elements
* **Library Management System (Software System):** Core platform for cataloging and circulation.
* **Library Patron (Person):** End-user utilizing self-service portals.
* **Librarian / Staff (Person):** Internal user managing the catalogue and desk operations.
* **Payment Gateway (External System):** Third-party processor for fines and fees.
* **Notification Service (External System):** EU-hosted provider for email and SMS alerts.
* **Digital Rights Management (DRM) Provider (External System):** Manages licensing and access control for digital assets.

## Relationships
* **Library Patron -> Library Management System:** HTTPS via Web/Mobile UI for self-service portals.
* **Librarian / Staff -> Library Management System:** HTTPS via Admin UI for cataloging and circulation.
* **Library Management System -> Payment Gateway:** HTTPS/REST API for transaction processing.
* **Library Management System -> Notification Service:** SMTP and HTTPS APIs using EU-hosted endpoints to satisfy data residency.
* **Library Management System -> DRM Provider:** HTTPS/REST API with OAuth 2.0 for digital asset licensing.

## Technology Stack
* **HTTPS/REST APIs:** Protocol for all internal and external system communications.
* **OAuth 2.0:** Protocol for secure authentication and token verification with the DRM provider.
* **EU-hosted Endpoints:** Architectural deployment choice for external services to strictly enforce EU data residency.

## Rationale
This architecture cleanly separates user interactions from core management and external integrations while enforcing strict geographic data boundaries. Leveraging secure REST APIs and EU-hosted endpoints guarantees compliance with regional constraints without sacrificing performance.