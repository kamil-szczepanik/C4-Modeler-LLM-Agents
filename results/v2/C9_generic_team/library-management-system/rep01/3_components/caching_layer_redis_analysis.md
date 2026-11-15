## Overview
The Library Management System is a solution for public and academic libraries to catalogue items, manage circulation, and provide self-service portals. It uses a high-performance Caching Layer (Redis) to accelerate read operations and ensure fast search response times.

## Key Elements
- Caching Layer (Redis): In-memory data store for read acceleration.
- Core Domain Services: Microservices utilizing a Cache-Aside pattern.
- Primary Transactional Datastore: Relational database for ACID transactions.
- EU-certified Secrets Management Vault: Secure injection container for credentials.

## Relationships
- Core Domain Services -> Caching Layer (Redis): Queries caching layer using RESP over TCP with TLS.
- Core Domain Services -> Primary Transactional Datastore: Executes database writes and fallback queries using SQL over TCP.
- Caching Layer (Redis) -> EU-certified Secrets Management Vault: Retrieves runtime TLS certificates and credentials.

## Technology Stack
- Redis: Chosen for low-latency in-memory read acceleration.
- RESP (REdis Serialization Protocol): Protocol used for communication over TCP.
- Prometheus: Utilized for monitoring hit/miss ratios, memory fragmentation, and connected clients.
- EU-certified Secrets Management Vault: Enforces EU data residency for credentials and TLS certificates.

## Rationale
This architecture meets the < 800 ms search performance requirement through Redis read acceleration while strictly enforcing EU data residency constraints. Reliability is maintained via connection pooling, strict timeouts, and database fallback mechanisms.