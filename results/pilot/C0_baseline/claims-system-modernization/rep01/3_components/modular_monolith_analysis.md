## Overview
Gradually replaces the legacy mainframe claims system with a hybrid cloud platform while ensuring uninterrupted processing. The architecture uses a modular monolith to isolate domain logic and support incremental migration.

## Key Elements
- ClaimManagement component
- PolicyVerification component
- DocumentHandling component
- Azure SQL Database
- Azure Service Bus
- Redis Cache
- In-Process Mediator

## Relationships
- ClaimManagement -> Azure SQL Database: Persists transactional data [T-SQL]
- ClaimManagement -> Azure Service Bus: Publishes asynchronous domain events [AMQP]
- ClaimManagement -> Redis Cache: Updates read-model projections [Redis Protocol]
- Components -> In-Process Mediator: Communicates via strongly-typed domain events [In-Process]

## Technology Stack
- Node.js with TypeScript: Core runtime for clean domain encapsulation
- Azure SQL Database: Relational storage utilizing transactional outbox pattern
- Azure Service Bus: Asynchronous messaging broker for event-driven consistency
- Redis Cache: High-performance storage for low-latency adjuster screen reads
- TSyringe or Inversify: Dependency inversion container for strict module boundaries

## Rationale
The modular monolith isolates business logic and domain boundaries without the operational overhead of microservices, accommodating the team's limited cloud experience. Asynchronous eventing and Redis projections decouple high-performance UI reads from slower backend processes to meet strict performance requirements.