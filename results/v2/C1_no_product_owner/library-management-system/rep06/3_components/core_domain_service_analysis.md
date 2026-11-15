## Overview
The Library Management System is a comprehensive solution for public and academic libraries to catalogue physical and digital items, manage circulation, and provide self-service portals. It enforces EU-only data residency requirements.

## Key Elements
- **Users:** Library Patron, Librarian / Library Staff
- **External Systems:** Payment Gateway, Digital Content Provider
- **Containers:** Web Application, API Gateway, Core Domain Service, Search Service, Managed Kafka Event Bus, PostgreSQL Database
- **Core Domain Service Components:** CatalogManager, CatalogQueryFacade, CirculationEngine, DomainEventPublisher

## Relationships
- API Gateway -> Core Domain Service: Routes requests via gRPC/REST with mTLS
- Core Domain Service -> PostgreSQL Database: Persists data via JDBC with AES-256 encryption and jOOQ read-optimized queries
- Core Domain Service -> Managed Kafka: Publishes domain events using the Kafka protocol with payload encryption
- CirculationEngine -> Payment Gateway: Processes transactions via REST/HTTPS with mTLS and Resilience4j circuit breakers

## Technology Stack
- **Backend Framework:** Spring Boot / Java for the Core Domain Service
- **Database Layer:** PostgreSQL with Spring Data JPA and jOOQ for query optimization
- **Event Streaming:** Managed Kafka with SASL/SCRAM or mTLS authentication
- **Resilience & Security:** Resilience4j for circuit breaking, Spring Security with OAuth2/OIDC JWT validation, and OpenTelemetry for observability

## Rationale
This architecture uses a stateless Spring Boot container and read-optimized jOOQ queries to consistently meet the strict <800ms search performance requirement. It guarantees EU-only data residency and regulatory compliance through AES-256 storage, mTLS transport encryption, and strict PII tokenization.