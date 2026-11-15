## Overview
The Circulation & Search Service is a container within the Library Management System handling catalogue searches and circulation workflows. It is architected for high performance, fault tolerance, and strict EU data residency compliance.

## Key Elements
- **Search API Handler**: FastAPI component managing queries, fuzzy matching, and input sanitization.
- **Circulation Engine**: FastAPI component handling checkout, hold, and return workflows with RBAC.
- **Circulation State Manager**: FastAPI component managing loan transactions and state.
- **Catalog Indexer Worker**: Python async consumer keeping indices synchronized.
- **Search Analytics Adapter**: FastAPI component collecting anonymized query metrics.
- **Elasticsearch**: Datastore enforcing AES-256 encryption at rest and localized EU volumes.
- **RabbitMQ**: Message broker managing asynchronous event updates.

## Relationships
- **Search API Handler -> Elasticsearch**: Queries and indexes catalogue data via REST/Transport over mTLS (TLS).
- **RabbitMQ -> Catalog Indexer Worker**: Consumes catalog sync events via AMQP.
- **Circulation Engine -> Circulation State Manager**: Executes internal Python function calls.
- **Circulation State Manager -> Core Catalog Service**: Queries operational data via gRPC over Istio service mesh (mTLS).
- **Search API Handler -> Search Analytics Adapter**: Emits asynchronous query metrics internally.

## Technology Stack
- **FastAPI**: Chosen for asynchronous processing and low-latency API handling.
- **Elasticsearch**: Selected to achieve sub-800ms search responses (R-05).
- **RabbitMQ & Celery**: Utilized for asynchronous event-driven catalog synchronization.
- **Istio Service Mesh**: Implemented for mTLS communication and circuit breaking.

## Rationale
FastAPI and Elasticsearch deliver the sub-800ms search performance required for patron self-service portals. Strict component isolation, EU-bound persistent volumes, and mTLS guarantee security, low latency, and EU data residency compliance.