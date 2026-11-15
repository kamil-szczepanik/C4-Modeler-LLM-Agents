## Overview
The Circulation & Loan Service manages item circulation, loans, fine collection, and transactional state for the Library Management System. It ensures frictionless checkouts and renewals for patrons while maintaining strict financial and inventory control.

## Key Elements
- Loan Orchestrator (Node.js / Express)
- Fine & Fee Manager (Node.js / Express)
- Loan Data Access Repository (Sequelize ORM)
- Event Publisher (amqplib)
- PostgreSQL Database (PostgreSQL 15)
- RabbitMQ (Message Broker)
- Payment Gateway (Adyen/Stripe EU)

## Relationships
- API Gateway -> Loan Orchestrator [HTTP/2 reverse proxy]
- Loan Orchestrator -> Fine & Fee Manager [In-memory function call]
- Loan Orchestrator -> Loan Data Access Repository [TypeScript Async/Await]
- Loan Orchestrator -> Event Publisher [AMQP protocol]
- Fine & Fee Manager -> Payment Gateway [REST / HTTPS over TLS 1.3]
- Loan Data Access Repository -> PostgreSQL Database [SQL / PostgreSQL protocol over TLS 1.3]
- Event Publisher -> RabbitMQ [AMQP over TLS 1.3]

## Technology Stack
- Node.js / Express: Chosen for asynchronous I/O performance during peak academic checkout hours.
- Sequelize ORM: Manages transactional state against PostgreSQL with strict ACID isolation.
- OpenTelemetry: Provides distributed tracing and correlation IDs for request monitoring.
- Kubernetes: Deploys containers with HPA scaling and graceful shutdown handlers.

## Rationale
This component architecture separates concerns to ensure high concurrency and transactional integrity during peak loads. Strict security, idempotency, and EU data residency compliance are enforced natively across all data paths.