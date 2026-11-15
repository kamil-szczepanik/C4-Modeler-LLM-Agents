## Overview
The EMR Service manages electronic medical records, clinical notes, and audit trails for the Clinic Management System. It ensures high-performance clinical data access while enforcing strict healthcare compliance and interoperability standards.

## Key Elements
- EMR Controller Layer: Spring MVC REST Controllers handling incoming clinical HTTPS requests.
- Clinical Record Manager: Core domain service managing patient charts, progress notes, and diagnostics.
- Audit Trail Interceptor: AOP component capturing immutable access logs asynchronously.
- Encryption & Data Access Layer: Spring Data JPA with Hibernate utilizing column-level AES-256 encryption.
- FHIR Transformer Component: Mapping engine converting internal models to HL7 FHIR resources.

## Relationships
- EMR Controller -> Clinical Record Manager [In-process method call]
- Clinical Record Manager -> Encryption & Data Access Layer [In-process JPA / PostgreSQL protocol]
- Clinical Record Manager -> FHIR Transformer Component [In-process method call]
- Audit Trail Interceptor -> Message Broker [AMQP / Kafka, async]
- FHIR Transformer Component -> Database Cluster [Read-only queries via JPA]

## Technology Stack
- Java / Spring Boot: Chosen for enterprise maturity and robust ecosystem support.
- Spring Data JPA / Hibernate: Provides reliable ORM mapping and database interaction.
- Spring MVC: Facilitates structured REST API development over HTTPS.
- Apache Camel / Node.js: Powers the integration broker for HL7 FHIR workflows.
- RabbitMQ / Kafka: Enables asynchronous, decoupled audit event publishing.

## Rationale
This architecture achieves sub-second P95 response times by decoupling heavy database transactions from asynchronous audit logging. It guarantees HIPAA and GDPR compliance through built-in encryption and immutable AOP audit trails.