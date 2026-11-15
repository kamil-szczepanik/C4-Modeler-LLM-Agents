## Overview
[Hybrid Insurance Claims Modernization Platform gradually replaces a 30-year-old COBOL/DB2 mainframe with a cloud-native Azure architecture while maintaining business continuity. The Integration & Sync Worker ensures reliable, asynchronous data synchronization and consistency between the legacy system and new Azure services.]

## Key Elements
- **People:** End Customers & Brokers, Claims Adjusters, Compliance/Audit Officers, Business Operations / Support Team
- **External Systems:** Legacy Mainframe, Corporate Active Directory, Enterprise Service Bus (ESB), Audit & Compliance System
- **Containers:** Azure Functions (Integration & Sync Worker), Azure SQL Database, Azure Service Bus, Azure Key Vault, Azure Blob Storage / Cosmos DB
- **Components:** Mainframe Adapter Component (.NET Isolated Worker), Sync Orchestrator Component, Dead-Letter & Audit Handler Component, Replay API Controller Component, State & Deduplication Store

## Relationships
- **Integration & Sync Worker -> Enterprise Service Bus:** Asynchronous event messaging [Azure Service Bus via AMQP, secured by IPsec VPN/ExpressRoute]
- **Mainframe Adapter -> ESB:** Legacy payload transmission [mTLS, IPsec encryption]
- **Support Team -> Replay API Controller:** Manual transaction recovery [HTTPS via TLS 1.3, Azure Entra ID token validation]
- **Sync Orchestrator -> Azure SQL Database:** Transactional state and idempotency tracking [ADO.NET / Entity Framework Core]

## Technology Stack
- **Azure Functions:** Serverless execution for lightweight, scalable asynchronous event processing.
- **.NET Isolated Worker (.NET):** High-performance backend development supporting robust enterprise patterns.
- **Polly:** Fault-handling library providing exponential backoff retries and circuit-breaking for legacy stability.
- **Azure SQL Database:** Relational data store implementing the Outbox Pattern and idempotency deduplication.
- **Azure Key Vault & Managed Identities:** Secure credential storage eliminating plaintext secrets in application code.

## Rationale
[The hybrid architecture isolates expensive mainframe constraints while leveraging cloud elasticity to meet sub-2-second performance targets. Strict transactional guarantees and asynchronous queues ensure zero data loss (R-04) during gradual claim type migrations.]