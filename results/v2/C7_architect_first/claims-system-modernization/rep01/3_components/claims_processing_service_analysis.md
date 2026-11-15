## Overview
This architecture modernizes a regional insurer's claims platform by gradually migrating claim types from a 30-year-old mainframe to an Azure-based cloud environment. It ensures business continuity and data consistency via a hybrid integration pattern during the multi-year transition.

## Key Elements
- **Claims Orchestrator Component**: .NET/C# state machine managing claim lifecycles and idempotency.
- **Claim Type Adapter Component**: Strategy-pattern implementation for isolated feature toggling and rapid rollbacks.
- **Validation & Rules Engine Component**: Evaluates business logic locally before persistence.
- **Idempotency & Outbox Processor Component**: Ensures exactly-once processing and handles circuit breaking during batch windows.
- **Audit Logging Component**: Captures immutable business events using Azure SQL Ledger.

## Relationships
- **Claims Orchestrator** -> **Claim Type Adapter**: Invokes type-specific workflows via In-process C# Interfaces.
- **Claim Type Adapter** -> **Claims Database**: Persists state changes via Entity Framework Core [TDS / SQL].
- **Claims Orchestrator** -> **Idempotency & Outbox Processor**: Persists outbox messages transactionally [In-process / C#].
- **Claims Orchestrator** -> **Audit Logging Component**: Emits audit trails [In-process / C#].
- **Idempotency & Outbox Processor** -> **Claims Database**: Stores deduplication keys [TDS / SQL].

## Technology Stack
- **.NET Core**: Core runtime for business logic and components, chosen for enterprise maturity.
- **Azure Container Apps**: Hosting platform for microservices, simplifying operations for teams with limited cloud experience.
- **Azure SQL with SQL Ledger**: Primary database offering tamper-evident audit logs for regulatory compliance.
- **Azure Service Bus**: Asynchronous messaging backbone handling hybrid sync without blocking core workflows.
- **Azure App Configuration & Key Vault**: Centralized feature toggles for rollbacks and secure secret/PII management.

## Rationale
The hybrid architecture uses Clean Architecture principles and an outbox pattern to decouple the modern cloud platform from fragile mainframe dependencies. This isolates high-cost mainframe changes, guarantees sub-second adjuster UI performance, and enables one-day rollbacks per claim type.