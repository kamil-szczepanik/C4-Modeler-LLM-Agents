## Overview
The Library Management System is a comprehensive solution for public and academic libraries to catalogue items, manage circulation, and provide self-service portals. It enforces strict EU-only data residency while maintaining high performance.

## Key Elements
- **PostgreSQL**: Relational database serving as the primary persistent storage.
- **PgBouncer**: Connection pooling layer managing database traffic.
- **Primary PostgreSQL Instance**: Handles write workloads and transactional operations.
- **Read Replica Instance**: Handles read-heavy analytical traffic.
- **Catalog & Circulation Schema**: Stores items, loans, and patron data.
- **Audit & Reporting Schema**: Stores historical data isolated from operational paths.
- **Full-Text Search Indexer & Triggers**: Maintains real-time search synchronization via native indexes.
- **EU Data Residency Enforcer**: Enforces geographic restrictions via configuration and Row-Level Security.

## Relationships
- **Core Domain Service** -> **PgBouncer**: Submits transactional queries via [JDBC] over [TCP/IP].
- **PgBouncer** -> **Primary PostgreSQL Instance**: Routes and pools database connections via [TCP/IP].
- **Reporting & Analytics Service** -> **Read Replica Instance**: Executes read-only queries via [SQL/Alchemy].
- **Primary PostgreSQL Instance** -> **Read Replica Instance**: Executes asynchronous streaming replication via [TCP/IP].
- **Catalog & Circulation Schema** -> **Full-Text Search Indexer & Triggers**: Propagates internal events via [PostgreSQL Triggers/WAL].

## Technology Stack
- **PostgreSQL**: Chosen for robust ACID compliance, reliability, and native `tsvector`/`GIN` indexing.
- **PgBouncer**: Utilized for [TCP/IP] connection pooling to prevent exhaustion under peak loads.
- **SQL/Alchemy**: Used by reporting services for database interactions.
- **JDBC**: Utilized for core domain transactional persistence.

## Rationale
This architecture uses schema separation, read replicas, and connection pooling to eliminate resource contention and protect the <800 ms search SLA. Furthermore, engine-level residency controls ensure strict compliance with EU-only data constraints.