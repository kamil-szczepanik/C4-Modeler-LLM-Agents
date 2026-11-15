## Overview
The system is a Library Management System designed for public and academic libraries to handle item cataloging, circulation, and self-service portals. It utilizes a resilient, event-driven architecture to meet strict performance and data residency constraints.

## Key Elements
* RabbitMQ Broker Container
* Exchange Routing Layer (AMQP 0-9-1 Topic Exchanges)
* Quorum Queue Instances (Raft-backed)
* Publisher Confirm & Flow Control Module
* Management & Telemetry Plugin
* Dead-Letter Exchanges (DLX)
* Circulation Service (Quarkus)
* Catalog & Search Service (Spring Boot)
* Notification Worker (Node.js)
* Centralized Observability Platform

## Relationships
* Circulation Service -> Exchange Routing Layer: Publishes circulation events [AMQP over TLS]
* Circulation Service -> Publisher Confirm & Flow Control Module: Publishes events with confirms enabled [AMQP over TLS]
* Catalog & Search Service -> Exchange Routing Layer: Publishes catalog events [AMQP over TLS]
* Quorum Queue Instances -> Notification Worker: Delivers notification payloads [AMQP over TLS]
* Dead-Letter Exchanges -> Quorum Queue Instances: Retains failed messages for auditing [Internal AMQP]
* Management & Telemetry Plugin -> Centralized Observability Platform: Ships telemetry and queue metrics [HTTPS/Prometheus]

## Technology Stack
* RabbitMQ: Asynchronous event broker with AMQP over TLS for decoupled, reliable messaging.
* Raft Consensus: Powers quorum queues for crash-safe metadata replication across availability zones.
* Prometheus: Scrapes metrics from the RabbitMQ telemetry plugin for monitoring queue depth and consumer lag.
* Kubernetes: Deploys broker pods with persistent volume provisioned IOPS and resource quotas enforcing `pause_minority` partition handling.

## Rationale
This architecture ensures strict EU-only data residency and meets performance requirements like sub-800ms search responses through asynchronous event processing. Raft-backed quorum queues and dead-letter exchanges prevent data loss and guarantee business continuity during peak loads.