## Overview
[The system is a Redis cache tier for the Library Management System, designed to optimize catalogue search performance and manage active session states securely.]

## Key Elements
* Redis 7.x (OSS/Enterprise)
* Session Cache Component (Circulation & Loan Service)
* Search Cache Component (Catalogue & Search Service)
* Redis Sentinel (High Availability & Failover)
* redis_exporter (Observability)

## Relationships
* Backend services to Redis via RESP3 over TLS 1.3
* Internal container networking within private backend tier
* Redis Prometheus metrics exported to monitoring infrastructure

## Technology Stack
* Redis 7.x: Core in-memory data store for performance and caching
* RESP3: Protocol for internal backend communication
* TLS 1.3 & Disk Encryption: Secures data in transit and at rest for EU data residency
* AOF and RDB Persistence: Balances fast recovery with minimal write latency
* Prometheus & redis_exporter: Tracks cache hit ratios, memory, and performance

## Rationale
[This architecture enforces strict security and data residency compliance while isolating critical sessions from volatile searches to guarantee sub-second search responses.]