## Overview
The Online Bookstore System utilizes Amazon ElastiCache Redis as an in-memory caching and session management layer to deliver high-performance e-commerce features for 1 million monthly active users. It supports rapid catalog browsing, secure shopping carts, and real-time recommendations while ensuring strict security and GDPR/CCPA compliance.

## Key Elements
- **Session Store Engine**: Redis Hashes managing user shopping cart states with a 7-day TTL and `noeviction` policy.
- **Recommendation Cache Engine**: Redis Sorted Sets (`ZSET`) storing precomputed "Customers also bought" item affinities using `volatile-lru` eviction.
- **Order & Checkout Service**: ECS Fargate container handling transactions and acquiring locks via Amazon DynamoDB.
- **Recommendation Service**: ECS Fargate container fetching item affinities.
- **Customer Privacy/Compliance Service**: Manages data erasure and GDPR/CCPA "Right to be Forgotten" requests.

## Relationships
- **Order & Checkout Service -> Session Store Engine**: Reads and writes cart state via Redis Serialization Protocol (RESP v3) over TLS.
- **Order & Checkout Service -> Amazon DynamoDB**: Acquires transactional locks for checkout coordination via HTTPS/API.
- **Recommendation Service -> Recommendation Cache Engine**: Fetches item affinities using RESP v3 over TLS.
- **Customer Privacy/Compliance Service -> Session Store Engine**: Purges user session hashes and PII using Redis `SCAN` and `DEL` commands.

## Technology Stack
- **Amazon ElastiCache (Redis)**: In-memory datastore configured in Cluster mode with Multi-AZ replication to meet 99.95% availability targets.
- **Amazon DynamoDB**: Handles transactional checkout locks via conditional writes to prevent split-brain financial anomalies.
- **TLS 1.3 & AWS KMS**: Enforces transit encryption for RESP v3 traffic and at-rest encryption using Customer Managed Keys.
- **Redis AUTH & IAM**: Restricts access via least-privilege Redis ACLs and AWS IAM database authentication.

## Rationale
This architecture meets scalability and sub-2-second performance requirements by offloading high-velocity reads and session states to an isolated, highly available Redis cluster. Separating financial locking into DynamoDB ensures consistency for transactions while optimizing Redis for ephemeral caching.