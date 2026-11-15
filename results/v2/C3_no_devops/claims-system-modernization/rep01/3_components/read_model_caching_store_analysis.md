## Overview
[Hybrid Insurance Claims Modernization Platform: Gradually replaces a legacy COBOL/DB2 mainframe claims system with a modern Azure-based cloud platform while ensuring continuous processing.]

## Key Elements
- End Customers & Brokers
- Claims Adjusters
- Compliance/Audit Officers
- Legacy Mainframe
- Corporate Active Directory
- Read-Model & Caching Store (Azure Cosmos DB / Redis)
- Projection Consumer Component (.NET Background Service)
- Query API Component (.NET Minimal API)
- Distributed Cache Component (Azure Redis Cache)
- Document Store Component (Azure Cosmos DB - SQL API)

## Relationships
- Claims Core Domain Service -> Read-Model & Caching Store: Queries read-models and cache [TCP/TLS via gRPC]
- Projection Consumer Component -> Integration & Sync Worker: Consumes domain events [AMQP via Azure Service Bus]
- Query API Component -> Claims Core Domain Service: Exposes optimized query endpoints [TCP/TLS via gRPC]

## Technology Stack
- Azure Cosmos DB (SQL API): Persists schema-less JSON read models to handle mixed data structures for gradual migration (R-03)
- Azure Redis Cache: Handles ephemeral sessions and hot read-models with strict TTLs for sub-2-second adjuster screen loads (R-05)
- .NET Minimal API & Background Service: Implements Query API and Projection Consumer components for maintainable event processing
- Azure Key Vault: Stores Customer-Managed Keys (CMK) for encryption at rest across Cosmos DB and Redis

## Rationale
[This architecture uses a dedicated read-model and caching store to bypass mainframe latency, guaranteeing sub-2-second adjuster screens despite legacy constraints. Logical partitioning by claim type ensures seamless incremental migration and rapid one-day rollbacks.]