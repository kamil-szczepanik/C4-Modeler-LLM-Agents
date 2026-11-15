## Overview
The Core Domain Service is a Java-based Spring Boot microservice responsible for managing business logic, cataloguing, and circulation within the Library Management System. It enforces domain rules while adhering to strict EU data residency constraints.

## Key Elements
- **Catalogue Management Component**: Spring `@Service` (Java) handling item cataloguing.
- **Circulation Engine Component**: Spring `@Service` (Java) managing loans and reservations.
- **Payment & Notification Facade**: Spring `@Component` (Java) handling external integrations.
- **Data Access Repository**: Spring Data JPA (Java) managing persistence.
- **Event Publisher Component**: Spring Cloud Stream / Kafka Template (Java) handling event dispatch.

## Relationships
- **Catalogue Management & Circulation Engine** -> **Data Access Repository**: Persists and queries data [JDBC / In-process method calls].
- **Circulation Engine** -> **Payment & Notification Facade**: Triggers payments and alerts [In-process method calls].
- **Catalogue Management & Circulation Engine** -> **Event Publisher Component**: Dispatches domain events [In-process method calls].
- **Event Publisher Component** -> **Async Event Broker**: Publishes events [TCP / Kafka Protocol].
- **Payment & Notification Facade** -> **Payment Gateway & Notification Provider**: Processes transactions and messages [HTTPS].

## Technology Stack
- **Java & Spring Boot**: Core runtime and framework for dependency injection and service structure.
- **Spring Data JPA & JDBC**: Persistence layer technology for interacting with PostgreSQL.
- **Spring Cloud Stream / Kafka Template**: Abstraction for publishing messages to Apache Kafka.
- **HTTPS**: Secure transport protocol for external gateway and provider communications.

## Rationale
This component-level architecture applies Domain-Driven Design principles to cleanly separate cataloguing, circulation, persistence, and event publishing within the Core Domain Service. It ensures modularity and maintainability while meeting performance and EU-only data residency requirements.