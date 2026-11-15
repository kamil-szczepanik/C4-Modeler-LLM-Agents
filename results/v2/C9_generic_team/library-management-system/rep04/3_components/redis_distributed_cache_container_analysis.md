## Overview
The Library Management System is a solution for public and academic libraries to catalogue items, manage circulation, and provide self-service portals. It utilizes a Redis distributed cache container to absorb read spikes and manage session data while enforcing EU data residency.

## Key Elements
* Redis Distributed Cache Container (Redis)
* Catalog Management Service (Spring Boot)
* Circulation Service (Spring Boot)
* User Portals Service (Spring Boot)
* Asynchronous Message Broker Container (RabbitMQ / Kafka)
* Isolated Microservice Databases

## Relationships
* Catalog Management -> Redis Distributed Cache Container: Queries cache [TCP]
* Circulation -> Redis Distributed Cache Container: Queries cache [TCP]
* User Portals -> Redis Distributed Cache Container: Queries cache [TCP]
* Asynchronous Message Broker Container -> Catalog Management/Circulation/User Portals: Pub/sub cache invalidation events [TCP]

## Technology Stack
* Redis: Distributed caching and session management to meet <800ms search latency (R-05)
* Spring Boot: Microservice application layer with circuit-breaker and connection pooling configurations
* RabbitMQ / Kafka: Event-driven cache-busting and invalidation messaging

## Rationale
This architecture offloads read-heavy queries from primary databases to meet strict 99th-percentile search response times under 800ms. It isolates session data and high-throughput caching while strictly adhering to EU-only data residency constraints.