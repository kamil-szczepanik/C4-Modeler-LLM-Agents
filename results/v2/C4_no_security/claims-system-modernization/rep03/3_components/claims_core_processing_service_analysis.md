## Overview
The Insurance Claims Modernization system gradually replaces a 30-year-old COBOL/DB2 mainframe with a cloud-native platform. It ensures zero claim loss and rapid adjuster response times during a phased, multi-year migration.

## Key Elements
- Claims Workflow Orchestrator (MassTransit State Machine)
- Claim Domain Model (.NET Core)
- Mainframe Sync Coordinator (.NET Core with Polly)
- Payout & Ledger Engine (.NET Core)
- Azure Container Apps (ACA)
- Azure Service Bus with DLQ
- Azure SQL Database

## Relationships
- Claims Workflow Orchestrator -> Claim Domain Model: Invokes [In-process]
- Claims Workflow Orchestrator -> Payout & Ledger Engine: Initiates disbursements [In-process]
- Claims Workflow Orchestrator -> Azure SQL Database: Persists state [Entity Framework Core / T-SQL]
- Claims Workflow Orchestrator -> Azure Service Bus: Dispatches domain events [AMQP]
- Mainframe Sync Coordinator -> Mainframe Integration Adapter: Syncs dual-writes [gRPC/HTTPS]

## Technology Stack
- .NET Core / C#: Chosen for high performance and strong typing.
- Azure Container Apps (ACA) with KEDA: Simplifies event-driven scaling with low cloud experience.
- MassTransit: Manages sagas and state machines to guarantee consistency.
- Polly: Implements circuit breakers for resilient mainframe integration.
- Azure SQL Database: Provides reliable relational persistence and audit trails.
- Bicep: Manages Infrastructure as Code to prevent drift.

## Rationale
This hybrid architecture uses event-driven microservices on Azure to decouple the modern web UI from slow mainframe latency. It guarantees strict consistency and rapid fallback capabilities required during the 3-year migration.