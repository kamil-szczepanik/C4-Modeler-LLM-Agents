## Overview
The Clinic Management System manages patient admissions, EMRs, scheduling, and billing for healthcare facilities using a hybrid cloud architecture. The caching layer optimizes performance while adhering to strict HIPAA and GDPR compliance regulations.

## Key Elements
- Caching Layer: Redis with primary-replica replication, automated failover via Redis Sentinel/Cluster, and ACL-restricted key-spaces.
- Consuming Microservices: EMR Service, Scheduling Service, Billing Service, and Patient Registration Service.
- Message Broker: Persistent message queues with dead-letter routing for event-driven cache invalidation.
- Infrastructure: Hybrid deployment spanning on-premise Kubernetes and `eu-central-1` (AWS).

## Relationships
- EMR Service -> Caching Layer: Queries caching layer for performance optimization [In-memory Redis Protocol over TLS 1.3]
- Scheduling Service -> Caching Layer: Queries caching layer for validation checks [In-memory Redis Protocol over TLS 1.3]
- Caching Layer -> Message Broker: Receives asynchronous event-driven invalidation signals [AMQP/Kafka Protocol]

## Technology Stack
- Redis: In-memory store with LRU eviction and memory-wiping mechanisms for low latency and security.
- TLS 1.3: Secures all data in transit across the hybrid network boundary.
- Prometheus: Monitors cache hit ratios, memory fragmentation, and latency metrics.
- Circuit Breakers: Implemented in client libraries for fallback to primary data stores during network partitions.

## Rationale
This architecture ensures sub-second EMR screen loads and 99.99% high availability while strictly protecting sensitive patient data through tokenized caching and encryption. Resilient fallback mechanisms and quorum-based consensus maintain operational stability across hybrid cloud boundaries.