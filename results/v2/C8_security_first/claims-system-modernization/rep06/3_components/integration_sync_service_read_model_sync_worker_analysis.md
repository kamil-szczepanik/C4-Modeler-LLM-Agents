## Overview
[The system is a modern hybrid cloud platform that gradually replaces a legacy 30-year-old mainframe claims system while maintaining continuous processing. Its core purpose is to enable incremental claim type migration and fast adjuster user experiences without disrupting core operations.]

## Key Elements
*   [Azure Container Apps (ACA) Background Workers for Integration/Sync Service & Read-Model Sync Worker]
*   [Inbound Event Router component (.NET 8 Isolated Worker)]
*   [Read-Model Projection Engine component]
*   [Legacy Sync Bridge & Mainframe Adapter component]
*   [Azure Service Bus with AMQP protocol]
*   [Azure Cache for Redis for Idempotency Ledger]
*   [Azure Cosmos DB / PostgreSQL read-database]
*   [On-premise COBOL/DB2 Mainframe]

## Relationships
*   [Claims Core Service -> Azure Service Bus: Event streaming via AMQP]
*   [Azure Service Bus -> Inbound Event Router: Message consumption via AMQP]
*   [Inbound Event Router <-> Azure Cache for Redis: Deduplication checks via RESP]
*   [Legacy Sync Bridge -> On-premise COBOL/DB2 Mainframe: Bi-directional state synchronization via IPSec VPN / Azure ExpressRoute]
*   [Read-Model Projection Engine -> Azure Cosmos DB / PostgreSQL: Read-model updates]

## Technology Stack
*   [.NET 8 (Isolated Worker model): Chosen for high-throughput messaging and robust dependency injection]
*   [Azure Container Apps (ACA): Chosen over Durable Functions for simpler operations given the team's cloud experience]
*   [Azure Service Bus: Chosen for reliable messaging, sessions, and Dead-Letter Queue support]
*   [Azure Cache for Redis: Chosen for sub-millisecond distributed locking and idempotency checks]
*   [IPSec VPN / Azure ExpressRoute: Chosen for secure, encrypted hybrid connectivity to the on-premise mainframe]

## Rationale
[This hybrid architecture insulates adjusters from mainframe latency to meet performance goals while using robust messaging and idempotency controls to prevent data loss. Standardizing on simpler containerized workers matches the team's skill level and ensures reliable, gradual migration.]