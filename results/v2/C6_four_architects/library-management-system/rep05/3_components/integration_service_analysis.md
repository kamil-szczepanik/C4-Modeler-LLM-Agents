## Overview
The Library Management System is a comprehensive solution for public and academic libraries to catalogue items, manage circulation, and provide self-service portals. The Integration Service acts as a resilient, modular container that securely manages all external third-party communications within the EU.

## Key Elements
- Integration Service Container (NestJS / TypeScript)
- Integration Facade / Router (NestJS Module with Circuit Breaker & Retry Middleware)
- Payment Adapter Component (NestJS)
- SIS Sync Component (NestJS)
- Webhook Handler Component (NestJS)
- IoT Gateway Component (NestJS)
- Notification Adapter Component (NestJS)
- Delivery & Logistics Adapter Component (NestJS)
- External Systems: Stripe EU, University SIS, Third-Party Delivery, RFID Gates, LDAP/SAML IdP

## Relationships
- Core Services Container -> Integration Facade / Router: Delegates integration tasks [gRPC]
- Integration Facade / Router -> External Adapters: Dispatches payloads [In-Memory / Resilience4ts]
- Payment Adapter Component -> Stripe EU: Processes payments [HTTPS/REST]
- SIS Sync Component -> University SIS: Syncs patron rosters [SFTP/REST]
- IoT Gateway Component -> RFID Gates: Receives item scans [MQTT]
- Delivery & Logistics Adapter Component -> Third-Party Delivery: Coordinates shipments [HTTPS/REST]

## Technology Stack
- NestJS (TypeScript): Selected for strict modularity and dependency injection
- gRPC: Used for high-performance internal communication from core services
- MQTT & HTTPS/REST: Standardized protocols for IoT and external API integrations
- Resilience4ts: Implemented for circuit breaking and retry logic to prevent cascading failures

## Rationale
This modular NestJS architecture isolates external system volatility from core business logic while ensuring strict data residency compliance. The inclusion of a facade, circuit breakers, and localized regional deployment meets all performance and EU-only data constraints.