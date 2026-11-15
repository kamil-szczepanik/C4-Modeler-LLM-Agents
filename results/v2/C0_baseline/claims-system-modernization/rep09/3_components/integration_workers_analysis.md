## Overview
[The system modernizes a 30-year-old regional insurer's claims platform via a hybrid architecture. It gradually migrates claim types to Azure while the legacy mainframe remains the system of record.]

## Key Elements
- Integration Workers (.NET, Azure Container Apps)
- Message Router Component (.NET / MassTransit)
- Mainframe Sync Adaptor Component (.NET / Polly)
- Audit & Reconciliation Component (.NET / EF Core)
- Claim State Evaluator Component (.NET)
- Telemetry Publisher Component (.NET / OpenTelemetry)
- Azure Service Bus
- Azure SQL Database
- Azure Key Vault
- Azure Application Insights

## Relationships
- Message Router -> Azure Service Bus: Consumes and publishes asynchronous messages [AMQP]
- Message Router -> Claim State Evaluator: Evaluates claim type routing rules [In-process]
- Mainframe Sync Adaptor -> Legacy Mainframe: Synchronizes legacy payloads and enforces rate-limiting [mTLS/HTTPS]
- Mainframe Sync Adaptor -> Azure Key Vault: Retrieves mTLS certificates and credentials [Managed Identity]
- Audit & Reconciliation -> Azure SQL Database: Writes cryptographically hashed, append-only audit logs [EF Core/T-SQL]
- Telemetry Publisher -> Azure Application Insights: Exports worker lag, metrics, and structured logs [OpenTelemetry]

## Technology Stack
- .NET: Core framework for high-performance background worker execution
- Azure Container Apps: Serverless container hosting tailored for low cloud experience
- MassTransit: Reliable messaging framework for asynchronous event handling
- Polly: Resilience library for circuit breakers and retry policies
- OpenTelemetry: Standardized telemetry and distributed tracing
- Azure Key Vault: Secure secret management via Managed Identities

## Rationale
[This hybrid architecture mitigates cloud experience risks through managed Azure services while ensuring zero data loss via strict audit logging and circuit breakers. It respects the legacy mainframe constraints by decoupling processing via asynchronous messaging.]