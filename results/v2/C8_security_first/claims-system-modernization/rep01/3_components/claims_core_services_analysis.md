## Overview
The Claims Core Services component modernizes the regional insurer's claims platform via a hybrid architecture. It gradually migrates claim types from a 30-year-old mainframe while ensuring zero data loss and fast rollback capabilities.

## Key Elements
- Claim Domain Model / Business Engine (.NET 8, C#)
- Migration Router & Feature Toggles Component (.NET 8)
- Idempotency & Outbox Processor (.NET 8, EF Core)
- Event-Sourced State Store Component (.NET 8, Azure SQL)
- Resilience & Circuit Breaker Component (.NET 8, Polly)

## Relationships
- Claims API Gateway -> Resilience & Circuit Breaker Component [HTTPS / JSON]
- Resilience Component -> Claim Domain Model [In-Process]
- Migration Router -> Integration ACL Worker [AMQP via Azure Service Bus]
- Claim Domain Model -> Event-Sourced State Store [T-SQL / TDS]
- Claim Domain Model -> Outbox Processor [In-Process]
- Outbox Processor -> Azure Service Bus [AMQP]

## Technology Stack
- .NET 8 / C#: Core component framework for strong typing and enterprise reliability
- Azure Container Apps: Scalable container runtime utilizing managed serverless orchestration
- Azure SQL Database: Relational datastore with Transparent Data Encryption and immutable tables
- Polly: Resilience library for circuit breaking and graceful degradation during mainframe latency
- Azure Service Bus: Asynchronous message broker with Dead Letter Queues (DLQs)

## Rationale
This architecture decouples the modern web frontends from legacy mainframe constraints using asynchronous outbox messaging and circuit breakers. It provides strict idempotency and auditability to prevent data loss while supporting one-day rollbacks during the multi-year migration.