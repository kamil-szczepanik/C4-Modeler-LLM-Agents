## Overview
[The system is a modern insurance claims platform designed to gradually replace a legacy mainframe while ensuring continuous processing. Its core purpose is to enable online claim submission and adjuster workflows while maintaining strict data consistency across a hybrid infrastructure.]

## Key Elements
* Operational Data Store (Azure Database for PostgreSQL Flexible Server)
* Claim State & Domain Store (Component)
* Read Model & Cache Store (Component)
* Migration Metadata Store (Component)
* Audit & Compliance Log Store (Component)
* PgBouncer Connection Pooler
* Azure Monitor / Log Analytics Workspace

## Relationships
* Core Claims Domain -> Claim State & Domain Store: SQL / ADO.NET [TLS]
* Adjuster BFF -> Read Model & Cache Store: SQL / Entity Framework Core [TLS]
* Core Claims Domain -> Audit & Compliance Log Store: Internal DB Write [TLS]
* Azure Database for PostgreSQL -> Azure Monitor / Log Analytics Workspace: Native Diagnostic Log Streaming [Encrypted]

## Technology Stack
* Azure Database for PostgreSQL Flexible Server: Chosen for native JSONB support, high availability, and managed infrastructure reducing cloud-inexperienced team overhead.
* pgaudit Extension: Provides granular session and object audit logging for insurance regulatory compliance without application-layer overhead.
* PgBouncer: Manages connection pooling to prevent exhaustion during peak loads.
* Azure Monitor / Log Analytics: Centralizes audit and diagnostic log streaming, keeping operational databases unburdened.

## Rationale
[This architecture uses a decomposed PostgreSQL structure with read replicas and caching to overcome legacy mainframe latency while guaranteeing zero data loss. It balances strict regulatory compliance and maintainability with operational simplicity for a cloud-novice team.]