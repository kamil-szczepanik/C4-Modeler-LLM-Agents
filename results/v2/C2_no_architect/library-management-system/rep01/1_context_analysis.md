## Overview
The Library Management System provides cataloging, circulation management, and self-service portals for public and academic libraries. It ensures EU-only data residency and meets strict performance SLAs for patron searches.

## Key Elements
* **Library Patrons:** Students and public users accessing self-service portals.
* **Librarians / Circulation Staff:** Internal users managing inventory and daily circulation.
* **Library Administrators:** Internal users managing reporting and system access.
* **Notification Gateway:** External system for automated overdue and borrowing alerts.
* **External ILS / Book Supplier Integration:** External system for automated catalog updates.
* **Reporting & Analytics System:** Engine for tracking circulation trends and ROI.
* **Centralized Logging & SIEM Service:** Observability service for telemetry and security audits.

## Relationships
* **Patrons to System:** Interact via HTTPS over TLS 1.3 with rate-limiting and MFA.
* **Staff to System:** Authenticated via enterprise SSO with role-based access control.
* **System to Notification Gateway:** Dispatches automated digital alerts.
* **System to ILS / Book Supplier:** Connects via mutual TLS (mTLS) with cryptographically signed JWT/HMAC payloads.
* **System to SIEM / Analytics:** Streams asynchronous, pseudonymized operational telemetry and audit logs.

## Technology Stack
* **Encryption:** TLS 1.3 for transport layer; AES-256 for data at rest to meet GDPR.
* **Authentication:** Enterprise SSO with step-up auth for staff; MFA for patrons.
* **Integration Protocols:** mTLS and JWT/HMAC for secure supply chain communications.
* **Infrastructure:** EU-only cloud deployment regions to enforce data residency constraints.

## Rationale
This architecture segregates unauthenticated public traffic from internal administrative workloads to protect patron PII and meet GDPR requirements. Asynchronous data pipelining and decoupled integrations safeguard the <800 ms search SLA.