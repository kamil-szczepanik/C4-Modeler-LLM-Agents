## Overview
A Library Management System for public and academic libraries providing cataloging, circulation, and self-service portals. It ensures strict EU data residency and high-performance search capabilities.

## Key Elements
- **Users**: Library Patrons, Circulation Staff, Library Administrators
- **External Systems**: Payment Gateway, Identity Provider, Notification Service
- **Containers**: Web Frontend (React/TypeScript), API Gateway (Kong/Nginx), Core Business Service (Spring Boot), Search Service (Elasticsearch), Database (PostgreSQL), Notification Dispatcher (Python/Celery), Audit Logging Service (Go), Message Broker (RabbitMQ)
- **Message Broker Components**: Exchange (Direct/Topic), Durable Queues (`notification.queue`, `audit.queue`), Dead Letter Exchange & Queue (`notification.dlq`), Management API/UI

## Relationships
- Web Frontend -> API Gateway: HTTPS / REST / GraphQL
- API Gateway -> Core Business Service & Search Service: Internal gRPC / REST
- Core Business Service & Audit Logging Service -> Message Broker Exchange: Publish events [AMQP over TLS 1.3 with mTLS]
- Notification Dispatcher -> Message Broker Durable Queue: Consume messages [AMQP over TLS 1.3 with mTLS]
- Durable Queue -> Dead Letter Exchange: Forward poisoned messages [AMQP]

## Technology Stack
- **Frontend**: React/TypeScript on EU-region CDN for low latency.
- **Backend**: Spring Boot (Java) for core business logic.
- **Database**: PostgreSQL with AES-256 encryption-at-rest.
- **Search**: Elasticsearch ensuring 99th-percentile search response < 800 ms.
- **Messaging**: RabbitMQ containerized cluster with AMQP protocol, TLS 1.3, and mTLS.

## Rationale
The architecture uses containerized services within an EU Kubernetes environment to satisfy strict data residency constraints. RabbitMQ with durable queues and DLXs ensures reliable asynchronous communication without sacrificing user experience.