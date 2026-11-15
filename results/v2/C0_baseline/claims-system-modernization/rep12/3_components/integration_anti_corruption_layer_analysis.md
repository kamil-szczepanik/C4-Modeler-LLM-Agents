## Overview
The system modernizes a regional insurer's 30-year-old mainframe by introducing a cloud-based platform using a strangler fig migration strategy. It enables online claims submission and adjuster workflows while keeping the mainframe as the system of record.

## Key Elements
- Integration & Anti-Corruption Layer (.NET Core / MassTransit)
- Translation Engine (.NET Core / FluentValidation)
- Outbox Processor (MassTransit / Entity Framework Core / Azure SQL Serverless)
- Async Sync Worker (MassTransit / Polly)
- Routing & Feature Router (Azure App Configuration)
- Legacy Mainframe (COBOL/DB2)
- Azure API Management

## Relationships
- API Gateway -> Integration & Anti-Corruption Layer [Internal HTTPS/gRPC]
- Integration & Anti-Corruption Layer -> Legacy Mainframe [IBM MQ over mTLS]
- Outbox Processor -> Azure SQL Serverless [ADO.NET / EF Core]
- Routing & Feature Router -> Azure App Configuration [REST / HTTPS]

## Technology Stack
- .NET Core: Selected for building high-performance, maintainable microservices with strong enterprise support.
- MassTransit: Chosen to implement reliable messaging patterns and handle asynchronous workflows.
- Azure SQL Serverless: Provides ACID guarantees for the Transactional Outbox pattern to prevent lost claims.
- IBM MQ: Ensures secure, enterprise-grade messaging protocol with the on-premise mainframe.
- Azure App Configuration: Manages dynamic feature flags for gradual claim-type migration and rollbacks.

## Rationale
This hybrid architecture isolates expensive mainframe changes through an anti-corruption layer while ensuring sub-second UI performance. It guarantees transactional consistency and enables a risk-free, one-by-one claim migration path with rapid rollback capabilities.