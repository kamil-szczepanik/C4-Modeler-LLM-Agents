## Overview
[Library Management System] is a public and academic library solution designed for cataloging items, managing circulation, and providing self-service portals with strict EU data residency.

## Key Elements
- Notification Service (Node.js/Go container)
- Event Consumer Component (Go)
- Preference & Template Engine (Node.js/Go)
- Dispatch Adapter Component (Go)
- Audit & Logging Component (Go)
- Message Broker (Kafka/RabbitMQ)
- PostgreSQL Database
- HashiCorp Vault
- External EU-hosted Email/SMS Providers

## Relationships
- Event Consumer -> Message Broker: Consumes domain events [AMQP/mTLS]
- Preference & Template Engine -> PostgreSQL Database: Queries preferences and opt-out flags [SQL/TLS]
- Dispatch Adapter -> HashiCorp Vault: Fetches provider secrets [HTTPS/Token Auth with AppRole]
- Dispatch Adapter -> External Email/SMS Providers: Sends notifications [HTTPS/TLS 1.3]
- Dispatch Adapter -> Audit & Logging Component: Records delivery timestamps [In-memory/gRPC]

## Technology Stack
- Go & Node.js: Selected for asynchronous workload handling and micro-component performance.
- HashiCorp Vault: Used with AppRole authentication for dynamic credential management.
- PostgreSQL Database: Stores anonymized delivery logs and patron channel preferences.
- Message Broker (Kafka/RabbitMQ): Provides asynchronous queuing, dead-letter queues (DLQs), and backpressure control.
- OpenTelemetry & Prometheus: Enables distributed tracing, queue lag monitoring, and metric alerting.

## Rationale
This architecture ensures secure, asynchronous multi-channel notification delivery while strictly adhering to GDPR and EU-only data residency requirements. Decoupling components and isolating PII support reliable patron engagement, zero-downtime scalability, and effective librarian dispute resolution.