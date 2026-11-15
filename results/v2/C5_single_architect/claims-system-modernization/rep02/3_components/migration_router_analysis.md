## Overview
The Migration Router is a core hybrid container in the Insurance Claims Modernization platform, serving as an anti-corruption layer for dynamic claim routing. It orchestrates traffic between modern Azure services and the legacy on-premise mainframe while ensuring zero data loss and rapid fallback capabilities.

## Key Elements
* **Routing Controller (Spring Boot/Java):** Evaluates incoming claim types against the routing registry.
* **Feature Flag Manager (Redis Cache):** Enables instant fallback switchbacks to the mainframe within one day.
* **Anti-Corruption Layer (ACL) Mapper (MapStruct):** Translates modern JSON payloads to legacy formats.
* **Audit & Failover Logger (Azure Cosmos DB):** Captures failed routing decisions and transient timeouts.

## Relationships
* **Routing Controller -> Feature Flag Manager:** Queries active routing rules [In-process/Jedis]
* **Routing Controller -> ACL Mapper:** Transforms unrouted payloads [In-process]
* **Routing Controller -> Claims Core API:** Forwards migrated types [gRPC over HTTP/2]
* **Routing Controller -> Audit & Failover Logger:** Records routing telemetry and fallback events [gRPC/Queue]
* **Migration Router -> Integration Gateway & Sync Worker:** Mediates legacy mainframe requests [HTTPS/SOAP]

## Technology Stack
* **Azure Container Apps:** Runtime environment for high availability and scalability.
* **Spring Boot/Java:** Core framework for the routing controller providing robust enterprise capabilities.
* **MapStruct:** Efficient, compile-time object mapping for payload translation.
* **Redis:** In-memory caching for low-latency feature flag evaluations.
* **Azure Cosmos DB:** Scalable audit logging ensuring zero data loss during failovers.

## Rationale
This component architecture isolates the modern platform from legacy mainframe volatility while satisfying strict hybrid migration constraints. It ensures low-latency performance and sub-day rollback capabilities without modifying expensive mainframe interfaces.