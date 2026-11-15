## Overview
The Library Management System provides cataloging, circulation, and self-service portals for public and academic libraries within the EU. The architecture utilizes an event-driven messaging backbone to meet strict performance and data residency constraints.

## Key Elements
*   **Exchange Router**: Direct & Topic Exchanges routing messages via [AMQP 0-9-1].
*   **Message Queues**: Durable and Quorum Queues holding persistent messages on EU volumes.
*   **Authentication & Authorization Engine**: Erlang SSL and TLS client certificate validation module.
*   **Dead Letter Exchange & Retry Router**: Handles failed or unacknowledged messages.
*   **Cluster Coordination Manager**: Erlang Distributed Node Manager handling Quorum Queue replication.
*   **Management Plugin**: Exposes metrics and health checks via [HTTP/REST].

## Relationships
*   **Core Domain Service -> Exchange Router**: Publishes domain events via [AMQP, JSON, TLS].
*   **Integration Service -> Exchange Router**: Publishes legacy sync events via [AMQP, JSON].
*   **Exchange Router -> Message Queues**: Routes messages via [AMQP].
*   **Message Queues -> Notification Service**: Dispatches async alerts via [AMQP].
*   **Message Queues -> Integration Service**: Syncs legacy ILS data via [AMQP].
*   **Message Queues -> Dead Letter Exchange**: Forwards poisoned or expired messages via [AMQP].
*   **Node Manager <-> Peer RabbitMQ Nodes**: Replicates quorum states via [Erlang Distributed, TCP 25672].
*   **Prometheus / Monitoring -> Management Plugin**: Scrapes broker metrics via [HTTP].

## Technology Stack
*   **RabbitMQ 3.x (Erlang/OTP 26)**: Core message broker chosen for reliable asynchronous event handling.
*   **RabbitMQ Quorum Queues**: Raft-based replication ensuring high availability within EU availability zones.
*   **Erlang SSL / TLS**: Secures inter-service communication over TCP port 5671.
*   **RabbitMQ Management Plugin**: Provides operational observability and metric scraping.

## Rationale
This component architecture guarantees EU-only data residency through localized disk persistence and Erlang clustering. It ensures high resilience and low latency required for sub-800ms search and circulation workflows.