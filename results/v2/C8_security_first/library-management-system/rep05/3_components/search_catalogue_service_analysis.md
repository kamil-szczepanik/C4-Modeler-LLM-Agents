## Overview
The Library Management System is a comprehensive solution for public and academic libraries to catalogue items, manage circulation, and provide self-service portals. The architecture guarantees strict EU data residency and sub-800ms search latency.

## Key Elements
- **Patron Self-Service Portal & Staff Management Console**: Client interfaces communicating via gRPC.
- **Search & Catalogue Service**: Java / Spring Boot service containing Search Controller, Search Query Engine, Catalogue Synchronization Worker, and Catalogue Repository.
- **Elasticsearch**: Search backend utilizing Java API Client and blue-green index aliasing.
- **PostgreSQL**: Primary relational database with read-replicas.
- **Message Broker**: Kafka for event-driven synchronization.

## Relationships
- Patron Self-Service Portal & Staff Management Console -> Search & Catalogue Service: gRPC over mTLS (TLS 1.3).
- Search & Catalogue Service -> PostgreSQL: Spring Data JDBC / PostgreSQL Driver with non-blocking connection pools.
- Message Broker -> Catalogue Synchronization Worker: TLS 1.3 encrypted consumer streams.
- Search Query Engine -> Elasticsearch: Java API Client with Resilience4j circuit breaker.

## Technology Stack
- **Java / Spring Boot**: Core framework for the Search & Catalogue Service providing robust enterprise capabilities.
- **Elasticsearch**: Search engine chosen for sub-800ms faceted search performance (R-05).
- **PostgreSQL**: Relational storage enforcing AES-256 encryption at rest for catalogue metadata.
- **Kafka**: Event broker enabling asynchronous, decoupled catalogue synchronization.
- **Kubernetes**: Container orchestration platform deployed strictly within EU cloud zones.
- **Resilience4j**: Circuit breaker implementation for fault-tolerant fallback handling.

## Rationale
This architecture uses an event-driven, decoupled design to decouple read paths from write operations, ensuring the system meets the 99th-percentile search response time under 800ms (R-05). Strict security controls, component isolation, and EU-bound infrastructure guarantee compliance with data residency and access policies.