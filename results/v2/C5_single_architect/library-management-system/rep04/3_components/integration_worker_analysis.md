## Overview
The Library Management System provides cataloging, circulation management, and self-service portals for libraries. The Integration Worker container handles asynchronous tasks and external integrations within strict EU data residency constraints.

## Key Elements
- **Message Consumer**: Subscribes to events from the Message Broker.
- **Payment Integrator**: Communicates with the Payment Gateway.
- **Notification Integrator**: Handles payload mapping and delivery to the Notification Service.
- **Retry & Dead-Letter Handler**: Manages transient failures and unprocessable messages.
- **Webhook Receiver**: Ingests asynchronous callbacks from external systems.

## Relationships
- Message Consumer -> Message Broker (RabbitMQ): Subscribes to events [AMQP]
- Payment Integrator -> Payment Gateway: Processes fine payments [HTTPS/REST]
- Notification Integrator -> Notification Service: Sends alerts [HTTPS/REST]
- Webhook Receiver -> Payment Gateway: Ingests callbacks [HTTPS/REST]

## Technology Stack
- **Node.js with TypeScript**: Selected for asynchronous I/O performance.
- **BullMQ**: Manages retry logic and job queues.
- **PostgreSQL Database**: Backs BullMQ and ensures EU-only data residency without external Redis.
- **Regional Endpoint Configurations**: Hardcoded in HTTP clients to enforce compliance.

## Rationale
This component architecture ensures high availability and reliable asynchronous processing for external services. It rigorously enforces EU data residency constraints by utilizing regional endpoints and local database-backed queues.