## Overview
[The system modernizes a regional insurer's legacy COBOL/DB2 mainframe claims system by gradually migrating claim types to a hybrid Azure cloud platform. The Integration & Anti-Corruption Layer orchestrates dual-write synchronization, protocol translation, and state routing while protecting the legacy system.]

## Key Elements
- Mainframe Translation Adapter (.NET 8 / Azure Functions)
- Batch Window Throttler (Azure Service Bus)
- Dual-Write Router (.NET Core / Azure Functions with Durable Functions)
- Claim Provenance & Audit Registry (Azure Cosmos DB / Redis / Azure Table Storage)
- Claims Processing Service (.NET Core / Azure Container Apps)
- Mainframe Claims System (COBOL / DB2)

## Relationships
- Claims Processing Service -> Dual-Write Router [gRPC]
- Dual-Write Router -> Claim Provenance & Audit Registry [gRPC / Low-latency read-write]
- Mainframe Translation Adapter -> Claim Provenance & Audit Registry [gRPC]
- Mainframe Translation Adapter -> Mainframe Claims System [mTLS / TCP via ExpressRoute]

## Technology Stack
- .NET 8 / Azure Functions: Provides scalable serverless execution for payload translation and routing logic.
- Azure Service Bus: Queues and throttles messages to respect the strict nightly batch window (23:00-05:00).
- Azure Cosmos DB / Redis / Azure Table Storage: Maintains real-time claim provenance and routing state for rapid fallback (R-06).
- Azure Key Vault & Managed Identities: Secures credentials, handles certificate lifecycle, and enforces least-privilege access.

## Rationale
[This architecture successfully isolates the brittle mainframe via anti-corruption patterns and resilient asynchronous queues, ensuring zero data loss during incremental migrations. It satisfies strict hybrid constraints, security mandates, and the 1-day fallback requirement while bridging low cloud experience through managed services.]