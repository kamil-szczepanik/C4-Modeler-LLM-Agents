## Overview
The Library Management System provides cataloging, circulation, and self-service portals for academic and public libraries. It ensures EU-only data residency and maintains a 99th-percentile search response under 800 ms.

## Key Elements
- Users: Client / User Agent
- External Systems: Identity Provider (IdP), Notification Service, Monitoring Aggregator, Disaster Recovery Target
- Containers: Web Frontend, Mobile App, API Gateway (Envoy/NGINX), Data Routing Proxy, Catalog Management, Circulation, User Portals, Elasticsearch/OpenSearch, Redis, Isolated Microservice Databases, Asynchronous Message Broker (RabbitMQ/Kafka), Consul / Spring Cloud Config, OTel Collector
- Component: Catalog Management (Spring Boot)

## Relationships
- API Gateway Container -> Catalog Management: Routes traffic [gRPC/REST]
- Catalog Management -> Redis Distributed Cache Container: Queries cache [TCP]
- Catalog Management -> Elasticsearch / OpenSearch Search Container: Queries search index [TCP]
- Catalog Management -> Isolated Microservice Databases: Reads and writes data [SQL/TCP]
- Catalog Management -> Asynchronous Message Broker Container: Publishes/consumes events [AMQP/TCP]

## Technology Stack
- Spring Boot: Enterprise patterns, data access, and messaging abstractions for Catalog Management
- Redis: Cache-Aside pattern for low-latency queries
- Elasticsearch / OpenSearch: High-performance item catalog search
- RabbitMQ / Kafka: Asynchronous event-driven decoupling for writes
- Flyway / Liquibase: Automated database schema versioning
- Spring Boot Actuator: Liveness and readiness health check probes

## Rationale
This architecture uses caching, asynchronous messaging, and bulkhead isolation to meet strict search performance SLAs (<800 ms). EU-hosted infrastructure and isolated databases guarantee data residency and integrity constraints.