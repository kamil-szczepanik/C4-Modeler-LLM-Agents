## Overview
[The Insurance Claims Modernization system gradually replaces a legacy COBOL/DB2 mainframe with a modern Azure-based platform while maintaining uninterrupted claims processing. The Backend-for-Frontend (BFF) orchestrates interactions for the adjuster web application, utilizing caching and strict decoupling to satisfy performance and migration constraints.]

## Key Elements
- Claims Adjusters (End users)
- Backend-for-Frontend (BFF) (Azure Web Applications container)
- API Gateway / Anti-Corruption Layer (ACL) (Custom microservices on Azure)
- Caching / State Store (Azure Redis Cache)
- Event Broker (Azure Service Bus)
- COBOL/DB2 Mainframe (On-premises system of record)

## Relationships
- Claims Adjusters -> Backend-for-Frontend (BFF): Interact with the adjuster web application [HTTPS / REST]
- Backend-for-Frontend (BFF) -> API Gateway / Anti-Corruption Layer (ACL): Internal orchestration and data retrieval [HTTPS / gRPC]
- Backend-for-Frontend (BFF) -> Event Broker: Asynchronous event-driven migration [AMQP / MQTT]
- Backend-for-Frontend (BFF) -> Caching / State Store: Low-latency read models and session state [TCP / Redis Protocol]

## Technology Stack
- Azure Web Applications: Hosts the BFF due to managed scaling capabilities for a team with limited cloud experience.
- Azure Redis Cache: Externalizes session state and caches pre-aggregated read models to meet the 2-second UI latency requirement despite slow mainframe responses.
- OpenAPI / Swagger: Drives strongly-typed contract code generation to minimize integration overhead between frontend and backend services.
- Pact: Implements consumer-driven contract testing to validate schema changes during incremental claim migrations.
- W3C Trace Context: Powers distributed tracing across hybrid cloud and legacy on-premises environments.

## Rationale
[This architecture uses a thin, stateless BFF combined with externalized caching and modular handlers to isolate legacy mainframe dependencies and streamline incremental migrations. These design choices ensure sub-second UI performance, robust fault isolation, and the ability to roll back migrated claim types within one day.]