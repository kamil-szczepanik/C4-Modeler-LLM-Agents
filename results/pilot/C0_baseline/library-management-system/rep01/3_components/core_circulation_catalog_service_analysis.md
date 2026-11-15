## Overview
The Library Management System is a comprehensive solution for public and academic libraries to catalogue physical and digital items, manage circulation, and provide self-service portals. It enforces strict EU-only data residency and maintains a 99th-percentile search response time under 800 ms.

## Key Elements
- Core Circulation & Catalog Service (Java/Spring Boot)
- CatalogManager (Metadata handling)
- CirculationEngine (Loan workflows and fine calculations)
- FinePolicyEngine (Modular loan policies and fine rules)
- InventoryRepository (Data persistence layer)
- ExternalSyncAdapter (Digital provider integration via Spring Cloud Circuit Breaker)
- PostgreSQL Database Cluster (Stateful transactional storage)
- Redis Cache Tier (Caching hot items and active loans)
- Mobile API Gateway & Search Aggregator (External callers)
- Authentication & Session Service (OAuth2 / mTLS validation)

## Relationships
- Mobile API Gateway -> Core Circulation & Catalog Service [gRPC over TLS]
- Search Aggregator -> Core Circulation & Catalog Service [gRPC over TLS]
- Core Circulation & Catalog Service -> Authentication & Session Service [gRPC over TLS, mTLS]
- Integration Service -> Core Circulation & Catalog Service [gRPC over TLS, mTLS]
- Asynchronous Notification Worker -> Core Circulation & Catalog Service [gRPC over TLS, mTLS]
- Core Circulation & Catalog Service -> PostgreSQL Database Cluster [PostgreSQL Protocol, AES-256 at rest]
- Core Circulation & Catalog Service -> Redis Cache Tier [Redis Protocol, AES-256 at rest]

## Technology Stack
- Java / Spring Boot: Core runtime for high-concurrency circulation business logic
- Spring Data JPA: Object-relational mapping for PostgreSQL persistence
- PostgreSQL & Redis: Primary transactional store and high-performance caching tier
- gRPC over TLS & mTLS: Secure inter-service communication protocols
- OpenTelemetry: Distributed tracing for latency monitoring and observability
- Spring Cloud Circuit Breaker: Resilience pattern for external vendor timeouts (OverDrive, JSTOR)

## Rationale
This architecture uses modular Spring Boot components and gRPC to guarantee sub-second transaction processing under heavy academic loads. Strict mTLS, AES-256 encryption, and region-pinned infrastructure ensure complete compliance with EU-only data residency and privacy mandates.