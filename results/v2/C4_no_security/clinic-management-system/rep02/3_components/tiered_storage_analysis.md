## Overview
The Tiered Storage component manages long-term Electronic Medical Record archives for the Clinic Management System to meet 10-year data retention mandates. It offloads historical data from PostgreSQL to ensure cost-effective compliance with HIPAA and GDPR regulations.

## Key Elements
- Archive Manager: Handles ingestion, compression, and AES-256 client-side encryption.
- Lifecycle Policy Engine: Manages S3 object lifecycle rules and S3 Object Lock.
- Retrieval & Hydration Service: Executes accelerated S3 restores with a <5-minute SLA.
- S3-Compatible Storage: Provides secure, immutable cloud object storage.
- Apache Kafka: Transmits asynchronous event notifications.
- Notification Worker: Dispatches alerts to clinical staff upon hydration completion.

## Relationships
- Compliance Worker -> Archive Manager: Pushes retention archives via gRPC / HTTPS
- Retrieval & Hydration Service -> S3-Compatible Storage: Initiates accelerated restores via AWS SDK / HTTPS
- Retrieval & Hydration Service -> Apache Kafka: Publishes DataHydratedEvent
- Apache Kafka -> Notification Worker: Consumes hydration events
- Notification Worker -> UI/Clinician: Pushes in-app or email alerts

## Technology Stack
- Java / Spring Boot: Chosen for robust enterprise service development.
- S3-Compatible Storage / Glacier: Provides scalable, cost-effective cold data storage.
- Apache Kafka: Enables decoupled, event-driven asynchronous processing.
- PostgreSQL: Caches hydrated payloads temporarily.
- Prometheus / Grafana: Monitors SLA metrics and system latency.

## Rationale
This architecture balances regulatory compliance and operational cost by offloading cold data while guaranteeing a <5-minute asynchronous hydration SLA. Event-driven decoupling via Kafka ensures high availability and protects clinician workflow efficiency.