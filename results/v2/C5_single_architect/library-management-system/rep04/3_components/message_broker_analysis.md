## Overview
The Library Management System provides cataloging, circulation management, and self-service portals for libraries. It uses a component-level Message Broker architecture to handle asynchronous workflows and integrations.

## Key Elements
- **Exchange Router**: Directs incoming messages using RabbitMQ Direct/Topic Exchanges.
- **Queue Manager**: Manages durable message queues via RabbitMQ Quorum Queues.
- **Connection & Security Manager**: Handles authentication and TLS termination using TLS 1.3 and x.509/PLAIN auth.
- **Dead Letter Handler**: Captures failed messages using RabbitMQ Dead Letter Exchanges (DLX).

## Relationships
- **Core Domain -> Exchange Router**: Publishes domain events [AMQP 0-9-1 over TLS].
- **Exchange Router -> Queue Manager**: Routes events to queues [AMQP internal].
- **Queue Manager -> Integration Worker**: Delivers messages for processing [AMQP 0-9-1 over TLS].
- **Queue Manager -> Dead Letter Handler**: Forwards failed messages [AMQP internal].
- **Dead Letter Handler -> PostgreSQL Database**: Persists failed messages for audit/replay [JDBC over TLS].

## Technology Stack
- **RabbitMQ**: Message broker software for asynchronous decoupling and event routing.
- **RabbitMQ Quorum Queues**: Consensus replication to meet EU-only data residency and high availability constraints.
- **TLS 1.3**: Secure transport protocol ensuring encrypted communication.
- **PostgreSQL Database**: Relational database for persistent storage of failed messages.

## Rationale
This architecture ensures high availability and robust asynchronous workflow failure handling while strictly adhering to EU-only data residency requirements. Consensus replication guarantees data safety across distributed nodes.