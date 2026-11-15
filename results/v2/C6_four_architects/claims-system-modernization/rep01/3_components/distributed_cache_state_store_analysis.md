## Overview
This architecture modernizes a regional insurer's legacy mainframe claims system by deploying a hybrid cloud platform on Azure West Europe. It enables online claim submission and adjuster workflows while maintaining data consistency and supporting rapid fallbacks.

## Key Elements
- Customers & Brokers
- Claims Adjusters
- Customer Portal (React / TypeScript SPA)
- Web Frontend (React / TypeScript SPA)
- API Gateway / BFF (Node.js / Express)
- Claims Core Service (.NET 8 / C#)
- Integration & Sync Worker (Python / C# Azure Function)
- Claims Database (Azure SQL Database Managed Instance)
- Integration Event Broker (Azure Service Bus)
- Distributed Cache / State Store (Azure Cache for Redis)
- Configuration & Feature Store (Azure App Configuration)
- Legacy Mainframe (COBOL / DB2 on-premise)
- Active Directory / Entra ID Connect

## Relationships
- Customers & Brokers -> Customer Portal: Submits claims [HTTPS / TLS 1.3]
- Claims Adjusters -> Web Frontend: Manages claims [HTTPS / TLS 1.3]
- Customer Portal -> API Gateway / BFF: Routes API requests [HTTPS / TLS 1.3]
- Web Frontend -> API Gateway / BFF: Routes API requests [HTTPS / TLS 1.3]
- API Gateway / BFF -> Claims Core Service: Dispatches core operations [gRPC / TLS]
- Claims Core Service -> Claims Database: Reads/writes claims data [TDS / TLS 1.3]
- Claims Core Service -> Integration Event Broker: Publishes domain events [AMQP over TLS]
- Integration & Sync Worker -> Legacy Mainframe: Synchronizes data [MQ / TCP]
- Distributed Cache / State Store components:
  - Idempotency State Manager (Redis `SETNX` / TTL)
  - Distributed Session Provider (Redis Sessions)
  - Migration Routing & Fallback Cache (Redis Hashes)
  - Distributed Lock Manager (Redlock pattern)
  - Eviction & Expiration Policy Engine (`volatile-lru`)
- Claims Core Service -> Distributed Cache / State Store: Manages session cache and idempotency [Redis RESP / TCP over TLS]
- Integration & Sync Worker -> Idempotency State Manager: Prevents event replay [Redis RESP / TCP over TLS]
- Claims Core Service -> Migration Routing & Fallback Cache: Evaluates migration status [Redis RESP / TCP over TLS]
- Integration & Sync Worker -> Distributed Lock Manager: Acquires synchronization locks [Redis RESP / TCP over TLS]

## Technology Stack
- Azure (West Europe) & On-Premise Hybrid: Matches infrastructure constraints and data residency needs.
- React & TypeScript: Modern responsive SPA frameworks for customer portal and adjuster web apps.
- Node.js & Express: Lightweight API Gateway / BFF for frontend routing.
- .NET 8 / C#: Robust enterprise runtime for the core claims processing logic.
- Azure SQL Database Managed Instance: Fully managed relational database ensuring ACID consistency for migrated claims.
- Azure Service Bus: Reliable message broker for asynchronous event-driven integration.
- Azure Cache for Redis: Low-latency distributed cache satisfying sub-2-second adjuster screen performance goals (R-05).
- Azure App Configuration: Centralized management of application settings and feature flags.
- Python / C# Azure Functions: Flexible serverless workers for background synchronization and integration tasks.

## Rationale
The hybrid architecture balances low-risk incremental migration with strict consistency requirements, ensuring no claims are lost or duplicated while isolating expensive mainframe interactions. Redis caching and asynchronous synchronization bridge legacy performance gaps, enabling sub-2-second UI responses and 1-day fallback capabilities despite limited team cloud experience.