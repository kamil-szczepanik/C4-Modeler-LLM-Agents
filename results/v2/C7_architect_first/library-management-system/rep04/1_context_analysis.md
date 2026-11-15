## Overview
The Library Management System (LMS) is a EU-hosted solution providing public and academic libraries with cataloging, circulation, and self-service portals. It ensures high-performance item searches and strict regional compliance.

## Key Elements
- **Patron & Library Administrator / Staff**: End-users accessing self-service portals, circulation tools, and reporting via WCAG 2.1 AA accessibility standards.
- **Library Management System (LMS)**: Core software boundary handling cataloging (R-01), circulation, and search queries.
- **Identity Provider (IdP)**: Manages authentication via OAuth 2.0 / OpenID Connect and issues signed JWTs.
- **Payment Gateway**: Processes fines and fees with PCI-DSS compliance.
- **Notification Service**: Handles automated transactional alerts (SendGrid/Twilio EU region).

## Relationships
- **Patron / Staff / Administrator -> LMS**: HTTPS / REST using TLS 1.3, mTLS, and API rate-limiting.
- **LMS -> Identity Provider**: OpenID Connect / OAuth 2.0 for authentication and RBAC enforcement.
- **LMS -> Payment Gateway**: HTTPS / REST with regional EU acquirers for secure transaction processing.
- **LMS -> Notification Service**: Asynchronous webhooks with HMAC signature verification.

## Technology Stack
- **EU-Central Cloud Region (Frankfurt/Dublin)**: Enforces mandatory EU-only data residency and end-to-end encryption at rest.
- **OAuth 2.0 / OIDC & JWT**: Manages secure, role-based access control and multi-factor authentication.
- **Distributed Tracing & Centralized Logging**: Monitors system performance to meet the <800 ms search SLA (R-05).
- **Horizontal Autoscaling & Read-Replicas**: Scales infrastructure to handle peak academic enrollment periods without degradation.

## Rationale
This architecture uses an EU-centralized deployment boundary and regional cloud services to guarantee strict compliance with EU data residency and GDPR regulations. The integration of horizontal autoscaling, API rate-limiting, and distributed tracing directly supports the 99th-percentile search latency target under 800 ms (R-05).