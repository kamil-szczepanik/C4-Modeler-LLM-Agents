## Overview
[The Library Management System provides cataloging, circulation, and self-service portals for public and academic libraries. It enforces strict EU-only data residency and sub-800ms search performance.]

## Key Elements
- Catalog Management, Circulation, and User Portals microservices
- Isolated Microservice Databases (Relational/NoSQL)
- Redis Distributed Cache Container
- Elasticsearch / OpenSearch Search Container
- Asynchronous Message Broker (RabbitMQ / Kafka)
- Centralized Configuration Store (Consul / Spring Cloud Config)
- Log/Metrics Collector Agent (OTel Collector / Fluentd)

## Relationships
- Catalog Management -> Isolated Microservice Databases: Reads and writes data [SQL/TCP]
- Circulation -> Isolated Microservice Databases: Reads and writes data [SQL/TCP]
- User Portals -> Isolated Microservice Databases: Reads and writes data [SQL/TCP]
- Microservices -> Elasticsearch / OpenSearch: Executes search queries [HTTP/JSON]
- Microservices -> Redis: Caches read-heavy queries [RESP/TCP]
- Microservices -> Message Broker: Publishes/subscribes events [AMQP/TCP]

## Technology Stack
- Spring Boot: Core microservice framework for business logic containers
- Flyway / Liquibase: Automated schema migration and validation tools
- Resilience4j: Connection pooling and circuit-breaking strategy
- Testcontainers: Local development and integration testing
- OpenTelemetry / Fluentd: Telemetry and health-check monitoring

## Rationale
[Database-per-service isolation with strict zero-shared credentials ensures absolute compliance with EU data residency constraints. Application-level query timeouts and caching protect the strict 99th-percentile search response time under 800 ms.]