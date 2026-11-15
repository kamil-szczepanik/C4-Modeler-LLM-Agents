## Overview
[The Claims Orchestrator Container is the core backend service built in .NET Core that processes claims workflow logic, enforces business rules, and safely orchestrates hybrid data migration.]

## Key Elements
- API / Controller Layer
- Workflow Orchestrator (Saga Engine using MassTransit)
- Domain Service & Rules Engine
- Data Access Layer (Entity Framework Core & Transactional Outbox)
- Azure Container Apps
- Azure Service Bus
- Claims State Database (Azure SQL / Azure Cosmos DB)
- Azure App Configuration

## Relationships
- API Gateway -> API / Controller Layer: Routes requests [HTTPS/REST and gRPC]
- Workflow Orchestrator -> Domain Service: Evaluates business rules [In-memory C# calls]
- Data Access Layer -> Claims State Database: Persists transactional state [Database Protocol]
- Workflow Orchestrator -> Azure Service Bus: Publishes events and saga messages [AMQP]
- Workflow Orchestrator -> Azure App Configuration: Fetches feature flags for routing [HTTPS/REST]

## Technology Stack
- .NET Core / C#: Chosen for enterprise maintainability and robust cloud-native ecosystem support
- MassTransit: State machine saga framework implementing the Transactional Outbox pattern for zero data loss
- Entity Framework Core: Object-relational mapper for atomic state persistence and outbox management
- Azure Service Bus: Enterprise message broker ensuring reliable asynchronous communication
- Azure App Configuration: Stores feature flags for rapid one-day claim type rollback

## Rationale
[This architecture uses a saga-based orchestration pattern with MassTransit and Azure Service Bus to guarantee zero data loss and transactional consistency during hybrid migration. It isolates legacy mainframe dependencies via circuit breakers and feature flags, protecting user experience and enabling rapid rollback within one day.]