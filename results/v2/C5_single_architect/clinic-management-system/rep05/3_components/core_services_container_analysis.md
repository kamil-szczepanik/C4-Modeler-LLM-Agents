## Overview
The Core Services Container manages patient admissions, scheduling, clinical operations, and interoperability for the Clinic Management System. It provides high-availability, secure, and standards-compliant clinical workflows across hybrid environments.

## Key Elements
- Patient Management Component (Spring MVC / Data)
- Scheduling Engine Component (Spring Service)
- Event Publisher Component (Spring Cloud Stream / Kafka)
- FHIR Interoperability Component (Spring WebFlux)
- Security & Audit Interceptor Component (Spring AOP / Security)

## Relationships
- API Gateway -> Patient Management & Scheduling Engine: Routes internal requests [gRPC over TLS]
- API Gateway -> FHIR Interoperability Component: Routes external requests [REST/HTTPS]
- Patient Management & Scheduling Engine -> PostgreSQL Primary DB: Reads and writes data [JDBC over TLS]
- Event Publisher -> Async Message Broker: Publishes domain events [Kafka Protocol]
- Security & Audit Interceptor -> EMR & Audit Service: Streams audit trails [Kafka Protocol]

## Technology Stack
- Java Spring Boot: Selected for robust enterprise capabilities and microservices support.
- Spring Cloud Stream & Apache Kafka: Chosen for reliable, asynchronous event-driven messaging.
- Spring WebFlux: Utilized for non-blocking reactive HL7 FHIR API integration.
- Spring AOP & Security: Implemented for centralized access control and compliance auditing.
- JDBC over TLS: Ensures secure, encrypted database communication.

## Rationale
This component architecture meets strict HIPAA and GDPR compliance mandates through integrated security interceptors and immutable audit streaming. It guarantees high availability and sub-second performance using reactive components and gRPC communication over secure TLS channels.