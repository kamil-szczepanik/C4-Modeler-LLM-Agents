## Overview
[The Integration Worker is a .NET-based core component that safely synchronizes claim data between the new cloud platform and the legacy mainframe, satisfying R-04 and R-06.]

## Key Elements
- Message Listener Component (.NET / C#, AMQP)
- Transformation Engine Component (.NET / C#)
- Outbox/Retry Dispatcher Component (.NET / C#)
- Integration Audit Logger Component (.NET / C#)
- Circuit Breaker Policy Manager (.NET / C#, Polly)
- Feature/Kill-Switch Component (.NET / C#, ASP.NET Core Minimal APIs)

## Relationships
- Message Listener -> Transformation Engine [In-process, Direct Method Calls]
- Transformation Engine -> Outbox Dispatcher [In-process, Direct Method Calls]
- Outbox Dispatcher -> ACL Gateway [HTTPS/REST]
- Integration Worker -> Azure Service Bus [AMQP]
- Integration Audit Logger -> Azure Application Insights [HTTPS/REST]

## Technology Stack
- .NET / C#: Chosen for enterprise maintainability and team familiarity.
- Azure Service Bus: Used for reliable, decoupled asynchronous messaging.
- Polly: Implemented for circuit breaking and resilience against mainframe outages.
- ASP.NET Core Minimal APIs: Powers the administrative kill-switch for fast rollbacks.
- Azure Application Insights: Provides audit logging and observability.

## Rationale
[This component architecture ensures transactional consistency and reliable hybrid integration while strictly respecting the legacy mainframe's batch constraints. It directly operationalizes the one-day rollback and zero-data-loss requirements.]