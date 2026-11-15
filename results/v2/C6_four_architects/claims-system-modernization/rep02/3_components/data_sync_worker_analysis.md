## Overview
The Data Sync Worker container synchronizes data between the legacy on-premises mainframe and the modern Azure cloud platform during a 3-year hybrid migration. Its core purpose is to guarantee claim consistency without violating strict nightly batch windows or mainframe constraints.

## Key Elements
- **CDC Reader Component**: Parses incoming delta messages from the legacy system.
- **Mainframe Protocol Handler Component**: Translates proprietary MQ byte streams into domain objects.
- **Reconciliation Engine Component**: Enforces state reconciliation and prevents data loss using idempotency keys.
- **Outbox Dispatcher Component**: Publishes synchronization events using the transactional outbox pattern.
- **Dead Letter & Exception Router Component**: Isolates malformed payloads and reconciliation conflicts for manual intervention.
- **Metrics & Audit Telemetry Component**: Emits structured tracking metrics and audit logs.

## Relationships
- Mainframe Integration Adapter -> Mainframe Protocol Handler: Delivers raw byte streams [IBM MQ client]
- CDC Reader -> Reconciliation Engine: Passes raw delta payloads [In-memory / Java queues]
- Mainframe Protocol Handler -> CDC Reader: Supplies parsed messages [In-memory]
- Reconciliation Engine -> Primary Datastore: Executes state upserts [JDBC / TDS over TLS]
- Reconciliation Engine -> Outbox Dispatcher: Triggers event propagation [Transactional Outbox Pattern]
- Reconciliation Engine -> Dead Letter & Exception Router: Forwards poisoned or conflicting records [In-memory / BlockingQueue]
- Outbox Dispatcher -> Claim Routing Service: Publishes state delta events [AMQP over Azure Service Bus]
- Dead Letter & Exception Router -> Claim Routing Service: Publishes failure alerts [AMQP over Azure Service Bus]
- Reconciliation & Dead Letter Router -> Metrics & Audit Telemetry: Emits sync counters [In-memory]
- Metrics & Audit Telemetry -> Audit and Reconciliation Service: Streams audit telemetry [HTTPS / OpenTelemetry]

## Technology Stack
- Java / Spring Boot: Core runtime for cloud container applications, aligning with team skill sets.
- Spring Batch & Spring Integration: Handles batch processing pipelines and message routing.
- Azure Service Bus & SDK: Manages asynchronous event routing and dead-letter queues via AMQP.
- Micrometer & Azure Monitor SDK: Provides structured telemetry and observability.
- IBM MQ Client: Interfaces with the on-premises legacy mainframe.

## Rationale
This architecture uses familiar Java and Spring primitives to offset the team's limited cloud experience while ensuring zero data loss (R-04). By isolating legacy protocol handling and utilizing a transactional outbox pattern, it safely processes updates within the rigid 23:00–05:00 batch window.