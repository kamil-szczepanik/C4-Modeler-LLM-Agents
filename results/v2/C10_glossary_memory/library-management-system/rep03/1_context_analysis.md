## Overview
- The Library Management System provides cataloging, circulation management, and self-service portals for public and academic libraries.
- The system enforces strict EU-only data residency and maintains a 99th-percentile search response time under 800ms.

## Key Elements
- Library Member (Patron)
- Librarian / Staff
- Library Administrator
- Library Management System (Software System)
- Payment Gateway (External Software System)
- Notification Provider (External Software System)
- Identity Provider (External Software System)

## Relationships
- Users interact with the Library Management System via HTTPS using TLS 1.3.
- Library Management System integrates with Payment Gateway via HTTPS/REST for fine settlements.
- Library Management System integrates with Notification Provider via HTTPS/REST for loan reminders.
- Library Management System authenticates users via Identity Provider using OIDC/OAuth2 over HTTPS.

## Technology Stack
- OIDC/OAuth2: For tiered authentication and user session management.
- TLS 1.3: For encrypted data in transit across all external boundaries.
- AES-256: For data at rest with keys managed in an EU-hosted KMS.
- OpenTelemetry: For centralized distributed tracing to monitor search latency.
- Mutual TLS (mTLS): For Zero Trust inter-container communication.

## Rationale
- Decoupling the public search read-model from the transactional circulation domain ensures the 99th-percentile search response remains under 800ms.
- Strict EU-hosted infrastructure, AES-256 encryption, and vetted regional third-party integrations enforce absolute data residency compliance.