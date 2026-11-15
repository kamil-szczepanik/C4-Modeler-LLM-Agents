## Overview
[The Claims Core Container processes modernized and legacy claims using .NET on Azure Container Apps. It gradually replaces an on-premise mainframe while maintaining consistency and compliance.]

## Key Elements
- Claim Intake Controller (`ASP.NET Core API`)
- Claim Workflow Engine (`MassTransit / .NET`)
- Legacy Anti-Corruption Layer (ACL) Adapter (`IBM MQ`)
- Claim Domain Service (`C# / Domain-Driven Design`)
- Data Storage (`Azure SQL Database`)

## Relationships
- Claim Intake Controller -> Claim Workflow Engine: Dispatches commands (`In-Memory / MediatR`)
- Claim Workflow Engine -> Legacy ACL Adapter: Delegates unmigrated types (`AMQP / IBM MQ`)
- Claim Workflow Engine -> Message Broker: Emits domain events (`AMQP`)
- Claim Domain Service -> Azure SQL Database: Reads/Writes domain state (`Entity Framework Core / TDS`)

## Technology Stack
- .NET on Azure Container Apps: Chosen for core application runtime.
- MassTransit: Implements event-driven messaging and workflow routing.
- Azure SQL Database: Provides persistent transactional storage with Outbox pattern support.
- IBM MQ: Enables hybrid connectivity to the legacy on-premise mainframe.

## Rationale
[This architecture uses a modular internal design and Anti-Corruption Layer to safely isolate legacy mainframe dependencies. It enables gradual claim type migration while meeting strict consistency, rollback, and security requirements.]