## Overview
The Core Domain Service is a Java/Spring Boot container that implements reliable business logic for cataloging and circulation within the Library Management System. It enforces clear bounded contexts while ensuring EU-only data residency and high performance.

## Key Elements
* **Catalog Management Component**: Spring MVC/Data component handling physical and digital items.
* **Circulation & Fines Component**: Manages loans, returns, and payment processing.
* **Event Publisher Component**: Spring AMQP component dispatching domain events.
* **Registry Integration Component**: Spring Cloud OpenFeign component synchronizing metadata.
* **Security Context & Auth Component**: Spring Security component validating tokens locally.

## Relationships
* **API Gateway -> Core Domain Service**: Routes client requests via gRPC and REST.
* **Core Domain Service -> PostgreSQL Database**: Reads and writes relational data using JDBC over TLS.
* **Core Domain Service -> RabbitMQ/Apache Kafka Message Broker**: Publishes domain events via AMQP.
* **Core Domain Service -> Payment Gateway**: Processes library fines via HTTPS.
* **Core Domain Service -> National Library Registry**: Synchronizes metadata via HTTPS/REST.
* **Core Domain Service -> Identity Provider**: Authenticates users using OIDC.

## Technology Stack
* **Java / Spring Boot**: Foundation for robust business logic execution.
* **Spring Modulith**: Enforces package-level boundaries between internal components.
* **Spring Security / OIDC**: Validates JWT tokens locally to minimize latency.
* **Spring Cloud OpenFeign**: Facilitates reliable inter-service REST communication.
* **Spring AMQP**: Handles asynchronous event publishing to message brokers.

## Rationale
Decomposing the container with Spring Modulith isolates domain logic and prevents circular dependencies while maintaining strict EU data boundaries in PostgreSQL. Local JWT validation via Spring Security ensures search and transaction responses remain fast to meet performance constraints.