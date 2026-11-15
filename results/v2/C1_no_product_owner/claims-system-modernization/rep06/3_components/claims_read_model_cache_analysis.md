## Overview
[The Claims Read Model & Cache component provides low-latency materialized views of insurance claims to ensure sub-2-second adjuster screen loads while maintaining integration with the legacy mainframe system.]

## Key Elements
- Read Model Synchronizer (Azure Function, Node.js/TypeScript)
- Materialized View Store (Azure Cosmos DB, SQL API)
- Integration & Sync Engine (Azure Event Hubs)
- Adjuster Workspace Backend

## Relationships
- Integration & Sync Engine -> Read Model Synchronizer [AMQP]
- Read Model Synchronizer -> Materialized View Store [HTTPS / Cosmos SDK]
- Adjuster Workspace -> Materialized View Store [HTTPS / Cosmos SDK]

## Technology Stack
- Azure Cosmos DB (SQL API): Selected for native single-digit millisecond latency to satisfy R-05 without operational overhead.
- Azure Functions (TypeScript): Serverless compute for event processing with automatic scaling based on Event Hubs lag.
- Azure Managed Identities & RBAC: Eliminates static connection strings for secure, passwordless service authentication.
- Azure Private Endpoints: Restricts database network traffic within a secure virtual network boundary.

## Rationale
[This component architecture meets strict performance and security requirements by utilizing managed serverless compute and low-latency NoSQL storage protected by private networking and RBAC. Omitting intermediary caching layers reduces operational complexity while strictly enforcing PII compliance and data isolation.]