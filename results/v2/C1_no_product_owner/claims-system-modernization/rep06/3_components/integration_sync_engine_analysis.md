## Overview
The Integration & Sync Engine is a hybrid event-streaming platform that synchronizes data between the modern Azure cloud platform and the legacy on-premise mainframe. Its core purpose is to guarantee lossless claim migration, maintain consistency, and support bidirectional parity during the gradual deprecation of the 30-year-old legacy system.

## Key Elements
- **Outbox Event Dispatcher**: Lightweight Spring Boot poller streaming database outbox events.
- **Mainframe Adapter Service**: Apache Camel / Azure Functions container translating events for the mainframe.
- **Reconciliation & Rollback Worker**: Spring Batch worker ensuring dual-write parity and one-day fallback capability (R-06).
- **Azure Event Hubs**: Managed event streaming broker with AMQP 1.0 and native capture capabilities.
- **Azure Key Vault**: Secrets and certificate management storage integrated with managed identities.
- **Azure ExpressRoute**: Dedicated hybrid network connection securing on-premise to cloud transit.
- **Azure Monitor**: Observability platform tracking consumer lag, DLQs, and immutable audit logs.

## Relationships
- Claims Core API -> Outbox Event Dispatcher: Writes transactional sync state [JDBC]
- Outbox Event Dispatcher -> Azure Event Hubs: Publishes CDC events [AMQP 1.0 / HTTPS]
- Mainframe Adapter Service -> Azure Key Vault: Retrieves SFTP/mTLS credentials [Managed Identity / REST]
- Mainframe Adapter Service -> Legacy Mainframe: Pushes delta files and batch payloads [SFTP over Azure ExpressRoute with mTLS]
- Integration & Sync Engine -> Azure Monitor: Streams operational metrics and audit logs [HTTPS / Azure Diagnostics]

## Technology Stack
- **Azure Event Hubs**: Managed streaming to reduce operational overhead for a low-experience cloud team.
- **Spring Boot / Spring Batch**: Frameworks for reliable polling outbox patterns and reconciliation jobs.
- **Apache Camel / Azure Functions**: Integration routing and serverless compute for mainframe payload translation.
- **Resilience4j**: Circuit breaking and backpressure to protect the legacy mainframe from overload.
- **Azure Key Vault & Managed Identities**: Zero-trust credential retrieval and automated secret rotation.

## Rationale
This architecture uses fully managed Azure services to minimize day-2 operational toil for a team with limited cloud experience while securely bridging the hybrid gap. It enforces strict consistency, backpressure, and transactional outbox patterns to prevent data loss without breaching the rigid nightly batch window constraints.