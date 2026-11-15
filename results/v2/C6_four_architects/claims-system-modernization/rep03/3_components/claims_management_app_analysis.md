## Overview
[The system is the Claims Management App component, a core backend service modernizing a legacy regional insurer's mainframe claims platform. Its primary purpose is to process modern claims securely, handle gradual claim type migrations, and ensure hybrid interoperability.]

## Key Elements
* Claim Processing Controller (.NET 8 Web API)
* Claim Domain Model (.NET 8 / EF Core)
* Outbox Transaction Processor (.NET 8 Background Service)
* Mainframe Adapter (.NET 8 / Polly)
* Feature & Routing Switcher (.NET 8 In-Memory Service)
* Authorization & Context Enforcer (ASP.NET Core Middleware)
* Event Dispatcher (Azure Service Bus Client)

## Relationships
* Claim Processing Controller -> Claim Domain Model: Direct in-memory C# method calls [Synchronous]
* Claim Domain Model -> Claims Database: Entity Framework Core [TDS]
* Outbox Transaction Processor -> Event Dispatcher: Background polling and publishing [AMQP / Azure Service Bus]
* Mainframe Adapter -> Claim Routing Service: Low-latency routing and fallback [gRPC]
* Authorization & Context Enforcer -> All Controllers: Request interception [HTTP / JWT]

## Technology Stack
* .NET 8 (C#): Chosen for robust type safety, high performance, and built-in resilience libraries.
* Entity Framework Core & SQL Database: Ensures transactional consistency and atomic outbox writes via TDS.
* Polly: Implements Circuit Breaker patterns to isolate slow mainframe responses (up to 5s).
* Azure Service Bus: Handles asynchronous, reliable messaging via AMQP.
* ASP.NET Core Middleware: Enforces zero-trust security and Active Directory JWT validation.

## Rationale
[This architecture fits the requirements by decoupling slow legacy dependencies via Polly circuit breakers and in-memory routing switches to meet sub-2s UI performance and one-day rollback constraints. Furthermore, the Transactional Outbox pattern guarantees zero data loss or duplication across the hybrid Azure and mainframe boundary.]