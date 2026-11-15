## Overview
The Clinic Management System manages patient admissions, medical records, scheduling, and billing for healthcare facilities. The architecture ensures high availability, strict HIPAA/GDPR compliance, and seamless interoperability.

## Key Elements
- Patient Controller (Java / Spring MVC)
- Scheduling Controller (Java / Spring MVC)
- Appointment Engine (Java / Core Domain Component)
- Data Access Repository (Spring Data JPA)
- Event Publisher (Spring Kafka Template)
- Scheduling Cache Manager (Spring Data Redis)
- Audit Interceptor (Spring AOP)
- Outbox Event Handler (Transactional Outbox Pattern)
- FHIR Translation Adapter (HL7 FHIR Mapper)

## Relationships
- Patient Controller & Appointment Controller -> Audit Interceptor: Triggers audit events [In-Process / AOP]
- Appointment Engine -> Scheduling Cache Manager: Checks slot lock status [In-Process]
- Scheduling Cache Manager -> Distributed Cache: Reads/writes ephemeral availability locks [TCP]
- Appointment Engine -> Data Access Repository: Queries availability [In-Process]
- Event Publisher -> Outbox Event Handler: Commits events to transaction boundary [In-Process]
- Event Publisher -> Message Broker: Dispatches domain events [SASL/SCRAM over TLS]
- FHIR Translation Adapter -> Event Publisher: Dispatches standardized FHIR resources [In-Process]

## Technology Stack
- Java / Spring Boot: Core container runtime for enterprise reliability
- PostgreSQL: Primary relational database for ACID compliance
- Redis Enterprise: Distributed cache for fast pre-checks and locking
- Apache Kafka: Message broker for reliable asynchronous event streaming
- Spring AOP & JPA: Framework features for auditing and transactional outbox pattern

## Rationale
This component architecture implements a modular monolith pattern inside the Spring Boot container, ensuring clean separation of concerns and testability. Distributed locking and the transactional outbox pattern guarantee high availability (99.99%) and data integrity across active-active replicas.