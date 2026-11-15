## Overview
The Library Management System provides cataloging, circulation, and self-service portals for public and academic libraries. It prioritizes EU-only data residency and sub-800ms search response performance.

## Key Elements
- **Redis Container**: In-memory data store residing in the private backend VPC.
- **Session Management Component**: Handles user session states.
- **Catalog Read-Through Cache Component**: Stores frequently accessed bibliographic records.
- **Rate Limiter Component**: Backs API Gateway traffic throttling.
- **Connected Systems**: Web Application (React, TypeScript), API Gateway (Spring Cloud Gateway / Envoy), Catalogue Service (Java, Spring Boot).

## Relationships
- **Web Application -> API Gateway**: Routes client requests securely via HTTPS.
- **API Gateway -> Redis (Rate Limiter Component)**: Throttles traffic using RESP3 over TCP with TLS.
- **Catalogue Service -> Redis (Catalog Read-Through Cache Component)**: Caches frequent reads using RESP3 over TCP with TLS.

## Technology Stack
- **Redis OSS / Enterprise**: In-memory data store chosen for low-latency, high-throughput caching.
- **RESP3 over TCP with TLS**: Protocol used for secure, multiplexed communication strictly within the private backend network.

## Rationale
Routing all Redis access exclusively through backend services rather than the frontend Web Application mitigates security and data leakage risks. This architecture satisfies the EU data residency constraint while supporting high-performance requirements.