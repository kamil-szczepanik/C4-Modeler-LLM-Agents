## Overview
The Clinic Management System is a hybrid cloud platform designed to manage patient registration, EMRs, scheduling, and billing for medium-sized hospitals and clinics. It ensures HIPAA and GDPR compliance, 99.99% availability, and strict data retention requirements.

## Key Elements
- **API Gateway:** Nginx / Envoy handling entry routing, TLS termination, and rate limiting.
- **Identity & Access Management:** Keycloak / OAuth2 Proxy for MFA and RBAC.
- **Core Services:** Spring Boot / Java microservices (Patient & Scheduling, EMR with audit trails, and Billing).
- **Integration Service:** Node.js / Apache Camel handling HL7 FHIR transformations.
- **Message Broker:** Kafka / RabbitMQ with Dead Letter Queues (DLQ) for asynchronous billing retries.
- **Data Tier:** Regional active-passive PostgreSQL database with column-level AES-256 encryption.
- **Storage:** WORM object storage tier for 10-year audit log retention.

## Relationships
- **Clients to API Gateway:** HTTPS / gRPC over TLS.
- **API Gateway to Core/Integration Services:** gRPC over mTLS.
- **Core Services to Data Tier:** SQL over encrypted connections.
- **Core/Billing Services to Message Broker:** AMQP / Kafka with client-side envelope encryption over mTLS.
- **Integration Service to External Systems:** HL7 FHIR APIs over HTTPS.

## Technology Stack
- **Spring Boot / Java:** Selected for robust enterprise Core Service development.
- **Node.js / Apache Camel:** Chosen for rapid HL7 FHIR transformation capabilities.
- **PostgreSQL:** Utilized for reliable transactional data integrity with active-passive regional patterns.
- **Kafka / RabbitMQ:** Deployed for asynchronous event-driven messaging and billing fault-tolerance.
- **Nginx / Envoy:** Implemented for performant edge routing and security enforcement.

## Rationale
This architecture uses containerized microservices and regional active-passive databases to prevent cross-region WAN latency spikes, safeguarding sub-second EMR load times and 99.99% availability. Strict network segmentation, client-side message encryption, and WORM storage ensure end-to-end HIPAA and GDPR compliance.