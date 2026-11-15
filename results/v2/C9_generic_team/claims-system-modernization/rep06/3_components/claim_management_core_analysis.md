## Overview
The Claims Management Core processes modern insurance claims while supporting incremental migration from a 30-year-old mainframe. It ensures high reliability and fast adjuster interfaces in a hybrid cloud environment.

## Key Elements
- Claim Management Core (Azure App Service): Central processing container
- Modular Domain Packages (Auto, Property): Internal bounded contexts
- Outbox Table & Dispatcher: Reliability mechanism for event publishing
- Azure Service Bus: Asynchronous message broker
- ACL Gateway Interface: Boundary mapping to the legacy system
- Cache / Read Model Store: Optimized storage for fast queries

## Relationships
- BFF -> Claim Management Core: Sends HTTPS/REST requests
- Claim Management Core -> Azure Service Bus: Publishes domain events via AMQP
- Claim Management Core -> Cache / Read Model Store: Updates and queries read models via TCP/SQL
- Claim Management Core -> Anti-Corruption Layer (ACL): Translates legacy protocols via secure adapters

## Technology Stack
- Hexagonal Architecture (Ports and Adapters): Isolates core business logic from infrastructure
- Command Query Responsibility Segregation (CQRS): Optimizes write consistency and read performance (<2s UI load)
- Mediator Pattern (MediatR): Decouples request handlers within domain modules
- Outbox Pattern & Polly: Ensures zero-data-loss consistency (R-04) and network resilience

## Rationale
This architecture uses proven patterns like CQRS and Hexagonal design to isolate legacy complexity and manage limited cloud experience. It guarantees strict consistency and fast rollbacks without altering the restricted mainframe interfaces.