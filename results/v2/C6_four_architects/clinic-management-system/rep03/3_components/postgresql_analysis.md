## Overview
The Clinic Management System is a hybrid cloud-based clinical IT platform designed to manage patient admissions, electronic medical records, scheduling, and billing for medium-sized hospitals and clinics. Its core purpose is to deliver secure, highly available, and interoperable healthcare operations meeting strict regulatory mandates.

## Key Elements
- Patients, Doctors, Administrators (People)
- Clinic Management System (Software System)
- Web Frontend, API Gateway, Core Microservices, Background Worker, Integration Service, Message Broker, PostgreSQL, Object Storage, Caching & Session Container, Audit & Compliance Logging, Backup & Archive Manager (Containers)
- PostgreSQL Primary Instance, PostgreSQL Standby Replica(s), PgBouncer, Row-Level Security (RLS) Policy Engine, Logical Replication / CDC Publisher, Backup Agent, Encryption Manager (Components)
- Identity Provider, Third-Party Billing Gateway, External Lab/Imaging Systems, Notification Gateway, Cloud Backup Archive (External Systems)

## Relationships
- Core Microservices -> Connection Pooler: Database queries [TCP / TLS]
- Connection Pooler -> PostgreSQL Primary Instance: Forwarded transactions [TCP / TLS]
- PostgreSQL Primary Instance -> PostgreSQL Standby Replica: Streaming replication [TCP / TLS]
- PostgreSQL Primary Instance -> Message Broker: Publishes table mutations [TCP / PostgreSQL Wire Protocol]
- Core Microservices -> RLS Policy Engine: Applies context-aware database queries [SQL / TLS]
- Backup Agent -> Cloud Backup Archive: Streams encrypted WAL archives and snapshots [HTTPS / S3 API]
- PostgreSQL Primary Instance -> Encryption Manager: Encrypts/decrypts sensitive fields [Internal C Extension / KMS API]

## Technology Stack
- PostgreSQL 15+: Relational data storage for EMR and scheduling with AES-256 encryption at rest.
- PgBouncer: Connection pooling and multiplexing to prevent resource exhaustion.
- pgcrypto / KMS Integration: Transparent data encryption and column-level hashing for sensitive data.
- React / TypeScript & NGINX: Frontend user interface delivery.
- Go & Spring Boot: High-performance core microservices.
- Apache Kafka / RabbitMQ: Event-driven asynchronous messaging.
- Apache Camel / Node.js: Interoperability and integration workflows.

## Rationale
This architecture uses active-active hybrid cloud patterns and high-availability replicas to guarantee 99.99% uptime. Row-Level Security, encryption management, and comprehensive auditing ensure strict compliance with HIPAA and GDPR mandates.