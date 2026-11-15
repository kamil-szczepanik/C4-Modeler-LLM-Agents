## Overview
- Decomposes the Catalog & Search Service for the Library Management System into specialized internal components to deliver sub-800ms search responses and secure cataloging.
- Enforces strict EU-only data residency and role-based access control for all physical and digital inventory operations.

## Key Elements
- Search Query Engine [component] (Java, Spring Data Elasticsearch)
- Catalog Management API [component] (Java, Spring MVC)
- Index Synchronization Worker [component] (Java, Spring Integration)
- Elasticsearch Index [component] (Elasticsearch)
- Database [container] (PostgreSQL)
- API Gateway [container] (NGINX / Envoy)
- Message Broker [container] (Apache Kafka / RabbitMQ)
- Audit Service [container] (Go)

## Relationships
- API Gateway -> Search Query Engine [gRPC over mTLS]
- API Gateway -> Catalog Management API [gRPC over mTLS]
- Search Query Engine -> Elasticsearch Index [Internal Java API / Transport over mTLS]
- Catalog Management API -> Database [SQL over mTLS]
- Index Synchronization Worker -> Message Broker [AMQP/Kafka Protocol over mTLS]
- Index Synchronization Worker -> Database [SQL over mTLS]
- Catalog Management API -> Audit Service [REST over mTLS]

## Technology Stack
- Java & Spring Boot: Core framework for high-performance microservices and component decomposition.
- Elasticsearch: High-speed search engine ensuring 99th-percentile search responses under 800ms.
- PostgreSQL: Relational database providing ACID-compliant transactional persistence.
- Apache Kafka / RabbitMQ: Asynchronous message broker for event-driven index synchronization.
- gRPC & mTLS: Secure, low-latency inter-service communication protocol with mutual TLS authentication.

## Rationale
- Separating the Search Query Engine from the Catalog Management API prevents high-volume patron searches from degrading critical librarian updates.
- Implementing an event-driven Index Synchronization Worker alongside encrypted EU-hosted infrastructure ensures strict data residency, audit compliance, and sub-800ms performance SLAs.