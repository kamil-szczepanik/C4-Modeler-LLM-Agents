## Overview
The Patient Management Microservice handles patient admissions and demographic capture within the Clinic Management System. It ensures HIPAA and GDPR compliance, high availability, and high-performance data access.

## Key Elements
- Clinic Staff and Patients (Users)
- API Gateway (Edge Routing, OAuth2/OIDC)
- Patient Management Microservice (Containers/Components: PatientController, PatientService, PatientRepository, PatientCacheManager, AuditLogger)
- PostgreSQL Database
- Redis Cache
- Elasticsearch Audit Trail
- Apache Kafka (Messaging Backbone)
- HL7 FHIR Integration Container (Apache Camel)

## Relationships
- API Gateway -> Patient Management Microservice: Routes requests [gRPC, mTLS]
- PatientController -> PatientService: Delegates requests [In-memory method calls]
- PatientService -> PatientRepository: Executes queries [Hibernate/JPA, JDBC over TLS 1.3]
- PatientService -> PatientCacheManager: Manages cache [Lettuce drivers]
- PatientService -> Messaging Backbone: Publishes domain events [Apache Kafka, JSON, TCP]
- AuditLogger -> Elasticsearch Audit Trail: Emits audit logs [HTTP/S]

## Technology Stack
- Java 21 with Spring Boot 3: Chosen for robust enterprise standards, dependency injection, and native security auditing.
- Spring Data JPA & Hibernate: Provides type-safe database access and isolation of business logic from persistence.
- Jakarta Validation: Enforces strict input sanitization for HIPAA and GDPR data compliance.
- Redis & Lettuce Drivers: Enables fast in-memory caching to meet sub-second P95 performance constraints.
- Apache Kafka: Facilitates asynchronous, decoupled event-driven architecture across microservices.
- PostgreSQL & Elasticsearch: Secures data at rest via AES-256 and maintains immutable audit trails.

## Rationale
This architecture isolates domain logic, leverages caching to meet strict performance requirements, and enforces encryption and auditing to satisfy healthcare compliance mandates. Asynchronous messaging via Kafka ensures high availability and scalability across hybrid cloud environments.