## Overview
The Library Management System is a cloud-native platform for public and academic libraries to catalogue physical and digital items, manage circulation, and provide self-service portals. It enforces strict EU data residency while maintaining high-performance search capabilities.

## Key Elements
- **Library Patrons (Members):** End-users accessing self-service portals.
- **Librarians / Circulation Staff:** Internal users managing inventory and circulation.
- **Library Administrators:** Internal users handling system reporting and oversight.
- **Library Management System:** Core software system handling cataloguing and circulation.
- **External Identity Provider:** EU-hosted IdP for authentication.
- **Payment Gateway:** EU region payment processor for fees and fines.
- **Notification Service:** EU instance for loan reminders and notices.
- **Observability Platform:** EU-hosted telemetry and monitoring system.

## Relationships
- Library Patrons, Librarians, and Administrators interact with Library Management System via HTTPS (TLS 1.3).
- Library Management System authenticates users against External Identity Provider via OpenID Connect (OIDC).
- Library Management System integrates with Payment Gateway and Notification Service via REST over mTLS (TLS 1.3).
- Library Management System forwards telemetry to Observability Platform via OpenTelemetry Protocol (OTLP) over TLS.

## Technology Stack
- **Cloud-Native Container Platform:** Provides horizontal auto-scaling to meet <800ms search NFR.
- **OpenID Connect (OIDC) & JWT:** Enables secure, stateless user authentication and role-based access.
- **EU-hosted Key Management Service (KMS):** Ensures AES-256 encryption at rest for strict GDPR compliance.
- **Anycast CDN / Load Balancer:** Geo-routes traffic strictly to EU edge nodes for performance and residency enforcement.

## Rationale
This architecture ensures strict compliance with EU-only data residency mandates through regionally isolated infrastructure and cryptographic controls. Simultaneously, it meets rigorous performance and availability targets via auto-scaling and low-latency edge routing.