## Overview
The Library Management System provides cataloging, circulation, and self-service portals for public and academic libraries within EU data residency constraints. It utilizes an asynchronous event-driven architecture to maintain high availability and performance.

## Key Elements
- RabbitMQ (Message Broker)
- Exchange Router (Erlang/Direct & Topic Exchanges)
- Queue Manager (Erlang/Mnesia)
- DLQ & Policy Engine (Erlang)
- Metrics Exporter (Erlang/Prometheus Plugin)
- Catalog & Search Service
- Circulation & Loan Service
- Notification Dispatcher

## Relationships
- Catalog & Search Service -> Exchange Router: Publishes catalogue events [AMQP 0-9-1 over TLS 1.3 with mTLS]
- Circulation & Loan Service -> Exchange Router: Publishes loan and payment events [AMQP 0-9-1 over TLS 1.3 with mTLS]
- Exchange Router -> Queue Manager: Dispatches messages to target queues [Internal Erlang messaging]
- Queue Manager -> Notification Dispatcher: Consumes queued events [AMQP 0-9-1 over TLS 1.3]
- Queue Manager -> DLQ & Policy Engine: Routes poisoned messages [Internal Erlang messaging]
- Queue Manager -> Metrics Exporter: Feeds runtime and depth metrics [Internal Erlang messaging]

## Technology Stack
- RabbitMQ: Chosen for reliable asynchronous messaging and service decoupling.
- Erlang/Mnesia: Powers core broker components, queue management, and durable message storage.
- AMQP 0-9-1 over TLS 1.3: Secures inter-service messaging with mutual TLS (mTLS).
- Prometheus Plugin: Enables low-overhead runtime and lag metrics extraction.

## Rationale
This architecture decouples core services to ensure high availability and responsiveness for patrons and staff. Using encrypted quorum queues, dead-letter queues, and strict EU data residency controls guarantees system resilience, security, and zero message loss.