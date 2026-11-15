## Overview
The Library Management System is a solution for public and academic libraries to catalogue items, manage circulation, and provide self-service portals, adhering strictly to EU-only data residency.

## Key Elements
- Library Patron, Librarian
- Identity Provider (IdP), Payment Gateway, Notification Provider
- Web Frontend (React SPA, Nginx)
- API Gateway (Spring Cloud Gateway)
- Catalogue Service, Circulation Service, Notification Service (Spring Boot, Java 21)
- PostgreSQL, Elasticsearch
- RabbitMQ Components: AMQP Protocol Adapter, Exchanges Component, Queues Component, DLX & Routing Component, Persistent Storage Volume, Alerting and Log Forwarding Component

## Relationships
- Circulation Service -> AMQP Protocol Adapter: Publishes circulation events [AMQP 0-9-1 over mTLS]
- AMQP Protocol Adapter -> Exchanges Component: Routes messages [Internal Erlang messaging]
- Exchanges Component -> Queues Component: Routes messages to persistent queues [Internal Erlang messaging]
- Queues Component -> Notification Service: Delivers notification payloads [AMQP 0-9-1 over mTLS]
- Queues Component -> DLX & Routing Component: Forwards failed/expired messages [Internal Erlang messaging]
- DLX & Routing Component -> Queues Component: Routes to dead-letter queues [Internal Erlang messaging]

## Technology Stack
- Java 21 & Spring Boot: Core microservices framework for robust business logic
- Spring Cloud Gateway: Centralized routing and API management
- Elasticsearch: High-performance indexing ensuring 99th-percentile search response under 800 ms
- PostgreSQL: Relational persistence for transactional catalog and circulation data
- RabbitMQ with Quorum Queues: Asynchronous messaging utilizing Raft consensus across three availability zones for zero data loss
- Erlang/RabbitMQ Core: Message broker engine supporting AMQP 0-9-1 and TLS clustering
- Vault & mTLS: Secure credential management and encrypted service communication

## Rationale
This architecture uses scalable microservices and reactive search tooling to meet strict performance service-level objectives. Furthermore, containerized EU-bound persistent volumes, mutual TLS, and Quorum Queues satisfy compliance and reliability constraints.