## Overview
The Library Management System is a cloud-native software solution providing catalogue management, circulation services, and self-service portals for public and academic libraries. It guarantees EU-only data residency and sub-800ms search latency.

## Key Elements
- **People:** Library Patrons, Library Staff/Cataloguers, Library Administrators
- **Software Systems:** Library Management System (LMS), External Payment Gateway, External Identity Provider (IdP), External Notification Service
- **Containers/Components:** API Gateway, Self-Service Portals, Transactional Core, Asynchronous Event Bus, Reporting/Analytics Engine

## Relationships
- **Library Patrons & Staff** -> **Library Management System**: Uses via HTTPS (Web/Mobile Apps with TLS 1.3)
- **Library Management System** -> **Identity Provider**: Redirects for authentication via OIDC/OAuth 2.0
- **Library Management System** -> **Payment Gateway & Notification Service**: Integrates via outbound HTTPS/REST APIs with mTLS

## Technology Stack
- **Protocol/Security:** TLS 1.3 for transit, AES-256 for data at rest, OAuth 2.0 / OIDC for federated auth, mTLS for service-to-service communication
- **Infrastructure:** EU-pinned cloud regions, OpenTelemetry for distributed tracing, API Gateway with circuit breakers and fallback caching
- **Integration:** Asynchronous event bus / message broker for decoupling analytics from transactional workloads

## Rationale
This architecture enforces strict EU data residency and GDPR compliance using dedicated regional infrastructure and AES-256 encryption. Decoupling the reporting engine via an asynchronous event bus protects the 99th-percentile search response SLA of under 800 ms.