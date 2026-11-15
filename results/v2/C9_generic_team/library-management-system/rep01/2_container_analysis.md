## Overview
The Library Management System provides cataloging, circulation management, and self-service portals for public and academic libraries. It ensures strict EU-only data residency and maintains a 99th-percentile search response under 800 ms.

## Key Elements
* Library Patrons and Staff
* Self-Service Portals and Kiosks
* API Gateway and API Composition / BFF Container
* Core Domain Services
* Dedicated Search Tier
* Primary Transactional Datastore
* Caching Layer (Redis)
* Asynchronous Event Bus (Message Broker)
* Observability & Logging Container
* Data Migration and Backup Container
* Configuration & Feature Management Container
* Background Worker / Job Scheduling Container
* EU-certified Secrets Management Vault

## Relationships
* Self-Service Portals and Kiosks communicate with the API Gateway using HTTPS/REST.
* API Gateway routes client traffic to the API Composition / BFF Container via HTTP/REST.
* BFF Container interacts with Core Domain Services using gRPC/REST.
* Core Domain Services query the Caching Layer (Redis) and Primary Transactional Datastore via TCP/SQL.
* Core Domain Services publish updates to the Asynchronous Event Bus via AMQP/Kafka.
* Dedicated Search Tier consumes events from the Asynchronous Event Bus to update indices.
* Background Worker executes scheduled tasks against Core Domain Services and Primary Transactional Datastore.

## Technology Stack
* API Gateway & BFF: HTTP/REST for client orchestration and payload shaping.
* Asynchronous Event Bus: Message broker ensuring decoupled, EU-compliant event-driven sync.
* Dedicated Search Tier: Decoupled search infrastructure satisfying R-05 (< 800 ms search SLA).
* Caching Layer: Redis for in-memory read acceleration of item availability and patron accounts.
* Observability: Centralized metrics, tracing, and log aggregation with PII masking.
* Security: EU-certified Secrets Management Vault for credential and secret injection.
* Contracts: OpenAPI and AsyncAPI for strict interface and schema validation.

## Rationale
This container architecture decouples search and read-heavy operations to guarantee the strict < 800 ms search performance SLA. All components and data flows are strictly bounded within EU infrastructure to satisfy data residency constraints.