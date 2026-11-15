## Overview
The Polyglot Persistence Layer manages hybrid data storage for the modern claims platform during the 3-year mainframe migration. It provides schema flexibility, strong transactional consistency, and native change data capture to ensure zero data loss.

## Key Elements
- Document Store (Azure Cosmos DB)
- Relational Store (Azure PostgreSQL)
- Managed CDC & Audit Streamer (Azure Event Hubs)
- Claims Core Engine
- Reconciliation Service & Audit System
- Migration Operations Dashboard

## Relationships
- Claims Core Engine -> Document Store (Azure Cosmos DB): HTTPS/TCP via Cosmos SDK for CRUD operations
- Claims Core Engine -> Relational Store (Azure PostgreSQL): TCP/IP via JDBC for transactional consistency
- Document Store & Relational Store -> Managed CDC & Audit Streamer (Azure Event Hubs): Native change streams
- Managed CDC & Audit Streamer -> Reconciliation Service & Audit System (AMQP/HTTPS) for audit logging
- Managed CDC & Audit Streamer -> Migration Operations Dashboard (WebSockets/HTTPS) for real-time tracking

## Technology Stack
- Azure Cosmos DB: Provides schema flexibility for migrating disparate claim types
- Azure PostgreSQL: Delivers strong transactional consistency for core claims data
- Azure Event Hubs: Powers fully managed native change data capture (CDC) to minimize operational toil for an inexperienced cloud team
- OpenTelemetry: Enforces distributed tracing across databases to meet strict sub-2s latency requirements

## Rationale
This polyglot architecture balances schema flexibility for incremental claim type migration with strong transactional consistency and auditability. Utilizing fully managed Azure services mitigates operational risks for a team with limited cloud experience while ensuring robust rollback capabilities.