## Overview
The Library Management System provides self-service portals, circulation management, and cataloging for academic and public libraries. The Redis container acts as an in-memory data store providing session management, caching, and rate limiting strictly within EU boundaries.

## Key Elements
* **Session Store Component:** Manages active Patron and Librarian authentication states.
* **Catalog Cache Component:** Caches frequent catalogue metadata to offload PostgreSQL.
* **Rate Limiter Component:** Protects API Gateway from abuse on self-service endpoints using Lua scripting for atomicity.
* **Persistence & Replication Engine:** Handles asynchronous RDB/AOF snapshotting to EU-bound local storage.
* **Pub/Sub Messaging Component:** Manages event broadcasting for cache invalidation.
* **Cluster & Sentinel Management Component:** Handles node health checks and automatic failover.
* **Security & TLS Termination Component:** Manages inbound cryptographic handshakes using TLS 1.3.
* **EU Memory-Bound Storage Engine:** Enforces hardware/runtime constraints for EU-only data residency.

## Relationships
* **Core Domain Service -> Security & TLS Termination:** Sends session and metadata requests [RESP over TLS 1.3]
* **API Gateway -> Security & TLS Termination:** Sends rate-limit checks [RESP over TLS 1.3]
* **Security & TLS Termination -> Session, Cache, Rate Limiter Components:** Routes decrypted commands [In-Memory IPC]
* **Session Store & Catalog Cache -> Persistence & Replication Engine:** Asynchronously persists snapshots [Local I/O]
* **Core Domain Service -> Pub/Sub Messaging:** Publishes cache eviction events [RESP over TLS 1.3]
* **Pub/Sub Messaging -> Catalog Cache:** Triggers targeted key invalidations [In-Memory Call]

## Technology Stack
* **Redis:** In-memory data store chosen for sub-millisecond response times to meet the <800ms search NFR.
* **RESP Protocol over TLS 1.3:** Ensures secure, encrypted communication for data-in-transit within the EU.
* **Lua Scripting:** Executes atomic rate-limiting and session-refresh logic directly within the engine to prevent race conditions.
* **RDB/AOF Snapshotting:** Provides data durability without degrading single-threaded event loop performance.

## Rationale
This component architecture optimizes Redis for high availability and low latency while strictly enforcing EU data residency constraints. Background snapshotting and single-threaded execution ensure search performance SLAs are consistently met.