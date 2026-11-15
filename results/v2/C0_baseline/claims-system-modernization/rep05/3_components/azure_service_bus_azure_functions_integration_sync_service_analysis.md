## Overview
[Azure Service Bus & Azure Functions] provides an event-driven asynchronous synchronization and integration engine between cloud containers and the on-premise mainframe. It ensures zero lost claims during the hybrid migration while supporting rapid claim-type rollbacks.

## Key Elements
- Claim Event Topic (Azure Service Bus Topic)
- Sync Orchestrator Function (Azure Functions - C# isolated worker)
- Dead-Letter Manager Function (Azure Functions)
- Sync Metrics & Audit Publisher Function (Azure Functions)

## Relationships
- Azure Service Bus Topic -> Azure Functions: Pub/sub claim lifecycle event routing using AMQP
- Azure Functions -> Azure Cosmos DB & Mainframe Integration Adapter: State synchronization and event processing via HTTP/Service Bus
- Azure Functions -> Application Insights: Telemetry, distributed W3C tracing, and operational audit publishing

## Technology Stack
- Azure Service Bus: Managed pub/sub messaging and dead-letter queues chosen for reliability and low operational overhead
- Azure Functions (C# Isolated Worker): Serverless event processing selected to minimize custom infrastructure management
- Azure Virtual Network & Private Endpoints: Network isolation chosen to secure the hybrid integration boundary
- Managed Identities (Entra ID): Service-to-service authentication used to eliminate static connection strings
- Azure Key Vault: Customer-managed keys and payload encryption used for PII/PHI protection

## Rationale
This architecture uses managed Azure services to reduce operational complexity for a team with limited cloud experience. It directly satisfies consistency and maintainability requirements through robust dead-letter handling, idempotency, and automated audit logging.