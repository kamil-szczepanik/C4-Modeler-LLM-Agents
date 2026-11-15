## Overview
[The system modernizes a 30-year-old mainframe claims system through a hybrid cloud architecture while legacy processing continues. The Read Model Projector component asynchronously updates read models to ensure low-latency adjuster screens.]

## Key Elements
- Event Consumer Component (Azure Functions / .NET) with Checkpoint & Idempotency Filter
- Projection Handler Component (.NET Class Library)
- Database Writer Component (.NET / Cosmos DB SDK)
- Message Broker (IBM MQ)
- Adjuster Read Database (Azure Cosmos DB)

## Relationships
- Message Broker -> Event Consumer: Pulls domain events [AMQP / IBM MQ]
- Event Consumer -> Projection Handler: Dispatches raw payloads [In-memory C# calls]
- Projection Handler -> Database Writer: Sends transformed read models [In-memory C# calls]
- Database Writer -> Adjuster Read Database: Persists state and secures private connectivity [HTTPS / Cosmos DB SDK over Private Endpoints]

## Technology Stack
- Azure Functions (.NET): Chosen for serverless execution to mitigate the team's limited cloud experience.
- Azure Cosmos DB: Provides partitioned storage to achieve adjuster screen loads under 2 seconds.
- IBM MQ: Handles reliable enterprise messaging and event distribution.
- OpenTelemetry & Application Insights: Tracks distributed tracing, consumer lag, and projection latency.
- Azure Managed Identity & VNet Integration: Enforces zero-trust security and secretless authentication.

## Rationale
[This decoupled, serverless architecture simplifies cloud adoption while satisfying stringent performance and consistency requirements. Robust idempotency filters and private networking ensure zero data loss and regulatory compliance during incremental migration.]