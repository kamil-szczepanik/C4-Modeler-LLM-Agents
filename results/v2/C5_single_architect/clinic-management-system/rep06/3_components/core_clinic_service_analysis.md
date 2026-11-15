## Overview
The Clinic Management System is a hybrid cloud clinical IT platform designed to manage patient admissions, electronic medical records (EMR), scheduling, and billing. It provides high availability (99.99%) and strict HIPAA/GDPR compliance for medium-sized hospitals and clinics.

## Key Elements
- **Users**: Patient / User, Clinician / Staff, Hospital Administrator
- **External Systems**: External Lab & Imaging Systems, Insurance Payment Gateways, Identity Provider (IdP), SMS / Notification Gateway, Regulatory Compliance / Auditing Authority
- **Containers**: API Gateway (NGINX / Envoy), Web Application (React / TypeScript), Core Clinic Service (Java / Spring Boot), Scheduling Service (Go), Billing Service (Node.js), Integration Service (Apache Camel / Spring Integration), Event Broker (Apache Kafka / RabbitMQ), PostgreSQL Database (PostgreSQL with AES-256), Redis Cache (Redis)
- **Core Clinic Service Components**: PatientController (Spring MVC), ClinicalRecordManager (Spring Service), DataAccessor (Spring Data JPA / Hibernate), EncryptionEngine (Spring Component)

## Relationships
- API Gateway -> Core Clinic Service: Routes requests [gRPC over mTLS]
- Core Clinic Service -> Event Broker: Publishes asynchronous domain events [AMQP / Kafka protocol]
- Core Clinic Service -> PostgreSQL Database: Reads and writes transactional data [JDBC / SQL over TLS]
- PatientController -> ClinicalRecordManager: Method calls [In-process]
- ClinicalRecordManager -> EncryptionEngine: Encrypts/decrypts PHI payloads [In-process]
- ClinicalRecordManager -> DataAccessor: Transactions [JDBC over TLS]
- ClinicalRecordManager -> Event Broker: Publishes EMRUpdatedEvent [Kafka Producer, AMQP]

## Technology Stack
- Java / Spring Boot: Core business logic implementation for high performance and maintainability.
- Spring Data JPA with Hibernate: Provides robust dirty tracking and `@EntityListeners` for immutable EMR audit trails.
- Google Tink Cryptographic Library: Handles transparent envelope encryption (AES-256) for PHI.
- Apache Kafka / RabbitMQ: Asynchronous messaging for high-availability event distribution.
- PostgreSQL: Relational persistence with AES-256 data at rest.

## Rationale
This architecture uses a hybrid cloud infrastructure with active-active high availability to meet the stringent 99.99% uptime requirement. Component-level cryptographic controls and immutable audit trails ensure full HIPAA and GDPR compliance for sensitive medical data.