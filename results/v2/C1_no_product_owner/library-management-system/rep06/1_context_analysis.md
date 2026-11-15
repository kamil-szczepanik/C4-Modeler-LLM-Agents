## Overview
The Library Management System provides cataloging, circulation, and self-service portals for public and academic libraries within EU data residency constraints. It ensures high-performance search capabilities while securing external payment and digital content integrations.

## Key Elements
* **Library Management System:** Core software system handling cataloging, circulation, and search.
* **Library Patron:** End-user accessing self-service portals to search and borrow items.
* **Librarian / Library Staff:** Administrative users managing inventory and circulation desk operations.
* **Payment Gateway:** External system handling fines and fees.
* **Digital Content Provider:** Third-party APIs for streaming and downloading digital assets.

## Relationships
* **Patron -> Library Management System:** HTTPS (Web/Mobile) for catalog search and loan management.
* **Librarian -> Library Management System:** HTTPS for inventory and circulation control.
* **Library Management System -> Payment Gateway:** REST/HTTPS with mutual TLS (mTLS) for fine payments.
* **Library Management System -> Digital Content Provider:** REST/HTTPS with mTLS for digital asset access.

## Technology Stack
* **Cloud Infrastructure:** EU-central cloud regions (Frankfurt/Ireland) with multi-AZ failover for data residency and high availability.
* **Transport & Security:** TLS 1.3 for HTTPS traffic, mTLS for external integrations, and AES-256 for data at rest.
* **Authentication & Authorization:** OAuth 2.0 / OpenID Connect with Role-Based Access Control (RBAC).
* **Search & Performance:** Internal dedicated search index isolated within the EU boundary to meet performance SLAs.

## Rationale
This architecture enforces strict EU data residency and robust security boundaries while insulating internal search performance from external network latency. Asynchronous integrations and dedicated regional search infrastructure reliably achieve sub-800ms search response targets.