## Overview
This system modernizes a regional insurer's 30-year-old mainframe by incrementally migrating claim types to a hybrid Azure cloud platform. It ensures zero data loss and seamless coexistence with the legacy COBOL/DB2 system of record.

## Key Elements
- **Azure Service Bus**: Handles asynchronous messaging, event publishing, and dead-letter queues.
- **Azure Cache for Redis**: Provides high-performance caching for read-heavy reference data.
- **Azure Blob Storage**: Stores large binary files via the Claim Check pattern.
- **Modular Monolith**: Core business logic container processing claims and consuming messages.
- **Azure Application Insights**: Collects telemetry, metrics, and distributed tracing.

## Relationships
- **Modular Monolith -> Azure Service Bus**: Publishes and consumes domain events using AMQP with W3C trace context headers.
- **Modular Monolith -> Azure Cache for Redis**: Reads and writes cached reference data using the Redis Protocol via Cache-Aside pattern.
- **Modular Monolith -> Azure Blob Storage**: Offloads and retrieves large binary documents using HTTPS.
- **Azure Service Bus -> Azure Application Insights**: Emits telemetry for dead-letter queues and message processing states.

## Technology Stack
- **Azure Service Bus**: Chosen for reliable managed queuing, dead-letter support, and at-least-once delivery guarantees.
- **Azure Cache for Redis**: Selected for low-latency read caching to shield the legacy mainframe from performance bottlenecks.
- **Transactional Outbox Pattern**: Implemented in the database to eliminate dual-write failures during event publishing.
- **Claim Check Pattern**: Used with Azure Blob Storage to keep message payload sizes small and maintain throughput.

## Rationale
This architecture uses managed Azure cloud components to simplify operations for a team with limited cloud experience while guaranteeing zero message loss. It isolates the expensive-to-change mainframe through robust asynchronous messaging and caching patterns.