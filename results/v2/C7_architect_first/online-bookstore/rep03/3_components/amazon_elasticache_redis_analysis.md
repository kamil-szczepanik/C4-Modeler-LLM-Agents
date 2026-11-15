## Overview
- Defines internal component decomposition and operational safeguards for the Amazon ElastiCache (Redis) container.
- Supports 1M MAU scale, sub-2s page loads, and zero cart data loss for the online bookstore.

## Key Elements
- Redis Cluster Engine (Primary and Replica nodes across multiple Availability Zones)
- Session Store Module (`sess:*` keyspace for encrypted user sessions and shopping carts)
- Catalogue Cache Module (`cat:*` keyspace with LRU eviction for product metadata and search facets)
- Core E-Commerce API (Client interacting via Redis RESP protocol)

## Relationships
- Core E-Commerce API -> Session Store Module (Redis RESP protocol over TLS 1.3) for sub-millisecond cart lookups
- Core E-Commerce API -> Catalogue Cache Module (Redis RESP protocol over TLS 1.3) for read-heavy product metadata

## Technology Stack
- Amazon ElastiCache (Redis OSS / Memory Store): Managed caching engine ensuring high availability and sub-millisecond latency.
- Redis Append-Only File (AOF) & Daily Snapshots: Persistence strategy ensuring zero data loss during failovers.
- AWS KMS: Customer-managed keys (CMK) providing encryption at rest for PII and session data.
- TLS 1.3: In-transit encryption across all shards and connections.
- AWS Secrets Manager: Automatic rotation of Redis AUTH credentials.

## Rationale
- Logical keyspace separation prevents catalog cache thrashing from evicting critical user session data.
- Multi-AZ deployment, AOF persistence, and strict replica write settings guarantee 99.95% uptime and GDPR/CCPA compliance.