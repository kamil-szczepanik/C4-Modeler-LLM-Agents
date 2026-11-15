## Overview
The Patient & Scheduling Service is a NestJS-based microservice within the Clinic Management System that handles patient admissions, demographics, and appointment scheduling. It ensures secure, high-concurrency operations for medium-sized hospitals and clinics.

## Key Elements
- Patient Registration Controller & Service (NestJS component)
- Scheduling Engine & Resource Validator (NestJS component)
- Notification Dispatcher (NestJS component)
- Patient Consent & Privacy Manager (NestJS component)
- Database Cluster (PostgreSQL)
- Message Broker (Apache Kafka)
- In-Memory Cache (Redis)

## Relationships
- API Gateway -> Patient & Scheduling Service: Routes client requests [mTLS]
- Patient Registration Service -> Patient Consent & Privacy Manager: Validates consent metadata [Internal TypeScript Function Call]
- Patient Registration Service -> Database Cluster: Persists demographics [TypeORM / PostgreSQL protocol]
- Scheduling Engine -> Redis Cache: Performs slot-locking and clash checks [Redis Protocol]
- Scheduling Engine -> Database Cluster: Persists appointments and audit logs [TypeORM / PostgreSQL protocol]
- Scheduling Engine -> Message Broker: Emits `AppointmentBooked` events [Kafka protocol]

## Technology Stack
- NestJS / Node.js: Framework for building modular, high-performance TypeScript microservice components.
- PostgreSQL: Relational storage for encrypted patient and scheduling data ensuring durability.
- Redis: In-memory cache utilizing distributed locking (Redlock) for atomic appointment clash checks.
- Apache Kafka: Event broker for reliable asynchronous messaging and notifications.
- AES-256: Encryption standard for satisfying HIPAA and GDPR data security mandates.

## Rationale
This component architecture uses modular NestJS services and Redis distributed locking to achieve sub-second P95 performance and 99.99% availability during high-concurrency scheduling. Built-in consent management and field-level AES-256 encryption guarantee strict HIPAA and GDPR compliance.