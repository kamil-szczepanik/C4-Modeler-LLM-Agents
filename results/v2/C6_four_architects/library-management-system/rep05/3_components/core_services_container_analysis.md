## Overview
The Library Management System provides cataloguing, circulation, and self-service portals for public and academic libraries within an EU-only data residency constraint. The core services container utilizes a modular Spring Boot architecture to deliver scalable business logic.

## Key Elements
* Catalogue Management Component (Spring Bean / Java)
* Circulation Engine Component (Spring Bean / Java)
* Search Orchestrator Component (Spring Bean / Java)
* Authentication/Authorization Component (Spring Security / Java)
* Notification & Event Dispatcher Component (Spring Event / Java)
* Transaction & Audit Component (Spring `@Transactional` / Java)
* External Containers: PostgreSQL RDS, Elasticsearch Cluster, Managed RabbitMQ, AWS Redis, AWS S3

## Relationships
* Search Orchestrator Component -> Search Container: Executes high-performance queries [REST over TLS]
* Circulation Engine Component -> Message Broker: Publishes domain events [AMQP/TLS]
* Transaction & Audit Component -> Database: Commits atomic operations [JDBC over TLS]
* Circulation Engine Component -> Cache / Session Store: Manages transient states [RESP over TLS]
* Internal Components: Communicate via [In-process Method Calls]

## Technology Stack
* Java & Spring Boot: Provides robust enterprise framework for core services
* Elasticsearch: Delivers high-performance sub-800ms search capabilities
* PostgreSQL (RDS): Ensures ACID compliance for transactional data
* RabbitMQ & Redis: Handle asynchronous messaging and session caching

## Rationale
This modular component structure isolates business logic and guarantees ACID compliance for circulation workflows. Offloading complex queries to Elasticsearch ensures the 99th-percentile search response remains under 800ms while strictly enforcing EU data residency.