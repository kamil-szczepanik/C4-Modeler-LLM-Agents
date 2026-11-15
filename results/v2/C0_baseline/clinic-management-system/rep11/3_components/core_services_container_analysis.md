## Overview
The Clinic Management System is a hybrid cloud platform designed for medium-sized hospitals and clinics to manage patient admissions, electronic medical records, scheduling, and billing. It provides high availability, stringent security compliance, and high-performance clinical workflows.

## Key Elements
- **API Gateway**: Nginx / Envoy handling entry routing and mTLS.
- **Core Services Container**: Java / Spring Boot modular monolith containing Patient Management, Scheduling, EMR Core, and Billing components.
- **Databases & Caching**: PostgreSQL (OLTP with AES-256), ClickHouse (OLAP), and Redis for caching and locks.
- **Messaging**: Apache Kafka for asynchronous domain events.
- **Security & Infrastructure**: HashiCorp Vault sidecar, Istio service mesh, and Spring Security with RBAC.

## Relationships
- **API Gateway -> Core Services Container**: Routes authenticated requests via mTLS [Istio service mesh].
- **Core Services Container -> PostgreSQL**: Reads and writes transactional clinical data [JDBC / SQL].
- **Core Services Container -> Redis**: Manages scheduling locks, caching, and state [Redis Protocol with AES-256].
- **Core Services Container -> Apache Kafka**: Publishes asynchronous domain events and insurance claims [Kafka Protocol].

## Technology Stack
- **Java / Spring Boot**: Chosen for enterprise maturity, strong dependency injection, and modular architecture.
- **PostgreSQL & Redis**: Selected for robust transactional ACID guarantees and sub-millisecond caching performance.
- **Apache Kafka**: Implemented for reliable asynchronous event streaming and dead-letter queue handling.
- **HashiCorp Vault & Istio**: Deployed for secure secret management and zero-trust hybrid network encryption.

## Rationale
This architecture meets HIPAA/GDPR constraints and 99.99% uptime requirements through encrypted multi-region deployment and robust circuit-breaking. The Spring Boot modular monolith design with Redis caching directly ensures EMR screen loads under 1 second P95.