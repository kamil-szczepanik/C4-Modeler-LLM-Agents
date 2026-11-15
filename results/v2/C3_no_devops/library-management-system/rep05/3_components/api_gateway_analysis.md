## Overview
The Library Management System provides cataloging, circulation, and self-service portals for public and academic libraries. The architecture enforces EU-only data residency while maintaining high-performance search and scalable operations.

## Key Elements
* Library Patrons, Librarians / Circulation Staff, Library Administrators
* Web Application (React, TypeScript, Nginx)
* API Gateway (Spring Cloud Gateway, Java)
* Response Cache (Redis, in-memory data store, EU-hosted)
* Audit Publisher (Spring Cloud Sleuth / Micrometer, Java)
* Core Services Container (Spring Boot, Java)
* Search Container (Elasticsearch / OpenSearch)
* Message Broker (Apache Kafka / RabbitMQ)
* PostgreSQL (AWS RDS EU)
* External Systems: Stripe EU, Keycloak/Auth0 EU tenant, SendGrid EU

## Relationships
* Web Application -> API Gateway: Sends API requests [HTTPS (REST/GraphQL, TLS 1.3)]
* API Gateway -> Response Cache: Reads/Writes cached search payloads [In-memory RESP protocol over TLS]
* API Gateway -> Core Services Container: Routes traffic to core business logic [gRPC/HTTPS using mTLS]
* API Gateway -> Search Container: Routes search queries [gRPC/HTTPS using mTLS]
* API Gateway -> Message Broker: Emits asynchronous telemetry and request logs [AMQP/Kafka Protocol over TLS]

## Technology Stack
* Spring Cloud Gateway: Chosen for robust routing, edge security, and ecosystem integration
* Redis: Selected for low-latency response caching and Token Bucket rate limiting
* Spring Boot & Java: Provides reliable core services and gateway components
* Elasticsearch / OpenSearch: Delivers sub-800ms search performance for catalog queries
* Apache Kafka / RabbitMQ: Enables asynchronous audit logging and metrics emission without latency penalty
* PostgreSQL (AWS RDS EU): Ensures relational data storage within strict EU-only constraints

## Rationale
This architecture guarantees sub-800ms search responses through edge caching and optimized routing. It strictly enforces EU data residency and robust edge security using localized components and encrypted protocols.