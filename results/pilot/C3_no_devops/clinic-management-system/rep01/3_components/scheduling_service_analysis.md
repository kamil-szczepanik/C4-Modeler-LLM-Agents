## Overview
The Clinic Management System manages patient admissions, EMRs, scheduling, and billing for healthcare facilities. It ensures 99.99% availability, HIPAA/GDPR compliance, and 10-year data retention using a hybrid cloud architecture.

## Key Elements
- **Users**: Patients, Receptionists, Clinical Staff, Billing Specialists
- **External Systems**: External Labs/Imaging, Insurance Clearinghouses, Payment Gateways, Identity Provider
- **Containers**: API Gateway (Envoy/Kong), Patient Portal Service, Scheduling Service, EMR Service, Billing Service, HL7 FHIR Integration Service, Analytics Service, PostgreSQL Database, Apache Kafka, External Vault/HSM
- **Scheduling Service Components**: Appointment API Controller, Conflict Resolution Engine, Calendar Management Service, Notification Dispatcher, Waitlist Orchestrator

## Relationships
- API Gateway -> Scheduling Service: Routes scheduling requests [gRPC over mTLS]
- Scheduling Service -> PostgreSQL Database: Reads and writes scheduling data [TLS with AES-256 at rest]
- Scheduling Service -> Apache Kafka Message Broker: Publishes asynchronous events [Internal TLS]

## Technology Stack
- **Languages/Frameworks**: Java 17, Spring Boot, Spring Batch for microservices
- **Databases/Caching**: PostgreSQL Database, Redis Cluster for sub-millisecond slot validation
- **Messaging**: Apache Kafka with SCRAM-SHA-512 authentication and topic ACLs
- **Security**: OAuth2/JWT for RBAC, AES-256 encryption at rest, Vault/HSM

## Rationale
This hybrid architecture uses containerized microservices on Kubernetes and AWS to achieve high availability and active-active scaling. In-memory caching and gRPC ensure sub-second performance while robust encryption and audit trails satisfy HIPAA and GDPR mandates.