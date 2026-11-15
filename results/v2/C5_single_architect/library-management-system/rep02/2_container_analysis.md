## Overview
The Library Management System provides cataloguing, circulation, and self-service portals for public and academic libraries. It is architected to strictly enforce EU data residency and sub-800ms search performance.

## Key Elements
* Library Patrons and Library Staff (Users)
* Web Application (React/TypeScript SPA)
* API Gateway (Nginx / Spring Cloud Gateway)
* Core Domain Service (Java/Spring Boot)
* Search Service (Java with Elasticsearch)
* Notification Worker (Node.js)
* Database (PostgreSQL)
* Message Broker (RabbitMQ / Apache Kafka)
* External Systems: Payment Gateway, Notification Service, National Library Registry, Identity Provider

## Relationships
* Web Application calls API Gateway via HTTPS/REST
* API Gateway routes to Core Domain Service and Search Service via gRPC/REST over internal Docker networks
* Core Domain Service reads/writes to PostgreSQL via JDBC over TLS
* Core Domain Service publishes domain events to Message Broker via AMQP
* Notification Worker consumes events from Message Broker via AMQP and calls external Notification Service via HTTPS

## Technology Stack
* React/TypeScript: Powers the user-facing Single Page Application via CDN
* Java/Spring Boot: Implements reliable business logic for the Core Domain Service
* Elasticsearch: Powers high-performance catalog searches
* PostgreSQL: Stores relational data, pinned strictly to an EU region for compliance
* RabbitMQ/Apache Kafka: Handles asynchronous event-driven messaging via AMQP
* Nginx / Spring Cloud Gateway: Manages edge routing, TLS termination, and rate limiting

## Rationale
Isolating the Elasticsearch-backed Search Service guarantees the strict <800ms search performance requirement without degrading transactional database performance. Pinning PostgreSQL to an EU region strictly satisfies the mandatory EU-only data residency constraint.