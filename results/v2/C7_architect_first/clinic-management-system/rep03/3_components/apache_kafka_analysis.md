## Overview
The Clinic Management System is an enterprise clinical IT platform designed to securely manage patient admissions, electronic medical records (EMR), scheduling, and billing. It provides high-availability event-driven architecture to support medium-sized hospitals and clinics under strict regulatory compliance.

## Key Elements
- **Users**: Doctors, Nurses, Receptionists, Billing Staff, Clinic Administrators, Patients
- **External Systems**: Identity Provider (IdP), External Labs & Imaging Systems, Payment Gateway / Insurance Clearinghouse
- **Containers**: API Gateway (Nginx / Kong), Web Application (React / TypeScript, Nginx), Core Services (Node.js / NestJS or Java / Spring Boot), PostgreSQL, Redis, Apache Kafka, AWS S3 Object Lock
- **Kafka Components**: Kafka Brokers, KRaft Controller Quorum, Kafka Connect, Schema Registry, Kafka Stream Processors

## Relationships
- Core Services -> Kafka Brokers: Publishes and consumes asynchronous clinical events [Kafka Protocol / mTLS]
- Kafka Brokers -> AWS S3 Object Lock: Tiered storage and audit log archiving [HTTPS]
- Core Services -> Schema Registry: Validates event schemas [HTTP/REST / TLS]
- Kafka Brokers -> Schema Registry: Stores schema definitions [Kafka Protocol]

## Technology Stack
- **Message Broker**: Apache Kafka configured with `acks=all` and KRaft Mode for zero-data-loss event streaming and streamlined failovers.
- **Integration Framework**: Kafka Connect for exactly-once event syncing to PostgreSQL and AWS S3 Object Lock.
- **Schema Management**: Confluent Schema Registry enforcing Avro/Protobuf backward-compatibility rules.
- **Stream Processing**: Kafka Streams for real-time appointment clash checks and event aggregation.
- **Security & Compliance**: mTLS, SASL/OIDC (OAuth 2.0), ACLs, and AES-256 encryption at rest to satisfy HIPAA and GDPR mandates.

## Rationale
This architecture uses an event-driven Kafka backbone deployed via Strimzi to guarantee 99.99% availability and zero data loss for critical EMR workflows. Hybrid cloud design and strict security protocols ensure compliance with HIPAA, GDPR, and 10-year data retention requirements.