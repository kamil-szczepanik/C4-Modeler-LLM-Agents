## Overview
- Search Microservice for the Library Management System providing high-performance catalogue discovery for patrons and librarians.
- Designed to meet strict EU data residency constraints and sub-800ms search latency requirements.

## Key Elements
- Search Controller (Spring MVC)
- Search Query Builder & Sanitizer
- Catalogue Sync Consumer (Spring AMQP)
- Elasticsearch Client Adapter
- Elasticsearch (EU-hosted)
- Message Broker (RabbitMQ / Kafka)

## Relationships
- Search Controller -> Search Query Builder & Sanitizer: In-memory Java Method Call
- Search Query Builder & Sanitizer -> Elasticsearch Client Adapter: In-memory Java Method Call
- Elasticsearch Client Adapter -> Elasticsearch (EU-hosted): REST over TLS 1.3
- Catalogue Sync Consumer -> Message Broker: AMQP over TLS 1.3
- Catalogue Sync Consumer -> Elasticsearch Client Adapter: In-memory Java Method Call

## Technology Stack
- Java / Spring Boot: Core framework for the Search Microservice providing robust enterprise capabilities.
- Elasticsearch (EU-hosted): Search engine backend ensuring fast full-text search capabilities under 800ms.
- Spring AMQP: Event consumption library for real-time catalogue synchronization.
- OpenTelemetry: Distributed tracing framework for EU-compliant observability and latency monitoring.
- TLS 1.3 / mTLS: Transport layer security protocols enforcing EU-only data residency and zero-trust transport.

## Rationale
- Component decomposition and circuit breaker patterns isolate indexing bursts from search traffic to protect the <800ms SLA.
- Strict component-level authorization, input sanitization, and EU-pinned infrastructure satisfy security and data residency constraints.