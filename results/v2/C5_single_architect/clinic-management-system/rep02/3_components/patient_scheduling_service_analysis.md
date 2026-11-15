## Overview
The Patient & Scheduling Service is a Spring Boot component within the Clinic Management System designed to handle patient registrations and appointment scheduling. It ensures high concurrency, strict security, and hybrid cloud integration for medium-sized clinics.

## Key Elements
- **Patient Registration Controller & Service**: Manages patient admissions and demographic capture (R-01).
- **Scheduling Engine**: Executes appointment scheduling and resource clash checks (R-02).
- **Cache & Lock Manager**: Interfaces with Redis for distributed locking.
- **Data Access Repository**: Handles persistent storage interactions with PostgreSQL.
- **Event Publisher**: Dispatches domain events to Apache Kafka.

## Relationships
- API Gateway -> Patient Registration Controller & Service: Routes ingress traffic [gRPC]
- Patient Registration & Scheduling Engine -> Cache & Lock Manager: Acquires distributed locks [Redis RESP over TLS]
- Scheduling Engine -> Data Access Repository: Persists state [JDBC over TLS with AES-256]
- Scheduling Engine & Patient Registration -> Event Publisher: Dispatches domain events [Internal method call]
- Event Publisher -> Apache Kafka: Publishes state changes [TCP/SASL_SSL]

## Technology Stack
- **Spring Boot (Java)**: Core framework for implementing modular service components.
- **Redis**: Provides caching and distributed locks for appointment clash prevention.
- **PostgreSQL**: Stores patient and scheduling data with AES-256 encryption at rest.
- **Apache Kafka**: Handles asynchronous domain event publishing via SASL_SSL.
- **gRPC**: Facilitates low-latency internal service communication.

## Rationale
This component architecture uses domain-driven modularity and asynchronous event publishing to guarantee 99.99% availability. It isolates high-throughput scheduling locks and enforces strict HIPAA/GDPR data security constraints.