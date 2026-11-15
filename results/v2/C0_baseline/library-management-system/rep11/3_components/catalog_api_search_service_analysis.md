## Overview
The Catalog API & Search Service handles cataloging physical and digital items while delivering sub-800ms search responses. It provides high-performance, secure search capabilities exclusively within EU data boundaries.

## Key Elements
- Search Controller (.NET Core)
- Search Engine Client
- Catalogue Repository (.NET Core)
- Ranking & Personalization Service (.NET Core)
- OpenSearch Engine (EU Cloud Region)
- Redis Cache Layer
- Asynchronous Processing Worker (.NET Core Worker Service)

## Relationships
- Integration Gateway -> Search Controller: Routes API requests [gRPC over mTLS]
- Search Controller -> Redis Cache Layer: Checks cached auto-complete/queries [RESP over TLS]
- Search Controller -> Search Engine Client: Executes search queries [Internal RPC]
- Search Engine Client -> OpenSearch Engine: Queries catalog indexes [HTTPS / TLS 1.3]
- Catalogue Repository -> PostgreSQL: Mutates operational data [Encrypted SQL]
- Asynchronous Processing Worker -> OpenSearch Engine: Synchronizes data [Outbox Event Pattern]

## Technology Stack
- .NET Core: Core framework for high-throughput microservices.
- OpenSearch: Dedicated search engine for faceted search and typo-tolerance.
- Redis: In-memory cache for auto-complete and popular queries.
- PostgreSQL with GIN indexes: Transactional store for item mutations.
- OpenTelemetry: Secure telemetry generation without PII.

## Rationale
Decoupling search from transactional storage ensures sub-800ms search responses under heavy load. Enforcing AES-256 and mTLS within EU availability zones guarantees data residency compliance.