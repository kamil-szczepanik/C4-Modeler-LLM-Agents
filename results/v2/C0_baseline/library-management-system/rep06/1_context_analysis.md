## Overview
The Library Management System is a comprehensive platform for public and academic libraries to catalogue physical and digital items, manage circulation, and provide self-service portals. It ensures strict EU-only data residency and sub-second search performance.

## Key Elements
* **Library Patrons:** End-users accessing self-service search and borrowing portals.
* **Librarians / Circulation Staff:** Users managing daily cataloguing and circulation.
* **Library Administrators:** Users handling reporting, analytics, and system inventory.
* **Library Management System (LMS):** The core internal software platform.
* **Identity Provider (IdP):** External system for authentication and MFA.
* **Payment Gateway:** External system for processing fines and fees.
* **EU Cloud/CDN Provider:** Edge infrastructure for content delivery and latency reduction.

## Relationships
* Patrons, Staff, and Administrators interact with the *LMS* via HTTPS over Web/Mobile UI.
* *LMS* integrates with the *IdP* via OAuth 2.0 / OpenID Connect over TLS 1.3.
* *LMS* integrates with the *Payment Gateway* via REST APIs over TLS 1.3.
* Internal containers communicate securely using Mutual TLS (mTLS).

## Technology Stack
* **OAuth 2.0 / OpenID Connect:** Used via the IdP for secure patron and staff authentication.
* **TLS 1.3:** Enforced across all external and internal communications for transit security.
* **AES-256:** Applied for database encryption at rest to protect PII and borrowing history.
* **REST APIs:** Protocol utilized for secure communication with the Payment Gateway.
* **HashiCorp Vault / SPIFFE/SPIRE:** Used for dynamic secret management and workload token generation.

## Rationale
This architecture uses dedicated EU-hosted cloud infrastructure and strict data-at-rest encryption to fully satisfy the mandatory EU-only data residency constraint. Furthermore, it incorporates edge CDN delivery, mTLS microsegmentation, and containerized scalability to reliably achieve the sub-800ms search performance requirement.