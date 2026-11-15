## Overview
The Search Service is a high-performance component of the Library Management System that provides fast catalog searches for library patrons and staff. It is designed to meet strict performance and EU data residency constraints.

## Key Elements
- Library Patrons and Library Staff (Users)
- API Gateway (Nginx / Spring Cloud Gateway)
- Search Service (Java with Elasticsearch container)
- API Controller (Spring MVC / Spring WebFlux)
- Query Sanitizer Component (In-memory Java)
- Search Orchestrator (Java Service Bean)
- Elasticsearch Repository (Spring Data Elasticsearch)
- Catalogue Sync Listener (Spring AMQP / Kafka Listener)
- Message Broker (RabbitMQ / Apache Kafka)

## Relationships
- API Gateway -> API Controller: Routes search requests [gRPC/REST]
- API Controller -> Query Sanitizer Component: Sanitizes inputs [In-memory Java Method Call]
- Query Sanitizer Component -> Search Orchestrator: Passes clean queries [In-memory Java Method Call]
- Search Orchestrator -> Elasticsearch Repository: Executes queries [Elasticsearch Java Client]
- Message Broker -> Catalogue Sync Listener: Consumes item events [AMQP/Kafka]

## Technology Stack
- Java / Spring Boot: Core component framework
- Elasticsearch: High-performance indexing and search engine
- Spring Data Elasticsearch: Repository data access layer
- Spring MVC / Spring WebFlux: Endpoint exposure
- Spring AMQP / Kafka Listener: Event ingestion

## Rationale
This architecture decouples ingestion from query paths to maintain high performance and meet the sub-800ms search latency requirement. It also integrates sanitization to ensure compliance with EU data residency rules.