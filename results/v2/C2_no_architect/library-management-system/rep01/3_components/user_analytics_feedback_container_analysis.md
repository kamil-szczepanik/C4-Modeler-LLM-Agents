## Overview
The Library Management System is a public and academic platform for cataloging items, managing circulation, and providing self-service portals. It uses a secured user analytics and feedback container to ingest anonymized patron data.

## Key Elements
- **Containers**: User Analytics & Feedback Container, API Gateway, Self-Service Portal, Audit & Compliance Container, Reporting & Analytics System, Centralized Logging & SIEM Service.
- **Components**: Fluentbit sidecars, Kafka ingestion consumers, Dead Letter Queue (DLQ).
- **People**: Library Patrons, Librarians / Circulation Staff, Library Administrators.

## Relationships
- **API Gateway -> User Analytics & Feedback Container**: Routes analytics requests via mTLS using SPIFFE/SPIRE.
- **Fluentbit sidecars -> Kafka**: Ingests telemetry via asynchronous message queues with schema validation.
- **User Analytics & Feedback Container -> Reporting & Analytics System**: Exports aggregated feedback and telemetry.

## Technology Stack
- **Kafka / Fluentbit sidecars**: Asynchronous telemetry ingestion and edge log collection.
- **EU-localized HSM**: AES-256 encryption key management for data at rest.
- **OAuth2 / JWT**: Strict RBAC authorization for telemetry streams and aggregated topics.
- **SPIFFE / SPIRE**: mTLS enforcement for internal communication.

## Rationale
This architecture ensures strict compliance with EU-only data residency and GDPR mandates through edge PII anonymization and encrypted regional storage. It decouples high-volume ingestion from analytics to maintain system scalability and performance.