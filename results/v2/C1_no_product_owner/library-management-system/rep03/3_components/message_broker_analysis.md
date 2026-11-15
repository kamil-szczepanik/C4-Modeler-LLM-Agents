## Overview
The Library Management System provides item cataloging, circulation management, and self-service portals for public and academic libraries. It processes catalog events and background jobs asynchronously via a secure, high-availability Message Broker.

## Key Elements
- Message Broker: RabbitMQ 3-node cluster
- Exchange Router: RabbitMQ Core Exchange Engine
- Queue Manager: Erlang ETS / Mnesia with Quorum Queues
- Connection & Security Handler: RabbitMQ SSL/TLS Plugin with mTLS
- Dead Letter Exchange & Retry Component: Quarantine queue mechanism
- Management & Telemetry Exporter: RabbitMQ Prometheus Plugin
- Producers/Consumers: Core Domain Microservice and Async Worker

## Relationships
- Core Domain Microservice -> Exchange Router: Publishes catalog events [AMQPS over TLS / mTLS]
- Async Worker -> Queue Manager: Consumes background jobs [AMQPS over TLS / mTLS]
- Queue Manager -> Secure Vault: Fetches TLS credentials [HTTPS]
- Observability Stack -> Management & Telemetry Exporter: Scrapes metrics [HTTP/S]

## Technology Stack
- RabbitMQ: Chosen for reliable asynchronous messaging and robust clustering
- Mnesia with Quorum Queues: Ensures message durability and high availability
- OpenTelemetry & Prometheus: Facilitates system observability and metric scraping
- HashiCorp Vault: Secures and rotates certificates and cluster credentials

## Rationale
This architecture uses a clustered, secure message broker to decouple services and handle high-throughput operations. It meets performance and EU-only data residency requirements through encrypted storage, strict resource quotas, and mTLS.