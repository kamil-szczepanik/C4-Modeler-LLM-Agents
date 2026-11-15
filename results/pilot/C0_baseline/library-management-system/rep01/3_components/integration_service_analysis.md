## Overview
The Integration Service synchronizes data and handles integrations with external providers for the Library Management System. It ensures seamless patron access to digital collections and reliable payment processing while maintaining EU data residency compliance.

## Key Elements
* Webhook Receiver (FastAPI)
* Task Dispatcher / Task Orchestrator Component (Celery)
* Provider Adapters Module
* Sync State Manager
* Redis Cache Tier / Message Broker
* Core Circulation & Catalog Service (Java/Spring Boot)
* PostgreSQL Database Cluster
* External Payment Gateways
* OverDrive and JSTOR Digital Content Providers

## Relationships
* Webhook Receiver -> Core Circulation & Catalog Service: Invokes updates via gRPC over mTLS [gRPC over TLS, mTLS]
* Task Dispatcher -> Redis: Coordinates asynchronous jobs via message broker queues [Redis Protocol]
* Provider Adapters -> OverDrive & JSTOR: Synchronizes data via outbound egress filtering [HTTPS, TLS 1.3]
* Webhook Receiver -> External Payment Gateways: Receives callback events [Webhooks, HTTPS]
* Sync State Manager -> PostgreSQL Database Cluster: Tracks transaction state with column-level encryption [PostgreSQL Protocol, TLS]

## Technology Stack
* Python / Celery: Powers asynchronous background task execution and job scheduling
* FastAPI: Provides high-performance API endpoints for webhook ingestion with schema validation
* Redis: Acts as the message broker with persistence enabled (AOF/RDB) for Celery queues
* PostgreSQL Database Cluster: Stores transaction states and patron metadata with column-level encryption
* TLS 1.3 / mTLS: Secures all internal and external network communications and enforces data boundaries

## Rationale
This architecture isolates volatile third-party integrations from core domains using asynchronous queues and dedicated adapters, protecting system performance and revenue streams. Strict egress filtering, TLS 1.3, and encrypted storage guarantee compliance with EU-only data residency constraints.