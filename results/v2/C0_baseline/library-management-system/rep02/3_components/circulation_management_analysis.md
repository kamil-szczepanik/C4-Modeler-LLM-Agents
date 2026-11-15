## Overview
The Library Management System is a solution for public and academic libraries to catalogue items, manage circulation, and provide self-service portals, adhering strictly to EU-only data residency constraints.

## Key Elements
- Circulation Management (Backend Service Container)
- Checkout Engine Component (Spring Boot / Java)
- Patron Account Manager Component (Spring Boot / Java)
- Circulation Data Access Component (JPA / PostgreSQL 15)
- Event Publisher Component (Spring Cloud Stream / Kafka)
- Self-Service Portal & Staff Management Console (React / Nginx)
- API Gateway (Kong / Envoy)

## Relationships
- Self-Service Portal to Checkout Engine via HTTPS/REST
- Staff Management Console to Patron Account Manager via HTTPS/REST
- Event Publisher to Kafka via TCP for asynchronous audit and notifications
- Checkout Engine and Patron Account Manager to Circulation Data Access via internal package-private boundaries

## Technology Stack
- Java 17 & Spring Boot 3: Selected for robust enterprise backend development and microservices compatibility
- PostgreSQL 15: Provides relational state storage with required EU-region data residency enforcement
- Apache Kafka: Enables decoupled asynchronous messaging and audit event publishing
- Spring Cloud Stream: Manages event publishing boundaries and prevents blocking transactions
- OpenTelemetry: Provides distributed tracing for performance monitoring

## Rationale
This component architecture separates self-service checkout workflows from administrative exception handling while enforcing strict EU data residency and RBAC security. Asynchronous event publishing and circuit breakers ensure high availability and prevent downstream failures during peak circulation rushes.