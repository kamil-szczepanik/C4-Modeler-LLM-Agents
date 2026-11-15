## Overview
The Clinic Management System is a clinical IT solution designed to handle patient admissions, electronic medical records (EMR), scheduling, and billing for medium-sized hospitals. It ensures high availability, strict HIPAA/GDPR compliance, and robust interoperability via modern cloud-native patterns.

## Key Elements
- **API Gateway / BFF**: Kong / Node.js
- **EMR Service (Parent Container)**: Spring Boot / Java
- **EMR Controller**: Spring MVC / Spring WebFlux
- **Clinical Record Manager**: Spring Service / DDD
- **Audit Logger Component**: Spring AOP / SLF4J
- **EMR Data Access Repository**: Spring Data JPA / Hibernate
- **Clinical Cache Component**: Spring Cache / Redis Client
- **Databases & Messaging**: PostgreSQL (AES-256 at rest), Redis, Apache Kafka

## Relationships
- API Gateway / BFF -> EMR Service: Routes requests internally [gRPC]
- EMR Controller -> Clinical Record Manager: Invokes business logic [Java Method Calls]
- Clinical Record Manager -> Audit Logger Component: Dispatches audit events [Internal Event]
- Clinical Record Manager -> EMR Data Access Repository: Persists records [JDBC / SQL via TLS]
- Clinical Record Manager -> Clinical Cache Component: Checks/updates cache [Lettuce / In-memory]
- Clinical Cache Component -> Redis: Reads/writes cached data [Redis Protocol / TLS]
- EMR Service -> Apache Kafka: Publishes domain events [TLS]

## Technology Stack
- **Spring Boot / Java**: Powers the EMR Service for enterprise-grade reliability and performance.
- **Spring AOP**: Isolates compliance logging without cluttering core domain logic.
- **Spring Data JPA & PostgreSQL**: Ensures robust persistence with mandatory AES-256 encryption at rest.
- **Redis & Spring Cache**: Delivers sub-second EMR screen loads (<1s P95) via caching.
- **Apache Kafka**: Enables reliable asynchronous event-driven communication.

## Rationale
This architecture uses an isolated internal component structure within the EMR Service to satisfy strict HIPAA/GDPR audit trails and sub-second performance SLAs. The hybrid setup with caching and event streaming ensures 99.99% availability and high scalability.