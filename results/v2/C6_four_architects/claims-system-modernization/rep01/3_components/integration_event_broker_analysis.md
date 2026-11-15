## Overview
The system modernizes a 30-year-old regional insurance mainframe claims platform by gradually migrating claim types to a new cloud-based architecture. It uses a hybrid cloud model to ensure continuous operations and zero data loss during the 3-year migration window.

## Key Elements
- Customer & Broker (Users)
- Claims Adjusters (Users)
- Customer Portal & Web Frontend (React / TypeScript SPA)
- API Gateway / BFF (Node.js / Express)
- Claims Core Service (.NET 8 / C#)
- Integration & Sync Worker (Python / C# Azure Function)
- Claims Database (Azure SQL Database Managed Instance)
- Integration Event Broker (Azure Service Bus: Claim Ingestion Topic, Mainframe Outbox Queue, Dead-Letter Handler, Replay & Dead-Letter Manager, Access Control & Namespace Authorization, Broker Diagnostics & Metrics Publisher)
- Distributed Cache / State Store (Azure Cache for Redis)
- Configuration & Feature Store (Azure App Configuration)
- Legacy Mainframe (COBOL / DB2)
- Active Directory / Entra ID Connect

## Relationships
- Customer Portal & Web Frontend -> API Gateway / BFF: HTTPS / REST
- API Gateway / BFF -> Claims Core Service: gRPC / HTTPS
- Claims Core Service -> Claims Database: TDS (TCP 1433)
- Claims Core Service -> Claim Ingestion Topic: Publishes domain events using CloudEvents JSON schema [AMQP over TLS (TCP 5671)]
- Integration & Sync Worker -> Mainframe Outbox Queue: Consumes ordered messages using Service Bus Sessions [AMQP over TLS (TCP 5671)]
- API Gateway / BFF -> Claim Ingestion Topic: Publishes direct customer/broker submission events [AMQP over TLS]
- Integration Event Broker -> Integration & Sync Worker: Pushes batched synchronization payloads [AMQP over TLS]
- Legacy Mainframe -> Integration & Sync Worker: Batch file exchange / DB2 direct read-write (SFTP / ODBC)
- Customer Portal & Web Frontend -> Active Directory / Entra ID Connect: OpenID Connect (OIDC) / OAuth 2.0

## Technology Stack
- Azure Service Bus: Asynchronous event broker with topics, session-enabled queues, and DLQ for reliable hybrid integration.
- .NET 8 / C#: High-performance core backend microservices.
- React / TypeScript: Modern, responsive single-page applications for portals and adjusters.
- Node.js / Express: API Gateway and Backend-for-Frontend (BFF) layer.
- Azure SQL Database Managed Instance: Relational data store for migrated claims.
- Azure Cache for Redis: Distributed caching and state management for performance.
- Python / C#: Lightweight workers for legacy mainframe synchronization and batch processing.

## Rationale
This hybrid architecture isolates expensive mainframe dependencies while delivering a modern sub-second user experience. It guarantees zero data loss (R-04) and rapid one-day fallback (R-06) via event-driven decoupling and strict state synchronization.