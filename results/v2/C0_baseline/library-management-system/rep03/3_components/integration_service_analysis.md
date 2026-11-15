## Overview
The Integration Service is a stateless Node.js component within the Library Management System responsible for managing secure external integrations with payment gateways and digital content providers. It ensures resilient transaction processing, digital license synchronization, and strict compliance with EU data residency.

## Key Elements
- Event Consumer Component (Node.js / TypeScript / Kafka.js)
- Payment Adapter Component (Node.js / TypeScript / Axios / Opossum)
- Content Provider Adapter Component (Node.js / TypeScript / Axios)
- Retry & DLQ Manager Component
- Notification Dispatcher Component (Node.js / TypeScript / Axios)
- Observability Exporter Component (prom-client)
- External Systems: Payment Gateway, Digital Content Providers, Message Broker, Secrets Manager, Centralized Observability & SIEM Platform, Notification & Audit Service

## Relationships
- Event Consumer -> Message Broker: Consumes domain events [Kafka Protocol]
- Payment Adapter -> Payment Gateway: Processes transactions and handles callbacks [TLS 1.3 / HMAC-SHA256]
- Content Provider Adapter -> Digital Content Providers: Retrieves metadata and licenses [TLS 1.3]
- Payment Adapter -> Secrets Manager: Fetches API keys and manages tokens [HashiCorp Vault API / mTLS]
- Retry & DLQ Manager -> Message Broker: Publishes failed messages to DLQ [Kafka Protocol]
- Retry & DLQ Manager -> Notification Dispatcher: Triggers alerts on persistent failure [Internal Async Call]
- Observability Exporter -> Centralized Observability & SIEM Platform: Ships anonymized metrics and logs [HTTPS / TLS 1.3]

## Technology Stack
- Node.js / TypeScript: Core runtime for asynchronous, non-blocking integration processing.
- Axios & Opossum: HTTP client and circuit breaker pattern implementation for external API resilience.
- Kafka.js: Event streaming library for asynchronous domain event consumption and DLQ management.
- HashiCorp Vault: Dynamic secret management with token renewal and hot-reloading.
- prom-client: Exposes Prometheus-compatible metrics for telemetry and monitoring.

## Rationale
This architecture ensures high availability and zero-latency patron transactions through circuit breakers and asynchronous retry mechanisms. It maintains strict EU data residency and security compliance by excluding PII/PCI-DSS data from logs and enforcing restricted network egress.