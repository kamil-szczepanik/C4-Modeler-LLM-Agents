## Overview
The Online Bookstore is a scaled-down Amazon-style e-commerce site designed to provide fast book browsing, secure checkout, and recommendations while ensuring compliance with GDPR, CCPA, and OWASP Top-10 security standards. It utilizes Amazon ElastiCache Redis to deliver high-performance caching for catalog data, active shopping carts, and sessions across AWS regions.

## Key Elements
- **Amazon ElastiCache Redis**: Central in-memory caching container.
- **Catalog Cache Component**: Stores serialized product details and search results in-memory.
- **Session & Cart State Component**: Manages ephemeral user cart states using in-memory hashes.
- **Replication & Persistence Manager**: Handles multi-AZ replication groups, AOF/RDB snapshots, and automated failover.
- **Cache Invalidation & Pub/Sub Worker**: Processes invalidation events to safely prune stale keys via Redis Pub/Sub.
- **Catalog & Search Container**: Spring Boot and Amazon OpenSearch service.
- **Order & Checkout Container**: Node.js and TypeScript service.

## Relationships
- **Catalog & Search Container** -> **Amazon ElastiCache Redis**: Queries catalog data and issues invalidation commands via Redis Protocol over TLS (TCP 6379).
- **Order & Checkout Container** -> **Amazon ElastiCache Redis**: Manages session and cart states via Redis Protocol over TLS (TCP 6379).
- **AWS SQS/SNS** -> **Cache Invalidation & Pub/Sub Worker**: Triggers event-driven cache invalidation hooks.

## Technology Stack
- **Amazon ElastiCache Redis**: In-memory data store chosen for sub-millisecond latency to meet performance (R-06) and scalability (R-05) requirements.
- **Redis Protocol over TLS (TCP 6379)**: Ensures secure data-in-transit encryption between containers and the cache.
- **AWS KMS**: Provides data-at-rest encryption for persistent storage, backups, and snapshots.
- **Redis AUTH & RBAC**: Enforces strict authentication and role-based access control to isolate keyspaces.
- **AWS Secrets Manager**: Automatically rotates Redis authentication tokens.
- **Redis Pub/Sub & Keyspace Notifications**: Powers event-driven cache invalidation hooks integrated with AWS SQS/SNS.

## Rationale
This architecture ensures 99.95% uptime and sub-2-second page loads by utilizing distributed in-memory caching to protect relational databases during peak traffic. It guarantees strict GDPR/CCPA compliance and OWASP mitigation through robust encryption, network isolation, and granular Redis ACLs.