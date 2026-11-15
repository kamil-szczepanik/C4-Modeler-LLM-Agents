## Overview
The Library Management System provides item cataloguing, circulation management, and self-service portals for academic and public libraries. It uses an event-driven architecture to ensure decoupled and scalable asynchronous processing within strict EU data residency constraints.

## Key Elements
- Patrons and Library Staff (Users)
- External Identity Providers, Payment Gateways, External Archival/Reporting System (External Systems)
- Client-Side SPA/Mobile Container, API Gateway Container (NGINX / Kong), Core Business Logic / Circulation API Container
- Search Engine Container (Elasticsearch / OpenSearch), Data Access Layer / Persistence Container (PostgreSQL)
- Asynchronous Message Broker Container (RabbitMQ / Kafka), Background Workers Container, HashiCorp Vault, Centralized Observability Container

## Relationships
- Core Business Logic / Circulation API Container -> Asynchronous Message Broker Container: Publishes domain events [AMQP/Kafka Protocol, TLS encryption]
- Asynchronous Message Broker Container -> Background Workers Container: Consumes events via subscription [Event Subscription, adaptive pre-fetch limits]
- Background Workers Container -> Data Access Layer / Persistence Container (PostgreSQL): Deduplicates events and persists transactions [JDBC / TCP]

## Technology Stack
- RabbitMQ / Kafka: Asynchronous message broker for decoupled event-driven processing and high throughput
- Avro / JSON Schema: Schema registry contracts for domain event versioning and compatibility
- PostgreSQL: Persistence container storing unique message IDs for consumer idempotency deduplication
- HashiCorp Vault: Configuration and secrets management for secure broker access

## Rationale
An event-driven broker architecture ensures high throughput and decouples core circulation logic from background processing tasks. Strict EU-hosted infrastructure, TLS encryption, and idempotent consumer deduplication meet compliance and performance requirements.