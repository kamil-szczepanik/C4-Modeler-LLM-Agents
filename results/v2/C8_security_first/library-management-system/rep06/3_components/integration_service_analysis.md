## Overview
The Integration Service coordinates external third-party communication for the Library Management System. It ensures secure, resilient data exchange while strictly enforcing EU data residency constraints.

## Key Elements
- Integration Service (Container)
- API Client Component (Go SDK)
- Message Consumer/Producer Component
- Synchronization Orchestrator
- Idempotency Manager Component
- External: EU Payment Gateway, National Library Database
- External: Message Broker (Kafka/RabbitMQ), HashiCorp Vault

## Relationships
- Integration Service -> Message Broker: Publishes and consumes messages [AMQP with mTLS]
- Integration Service -> EU Payment Gateway: Processes payments and webhooks [REST over TLS 1.3 with circuit breakers]
- Integration Service -> National Library Database: Synchronizes library records [REST over TLS 1.3 with rate limiting]
- Integration Service -> HashiCorp Vault: Dynamically fetches runtime credentials [REST via short-lived tokens]

## Technology Stack
- Go: Chosen for lightweight concurrency, fast startup times, and low-level protocol control
- HashiCorp Vault: Provides dynamic secret injection and eliminates local credential storage
- OpenTelemetry: Enables end-to-end distributed tracing across internal events and external APIs
- Redis: Powers the internal Idempotency Manager to prevent duplicate transactions
- Kubernetes: Hosts the containerized service with Horizontal Pod Autoscalers driven by consumer lag

## Rationale
This architecture guarantees strict EU data residency and robust security through mTLS, TLS 1.3, and container hardening. It maintains high availability and protects downstream services via circuit breakers, asynchronous retry queues, and idempotency management.