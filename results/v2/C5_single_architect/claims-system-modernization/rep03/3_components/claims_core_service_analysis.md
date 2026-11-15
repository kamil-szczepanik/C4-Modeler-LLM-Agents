## Overview
The Claims Core Service container uses a modular .NET Core component architecture deployed in Azure Container Apps to gradually migrate claim types from a legacy mainframe. It ensures high performance, transactional consistency, and rapid rollback capabilities during the hybrid cloud transition.

## Key Elements
- Claim Submission Controller (.NET Core API)
- Claims Router / Strategy Selector (.NET Core)
- Claim Workflow Engine (.NET Core / Workflow Core)
- Data Access Repository (Entity Framework Core)
- Mainframe Sync Publisher (.NET Core)
- Outbox Processor (.NET Core Background Service)
- Mainframe Anti-Corruption Client (.NET Core)

## Relationships
- API Gateway -> Claim Submission Controller: Routes incoming requests [gRPC]
- Claim Submission Controller -> Claims Router / Strategy Selector: Forwards requests for evaluation [In-Memory]
- Claims Router / Strategy Selector -> Claim Workflow Engine: Executes modern claim workflows [In-Memory]
- Claims Router / Strategy Selector -> Mainframe Anti-Corruption Client: Forwards unmigrated claims [HTTP/AMQP]
- Claim Workflow Engine -> Data Access Repository: Persists state and domain models [EF Core / TDS]
- Data Access Repository -> Outbox Processor: Stores transactional outbox events [EF Core / TDS]
- Outbox Processor -> Integration Message Broker: Publishes reliable domain events [AMQP]
- Mainframe Sync Publisher -> Integration Message Broker: Synchronizes state with legacy system [AMQP]

## Technology Stack
- .NET Core: Selected for core components due to team familiarity and strong enterprise ecosystem
- Entity Framework Core / TDS: Manages relational persistence with Azure SQL Database ensuring ACID compliance
- Workflow Core: Manages complex state transitions for migrated claim types
- Azure Service Bus: Handles asynchronous messaging via AMQP for decoupling and event distribution
- Transactional Outbox Pattern: Prevents dual-write consistency issues between the database and message broker

## Rationale
This component architecture isolates complex routing and state management, allowing individual claim types to be migrated or rolled back within one day. Furthermore, the outbox pattern and anti-corruption client decouple the modern UI from slow mainframe responses, satisfying strict performance and consistency constraints.