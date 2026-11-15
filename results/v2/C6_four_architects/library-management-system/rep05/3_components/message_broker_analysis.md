## Overview
- Library Management System provides cataloging, circulation management, and self-service portals for public and academic libraries.
- The architecture utilizes a managed message broker to handle asynchronous event processing and webhook ingestion within EU data residency constraints.

## Key Elements
- Exchange Router Component
- Queue Manager Component
- Connection & Security Manager Component
- Dead Letter & Retry Component
- Broker Metrics & Audit Component
- Topology Management Component
- Core Services Container
- Integration Service
- Async Worker Container
- SIEM / Central Log Collector

## Relationships
- Core Services & Integration Service -> Exchange Router: Publishes events [AMQP/TLS]
- Integration Service -> Exchange Router: Publishes incoming third-party webhook events [AMQP/TLS]
- Queue Manager -> Async Worker Container: Dispatches background jobs [AMQP/TLS]
- Queue Manager -> Dead Letter & Retry Component: Forwards failed messages [Internal AMQP]
- Dead Letter & Retry Component -> Async Worker Container: Re-dispatches retried tasks [AMQP/TLS]
- Exchange Router & Queue Manager -> Broker Metrics & Audit Component: Emits telemetry [Prometheus/TLS]
- Broker Metrics & Audit Component -> SIEM / Central Log Collector: Forwards security logs [Syslog/TLS]
- CI/CD Deployment Pipeline -> Topology Management Component: Applies schema definitions [HTTPS]
- Topology Management Component -> Exchange Router & Queue Manager: Applies bindings and TTL policies [AMQP Management API / HTTPS]

## Technology Stack
- Managed RabbitMQ: Provides reliable message brokering with native exchange and queue support
- AMQP 0-9-1 / AMQP/TLS: Secures internal messaging and communication protocols
- Prometheus / RabbitMQ Prometheus Plugin: Enables real-time queue observability and telemetry
- Terraform / RabbitMQ definitions JSON: Ensures declarative, immutable infrastructure management
- HTTPS / TLS: Secures management APIs, webhook ingestion, and log export

## Rationale
- Decouples synchronous HTTP ingestion from asynchronous processing to maintain high performance and search response SLAs under 800 ms.
- Enforces strict EU data residency and auditability through isolated queue management and secure TLS communication.