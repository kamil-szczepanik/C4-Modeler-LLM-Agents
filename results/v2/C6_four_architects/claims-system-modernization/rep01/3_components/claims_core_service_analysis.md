## Overview
This system modernizes a regional insurer's 30-year-old COBOL/DB2 mainframe by gradually migrating claims processing to a hybrid Azure cloud platform. The architecture ensures business continuity, maintaining the legacy system as the system of record during the transition.

## Key Elements
- Feature Routing Dispatcher (.NET class library)
- Claim Command Processor (.NET class library using MediatR)
- Claim Query Handler (.NET class library)
- Domain Model / Aggregate Roots (.NET class library)
- Anti-Corruption Layer (ACL) (.NET class library)
- Mainframe Adapter Component (.NET class library)
- Idempotency Validator (StackExchange.Redis)
- Integration Event Publisher (Azure.Messaging.ServiceBus)

## Relationships
- Feature Routing Dispatcher -> Claim Command Processor: Delegates modern claim workflows [Internal C# Method Call]
- Feature Routing Dispatcher -> Mainframe Adapter Component: Delegates legacy fallback workflows [Internal C# Method Call]
- Claim Command Processor -> Idempotency Validator: Checks duplicate processing [Redis Protocol over TLS]
- Claim Command Processor -> Domain Model / Aggregate Roots: Executes business rules [Internal C# Method Call]
- Domain Model -> Anti-Corruption Layer (ACL): Translates domain models to legacy structures [Internal C# Method Call]
- Domain Model -> Integration Event Publisher: Emits state change events [AMQP over TLS (TCP 5671)]
- Claim Query Handler -> Claims Database: Reads optimized claim data [TDS over TLS (TCP 1433)]

## Technology Stack
- .NET 8 / C#: Chosen for core business logic implementation, aligning with team capabilities
- MediatR: Implements CQRS pattern to separate command and query workloads
- StackExchange.Redis: Manages distributed caching for idempotency and session state
- Azure Service Bus: Handles asynchronous, reliable integration event messaging
- Azure App Configuration: Stores dynamic feature flags for real-time fallback routing

## Rationale
The component architecture cleanly isolates legacy integration complexities to support a one-day rollback constraint. Additionally, it optimizes query performance to meet sub-second response targets despite underlying hybrid latency limitations.