## Overview
- Manages patient admissions, electronic medical records, scheduling, and billing for medium-sized hospitals and clinics.
- Operates on a hybrid cloud infrastructure ensuring HIPAA/GDPR compliance and 99.99% high availability.

## Key Elements
- Core API Dispatcher (Go)
- Access Control & Policy Enforcement Component (Spring Boot)
- Patient Admissions Component (Go)
- Scheduling Component (Spring Boot)
- EMR Component (Spring Boot)
- Billing Component (Go)
- FHIR Interoperability Component (Go)
- Internal Event Dispatcher (Go)
- Data Encryption & Anonymization Component (Go)
- Database Repository Abstraction Layer (Go/Spring Data)

## Relationships
- API Gateway -> Core API Dispatcher: Routes validated requests [gRPC / mTLS]
- Core API Dispatcher -> Access Control & Policy Enforcement Component: Evaluates permissions [In-process method call / gRPC]
- Scheduling Component -> Caching & Session Container: Acquires distributed locks [Redis Protocol / TLS]
- EMR Component -> Audit & Compliance Logging: Dispatches audit events [gRPC]
- FHIR Interoperability Component -> Integration Service: Transmits standardized health records [gRPC / mTLS]
- Internal Event Dispatcher -> Message Broker: Publishes domain events [AMQP / TLS]
- Data Encryption & Anonymization Component -> PostgreSQL: Persists encrypted clinical data [SQL / TLS]

## Technology Stack
- Go: Used for Admissions, Billing, FHIR, Dispatcher, and Encryption to ensure high-throughput and low-latency processing.
- Spring Boot: Used for Scheduling, EMR, and Access Control to leverage robust enterprise ecosystems for complex transactions.
- PostgreSQL: Provides relational data persistence with AES-256 encryption at rest.
- Redis Enterprise: Manages caching, sessions, and distributed locks.
- Apache Kafka: Powers asynchronous event messaging between services.

## Rationale
- Polyglot architecture combines Go's speed for routing and encryption with Spring Boot's transaction management for clinical records.
- Strict component boundaries and encryption middleware guarantee HIPAA and GDPR compliance without sacrificing 99.99% availability.