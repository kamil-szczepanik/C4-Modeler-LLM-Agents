## Overview
The Library Management System is a solution for public and academic libraries to catalogue items, manage circulation, and provide self-service portals. It utilizes a robust, EU-compliant message broker to coordinate asynchronous workflows across microservices and workers.

## Key Elements
- **Message Broker:** RabbitMQ container handling asynchronous event streaming.
- **Exchange Router:** Topic Exchange (AMQP) for decoupling publishers from queues using routing keys.
- **Queue Manager:** AMQP queues maintaining bounded buffers for worker containers.
- **Persistence Log:** Mnesia/Disk storage ensuring localized message durability.
- **Dead Letter Exchange (DLX):** AMQP isolation mechanism for poisoned or unroutable messages.
- **Cluster Federation / Sharding Plugin:** Erlang-based clustering across availability zones.
- **Management & Monitoring Plugin:** HTTP/REST endpoint on port 15672 for Prometheus metrics.
- **Access Control & Virtual Host Manager:** AMQP SASL/TLS and x509 authentication module.

## Relationships
- **Core Services Container -> Exchange Router:** Publishes domain events via AMQP 0-9-1 over TLS.
- **Queue Manager -> Worker Containers (Async, Integration, Search):** Delivers buffered messages using push-based consumption with manual `basic.ack`.
- **Management & Monitoring Plugin -> Prometheus:** Exposes broker metrics via HTTP/REST for scraping.

## Technology Stack
- **RabbitMQ & AMQP 0-9-1:** Core messaging engine providing flexible routing and reliable queue management.
- **Erlang / Mnesia:** Underlying runtime and disk persistence engine ensuring strict EU-only data residency.
- **TLS 1.3 & x509:** Security protocols enforcing in-transit encryption and access control.

## Rationale
This architecture ensures strict EU data residency via localized Mnesia disk persistence and regional clustering. Furthermore, it meets high-performance and reliability NFRs through robust queue management, DLX error isolation, and Prometheus observability.