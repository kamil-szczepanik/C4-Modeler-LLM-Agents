## Overview
The Notification Dispatcher is an asynchronous container within the Library Management System responsible for routing, processing, and securely delivering patron alerts. It ensures reliable, privacy-compliant communication across multiple channels while adhering strictly to EU data residency mandates.

## Key Elements
- Notification Dispatcher (Node.js / TypeScript container)
- Message Consumer Component (Node.js / TypeScript)
- Preference Router Component (Node.js / TypeScript)
- Gateway Adapter Component (Node.js / TypeScript)
- Retry & Fallback Manager (Node.js / TypeScript)
- Event Publisher Component (Node.js / TypeScript)
- Message Broker (RabbitMQ / Kafka)
- Database Layer (PostgreSQL with EU-pinned JDBC)
- EU Notification Gateway (External System)
- Patron Self-Service Portal (React / TypeScript SPA)

## Relationships
- Message Broker -> Message Consumer Component: Delivers system events [AMQP / Kafka Protocol with mTLS / SASL]
- Preference Router Component -> Database Layer: Retrieves patron preferences and PII [PostgreSQL JDBC with TLS 1.3]
- Gateway Adapter Component -> EU Notification Gateway: Dispatches outbound alerts [HTTPS / REST with TLS 1.3, Certificate Pinning, Egress Filtering]
- Event Publisher Component -> Message Broker: Publishes delivery status and failure events [AMQP / Kafka Protocol]
- Patron Self-Service Portal -> Message Broker: Accesses notification history logs via downstream microservices

## Technology Stack
- Node.js / TypeScript: Core runtime and language for the Notification Dispatcher ensuring modular, testable components.
- RabbitMQ / Kafka: Message broker for asynchronous event consumption, dead-letter queues (DLQ), and status publishing.
- PostgreSQL: Relational database with EU-pinned storage for patron preferences and masked PII logs.
- Kubernetes: Deployment environment providing Horizontal Pod Autoscaling (HPA), resource governance, and Kubernetes Secrets for credential injection.
- OpenTelemetry: Distributed tracing framework for end-to-end payload monitoring and operational observability.

## Rationale
This architecture ensures high reliability and at-least-once processing via circuit breakers, retry managers, and dead-letter queues to prevent dropped patron notices during peak loads. It guarantees strict EU data compliance by enforcing TLS 1.3, application-layer encryption, and PII redaction across all asynchronous and synchronous communications.