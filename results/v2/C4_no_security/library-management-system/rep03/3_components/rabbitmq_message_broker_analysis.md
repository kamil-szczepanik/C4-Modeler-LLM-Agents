## Overview
The Library Management System provides cataloging, circulation, and self-service portals for public and academic libraries within EU data residency constraints. It ensures reliable asynchronous event processing and message durability for critical notifications.

## Key Elements
- **RabbitMQ Message Broker**: High-availability 3-node quorum queue cluster.
- **Exchanges & Queues**: Notification Exchange, DLX Exchange, Notification Queue, and Dead Letter Queue.
- **Admin Notification API**: Lightweight service (Go/Node.js) for secure DLX inspection and message replay.
- **Workers**: Notification & Payment Workers (Python/Celery).
- **Users**: Librarians and Library Administrators.

## Relationships
- Circulation & Core Container -> Notification Exchange: Publishes async events [AMQP]
- Notification Exchange -> Notification Queue: Routes messages [AMQP]
- Notification Queue -> Notification & Payment Workers: Consumes alerts [AMQP]
- Admin Notification API -> Dead Letter Queue: Inspects and republishes messages [AMQP/HTTPS]
- Librarians / Library Administrators -> Admin Notification API: Accesses replay dashboard [HTTPS]

## Technology Stack
- **RabbitMQ**: Asynchronous message broker with persistent quorum queues and TLS encryption.
- **Prometheus**: Metrics collection for queue depth and memory alarms.
- **Object Storage**: EU-localized storage for encrypted persistent volume backups.
- **Go / Node.js**: Implementation language for the Admin Notification API.

## Rationale
This architecture ensures robust asynchronous decoupling and message durability to prevent missed patron notifications. It maintains strict EU data residency while providing secure administrative tools for managing dead-lettered messages.