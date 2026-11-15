## Overview
[The system modernizes a 30-year-old regional insurance mainframe by gradually migrating claims handling to a hybrid cloud platform while legacy processing continues. It ensures zero claim loss, sub-2-second adjuster screens, and rapid one-day rollback capabilities.]

## Key Elements
- Claim Orchestrator Component (.NET Core / Mediator pattern)
- Claim Domain Model Component (.NET Core)
- Rollback Switch Component (.NET Core / Feature Flag pattern)
- Claim Audit & Event Publisher Component (.NET Core / Outbox Pattern)
- Azure Container Apps (.NET Core runtime)
- Azure Cosmos DB (Claims Audit Store)
- Azure Service Bus (Integration & Anti-Corruption Layer)
- Azure Key Vault (Secrets and CMK management)

## Relationships
- Claim Orchestrator -> Claim Domain Model: In-memory domain method calls [Direct]
- Claim Orchestrator -> Integration & Anti-Corruption Layer: Publishes domain events [AMQP (Azure Service Bus)]
- Rollback Switch -> Mainframe Adapter: Forwards unmigrated claim traffic [gRPC with payload signing]
- Claim Domain Model -> Claim Audit & Event Publisher: Raises domain events [In-memory / MediatR]
- Claim Audit & Event Publisher -> Claims Audit Store: Persists audit records [HTTPS (Document API)]
- Claim Audit & Event Publisher -> Integration & Anti-Corruption Layer: Dispatches integration events [AMQP]

## Technology Stack
- .NET Core: Selected for high-performance domain logic and microservice development
- Azure Container Apps: Chosen for serverless container orchestration with minimal cloud management overhead
- Azure Service Bus: Provides reliable asynchronous messaging using AMQP
- Azure Cosmos DB: Stores audit events with high availability and consistency
- Azure Key Vault: Secures PII encryption keys and managed identities

## Rationale
[This architecture decouples modern claim processing from the legacy mainframe using CQRS and the Outbox pattern, ensuring high performance and data consistency. The componentized design enforces strict security boundaries and supports the required 3-year hybrid coexistence and rapid rollback capabilities.]