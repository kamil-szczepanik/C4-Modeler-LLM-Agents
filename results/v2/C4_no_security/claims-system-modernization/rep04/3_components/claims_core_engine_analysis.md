## Overview
[The system is a hybrid cloud Claims Core Engine built with Java Spring Boot to modernize a regional insurer's claims platform. Its core purpose is to gradually migrate claim types from a 30-year-old mainframe while ensuring continuous processing and data consistency.]

## Key Elements
- Claim Orchestrator (Spring State Machine)
- Feature Router Component (Azure App Configuration)
- Synchronization & Reconciliation Adapter
- Data Access Facade (Spring Data JPA)
- Resilience & Caching Proxy (Resilience4j)
- Telemetry Interceptor (OpenTelemetry)

## Relationships
- Claims Core Engine -> Azure Service Bus: Publishes and consumes asynchronous messages [AMQP]
- Claims Core Engine -> Integration Mediator: Communicates domain events and legacy traffic [TCP/MQ, HTTPS]
- Claims Core Engine -> Polyglot Persistence Layer: Reads and writes claim state [PostgreSQL, Azure Cosmos DB]
- Claims Core Engine -> Azure Key Vault: Retrieves secrets using managed identities [HTTPS]

## Technology Stack
- Java Spring Boot: Core framework for application logic and component wiring
- Spring State Machine: Manages complex claim lifecycles across mixed states
- Resilience4j: Implements circuit breakers to isolate legacy mainframe latency
- OpenTelemetry: Provides distributed tracing across hybrid infrastructure
- Azure App Configuration: Externalizes feature flags for business-driven rollbacks
- Terraform: Manages immutable infrastructure-as-code deployments

## Rationale
[This architecture cleanly separates hybrid integration logic from domain processing using resilient proxies and decoupled event patterns. It guarantees strict performance, consistency, and rapid one-day rollback capabilities despite team cloud inexperience.]