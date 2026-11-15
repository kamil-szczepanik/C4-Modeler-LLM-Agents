## Overview
[The Redis Cache container provides high-performance in-memory storage for read-model projections, enabling sub-two-second screen loads for claims adjusters (R-05).]
[It shields the legacy mainframe and Azure SQL database from high-frequency query traffic during peak business hours while maintaining secure, encrypted data access.]

## Key Elements
- Azure Cache for Redis (Premium Tier, West Europe)
- Key Eviction Engine (`volatile-lru` policy)
- In-Memory Data Store (Redis Hashes and structured string keys with tenant/claim-type prefixes)
- RESP Interface (secured via Azure Private Link)
- Persistence Subsystem (point-in-time RDB snapshots for disaster recovery)

## Relationships
- Modular Monolith -> Azure Cache for Redis: Reads and writes read-model projections [RESP Protocol, TCP with TLS 1.3, ioredis client]
- Azure Key Vault -> Azure Cache for Redis: Supplies managed secrets, AUTH passwords, and TLS certificates [HTTPS]
- Azure Private Endpoint -> Azure Cache for Redis: Enforces network isolation within the virtual network [TCP]

## Technology Stack
- Azure Cache for Redis (Premium Tier): Chosen for managed replication, high availability, and multi-zone failover without deep cloud expertise.
- Redis Serialization Protocol (RESP) over TCP/TLS 1.3: Ensures low-latency, encrypted communication for real-time claim interactions.
- ioredis Node.js Client: Provides connection pooling, non-blocking asynchronous operations, and exponential backoff retry logic with jitter.
- Redis ACLs and AUTH: Restricts client command permissions (e.g., disabling `FLUSHALL` and `CONFIG`) to enforce the principle of least privilege.
- Platform-Managed Encryption-at-Rest: Protects sensitive PII and financial records held in system memory against physical snapshot extraction.

## Rationale
[This architecture satisfies strict performance constraints (R-05) by decoupling read-heavy adjuster workloads from slower persistent stores and the legacy mainframe.]
[It accommodates the team's limited cloud experience through a fully managed Azure tier while enforcing robust security, isolation, and high-availability patterns.]