## Overview
The Insurance Claims Modernization system gradually replaces a 30-year-old COBOL/DB2 mainframe with a modern hybrid cloud platform. It enables online claim submission and adjuster workflows while maintaining synchronization with the legacy system of record.

## Key Elements
- Customer / Broker (User)
- Claims Adjuster (User)
- Legacy Mainframe System (On-Premises System of Record)
- Active Directory (Identity Provider)
- Core Claims Service (.NET Core, Azure Container Apps)
- Claim Domain Model (Internal Component: Business logic)
- Mainframe Anti-Corruption Layer (Internal Component: Format translation)
- Outbox Processor (Internal Component: Reliable message queuing)
- Dual-Write / Sync Coordinator (Internal Component: State synchronization)

## Relationships
- Customer / Broker -> Web App Portal: Submits claims [HTTPS]
- Claims Adjuster -> Web App Portal: Manages claims [HTTPS]
- Web App Portal -> Claims API Gateway: Forwards API requests [REST/HTTPS]
- Claims API Gateway -> Core Claims Service: Routes requests [gRPC/HTTPS]
- Claim Domain Model -> Mainframe ACL: Delegates unmigrated types [Internal C# Interface]
- Claim Domain Model -> Outbox Processor: Persists events [EF Core / TDS]
- Outbox Processor -> Integration & Sync Service: Publishes events [AMQP / Azure Service Bus]
- Mainframe ACL -> Integration Gateway: Sends legacy updates [REST/HTTPS]
- Web App Portal -> Active Directory: Authenticates users [OpenID Connect / OAuth 2.0]

## Technology Stack
- Azure Container Apps: Serverless Kubernetes abstraction reducing cloud complexity for the team
- .NET Core / C#: Core runtime for the modern claims microservices and domain model
- Azure Service Bus: AMQP messaging broker ensuring reliable, asynchronous event delivery
- Azure SQL Database: Relational storage for modern claim records via TDS/ADO.NET

## Rationale
The hybrid architecture uses an Anti-Corruption Layer and asynchronous outbox pattern to safely isolate the new platform from legacy mainframe latency and costly interface constraints. This ensures zero data loss, supports incremental claim type migration, and allows a one-day rollback capability.