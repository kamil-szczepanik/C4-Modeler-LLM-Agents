## Overview
[The Insurance Claims Modernization system gradually replaces a 30-year-old regional insurer mainframe with a modern Azure platform while legacy claims continue processing. It provides sub-2-second adjuster experiences through caching while maintaining strict consistency with the mainframe system of record.]

## Key Elements
- Claims Core Service (Java / Spring Boot on Azure App Service)
- Read-Through Cache (Azure Cache for Redis Standard Tier)
- Redis In-Memory Data Store (Component of Read-Through Cache)
- Eviction Policy Manager (Component using native `volatile-lru`)
- Cache Synchronization Listener (Component for invalidation events)
- Message Broker (Azure Service Bus)
- Integration & Anti-Corruption Layer (Azure Functions)

## Relationships
- Claims Core Service -> Redis In-Memory Data Store: `GET/SET` [Redis RESP / TCP over TLS]
- Azure Service Bus -> Cache Synchronization Listener: `ClaimInvalidated Event` [AMQP]
- Cache Synchronization Listener -> Redis In-Memory Data Store: `DEL {key}` [Redis RESP / TCP over TLS]
- Claims Core Service -> Integration & Anti-Corruption Layer: `Fetch Claim` [REST / HTTPS]

## Technology Stack
- Azure Cache for Redis: Manages high-performance in-memory caching to ensure screen loads under 2 seconds.
- Azure Service Bus: Handles asynchronous event-driven claim invalidations to prevent stale data.
- Java / Spring Boot: Powers core business logic with straightforward enterprise cloud deployment.

## Rationale
[This hybrid architecture bridges high-latency mainframe responses with modern sub-2-second UI requirements without overwhelming the team's cloud experience. Event-driven cache invalidation ensures zero data loss and rapid 1-day fallback capabilities to the mainframe.]