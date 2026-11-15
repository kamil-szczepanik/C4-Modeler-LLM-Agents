## Overview
[The Clinic Management System is a hybrid clinical IT solution designed to manage patient admissions, electronic medical records (EMR), scheduling, and billing for medium-sized hospitals and clinics. Its core purpose is to streamline clinical workflows while ensuring high availability, sub-second performance, and strict HIPAA and GDPR compliance.]

## Key Elements
- Patients, Receptionists, Clinicians, Billing Specialists
- Core Services (Spring Boot / Java container)
- Patient Administration Component
- Scheduling Engine
- EMR Manager
- Workflow Orchestrator (Temporal Java SDK)
- Data Tier: PostgreSQL with Citus, Redis, Kafka/RabbitMQ
- Infrastructure & Security: Istio, Centralized Vault

## Relationships
- Web Application -> Core Services: gRPC over mTLS (Istio)
- Scheduling Engine -> Redis: Redlock algorithm over TLS for distributed resource locking
- EMR Manager -> PostgreSQL (Citus): JDBC / Spring Data JPA with HikariCP over TLS
- Core Services -> Kafka/RabbitMQ: Asynchronous domain mutation events using Spring Cloud Stream with payload-level envelope encryption
- Core Services -> Centralized Vault: Dynamic secret fetching via AppRole tokens and Spring Cloud Vault

## Technology Stack
- Spring Boot / Java: Chosen for robust enterprise backend services and ecosystem support
- PostgreSQL with Citus: Selected for scalable, distributed relational data storage supporting 10-year retention
- Redis: Utilized for distributed locking and low-latency scheduling clash checks
- Temporal (Java SDK): Implemented for managing complex multi-resource scheduling sagas
- Kafka/RabbitMQ: Deployed for reliable asynchronous event streaming and audit logging
- Istio: Used for Zero-Trust service-to-service mTLS and SPIFFE/SPIRE workload identity

## Rationale
[This architecture achieves 99.99% availability and sub-second P95 performance through local active-active clustering, Redis locking, and connection pooling while avoiding cross-region synchronous bottlenecks. It enforces strict HIPAA and GDPR compliance via end-to-end encryption, cryptographic audit trails, and zero-trust mTLS across the hybrid infrastructure.]