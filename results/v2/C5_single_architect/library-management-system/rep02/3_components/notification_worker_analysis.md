## Overview
The Notification Worker is an event-driven component of the Library Management System that reliably processes asynchronous events to deliver notifications to patrons and staff. It ensures system resilience through local rate-limiting, retry logic, and strict adherence to EU data residency constraints.

## Key Elements
- Message Consumer (Node.js/amqplib)
- Notification Router (TypeScript)
- Delivery Client (Axios)
- Retry Coordinator (TypeScript/Bottleneck)
- Dead Letter Handler
- Message Broker (RabbitMQ / Apache Kafka)
- External Notification Service

## Relationships
- Message Consumer -> Message Broker: Consumes events [AMQP]
- Message Consumer -> Notification Router: Passes deserialized events [In-memory function call]
- Notification Router -> Delivery Client: Sends formatted payload [In-memory function call]
- Delivery Client -> Retry Coordinator: Forwards failed requests [In-memory function call]
- Delivery Client -> Notification Service: Sends notifications [HTTPS]
- Retry Coordinator -> Notification Service: Retries requests [HTTPS]
- Dead Letter Handler -> Message Broker: Routes poison messages to DLQ [AMQP]

## Technology Stack
- Node.js: Provides fast asynchronous I/O and low memory overhead for event-driven processing.
- TypeScript: Ensures type safety across the worker's internal routing and retry logic.
- amqplib: Enables reliable message consumption over the AMQP protocol.
- Axios: Handles outbound, timeout-managed HTTPS requests to the external provider.
- Bottleneck: Manages exponential backoff and rate limiting locally for transient failure handling.

## Rationale
This architecture ensures high reliability and fault tolerance when communicating with external third-party systems. Localizing retry state and rate-limiting within the EU boundary satisfies strict data residency mandates while meeting system resilience goals.