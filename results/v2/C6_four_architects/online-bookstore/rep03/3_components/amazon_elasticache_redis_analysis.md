## Overview
The system is an online bookstore providing physical and electronic book sales with search, recommendations, and reviews. It utilizes a microservices architecture hosted on AWS to deliver high performance, scalability, and security.

## Key Elements
- Currency Rate Cache Component (Amazon ElastiCache, Redis)
- Catalog Query Cache Component (Amazon ElastiCache, Redis)
- Session Store Component (Amazon ElastiCache, Redis)
- Distributed Rate Limiter Component (Amazon ElastiCache, Redis)
- Idempotency & Deduplication Store Component (Amazon ElastiCache, Redis)
- Consuming Services: Payment & Currency Service (.NET Core), Catalog & Search Service (Spring Boot), Order & Checkout Service (Node.js), Amazon API Gateway

## Relationships
- Payment & Currency Service -> Currency Rate Cache Component [Redis Protocol over TCP]
- Catalog & Search Service -> Catalog Query Cache Component [Redis Protocol over TCP]
- Order & Checkout Service -> Session Store Component [Redis Protocol over TCP]
- Amazon API Gateway -> Distributed Rate Limiter Component [Redis Protocol over TCP]
- Order & Checkout Service -> Idempotency & Deduplication Store Component [Redis Protocol over TCP]

## Technology Stack
- Amazon ElastiCache (Redis): Managed in-memory data store for low-latency caching and state management.
- Redis Cluster Mode / Multi-AZ Replication: Deployed for high availability (99.95% uptime) and seamless failover.
- Redis Atomic Operations (`SETNX`, sorted sets, Lua scripts): Utilized for rate limiting and deduplication.

## Rationale
This architecture ensures sub-2-second page loads and handles 1 million MAU without degradation through efficient in-memory caching. It guarantees transaction safety and security via atomic idempotency locks and distributed rate limiting.