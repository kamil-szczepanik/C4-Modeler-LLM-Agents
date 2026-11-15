## Overview
The Library Management System is a cloud-hosted solution for public and academic libraries to catalogue physical and digital items, manage circulation, and provide self-service portals. It enforces strict EU-only data residency while maintaining a 99th-percentile search response under 800 ms.

## Key Elements
* Library Patrons (Students, Public)
* Library Staff and Cataloguers
* Library Administrators
* Library Management System (LMS)
* Enterprise Identity Provider (Auth0/Keycloak EU)
* Payment Gateway (Stripe EU)
* Notification Service (SendGrid/Twilio EU)

## Relationships
* Patrons and Staff authenticate against the Enterprise IdP via OIDC over HTTPS (TLS 1.3).
* Patrons and Staff interact with the LMS via HTTPS.
* LMS connects synchronously with the Payment Gateway via HTTPS and mTLS.
* LMS connects asynchronously with the Notification Service via message queues.

## Technology Stack
* OAuth 2.0 / OpenID Connect: Federates user identity and enforces Role-Based Access Control.
* TLS 1.3 and mTLS: Secures data-in-transit and verifies external workload identity.
* AES-256: Encrypts data-at-rest strictly within EU-hosted infrastructure.
* Asynchronous message queues: Decouples notification delivery and payment processing to protect core performance.

## Rationale
This architecture ensures strict compliance with EU data residency regulations while decoupling external dependencies to preserve high performance and circulation continuity. Security controls and asynchronous integrations protect the strict search latency SLA.