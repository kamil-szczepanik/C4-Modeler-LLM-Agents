## Overview
The Notification Service is a microservice built with Node.js and TypeScript that handles asynchronous multi-channel notifications for the Library Management System. It ensures secure, GDPR-compliant message delivery to library patrons and staff while enforcing strict EU data residency constraints.

## Key Elements
* Notification API Handler (Express.js, TypeScript)
* Message Dispatcher Engine (Node.js, TypeScript)
* Channel Adapter Module (Node.js, TypeScript)
* Template & Localization Manager (Node.js, TypeScript)
* Preference & Consent Manager (Node.js, TypeScript)
* RabbitMQ/Kafka Message Broker
* Redis In-Memory Cache
* EU-Hosted Email/SMS Providers

## Relationships
* Core API Gateway / Circulation Service -> Notification API Handler [gRPC, mTLS]
* Notification API Handler -> RabbitMQ/Kafka [AMQP / Kafka Protocol]
* Message Dispatcher Engine -> Preference & Consent Manager [Internal Function Call]
* Preference & Consent Manager -> Primary Database & Read Replica [PostgreSQL Protocol]
* Message Dispatcher Engine -> Channel Adapter Module [Internal Function Call]
* Channel Adapter Module -> EU-Hosted Email/SMS Providers [HTTPS, TLS 1.3]

## Technology Stack
* Node.js & TypeScript: Provides high throughput and type safety for asynchronous message processing.
* RabbitMQ/Kafka: Buffers traffic spikes during bulk notification events and decouples ingestion from dispatch.
* Express.js: Exposes gRPC/HTTP endpoints for secure ingress from core services.
* Redis: Caches GDPR consent states to maintain low dispatch latencies and protect the primary database.
* PostgreSQL: Persists user consent settings within strict EU data residency boundaries.

## Rationale
This architecture decouples message ingestion from delivery to handle peak loads during bulk operational alerts without blocking core library workflows. Strict adherence to EU data residency, mTLS, TLS 1.3, and Redis-backed consent caching ensures compliance with security mandates and GDPR requirements.