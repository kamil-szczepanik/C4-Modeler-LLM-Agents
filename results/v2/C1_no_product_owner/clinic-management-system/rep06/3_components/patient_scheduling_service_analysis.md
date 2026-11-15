## Overview
The Patient & Scheduling Service manages patient admissions and appointment scheduling for the Clinic Management System. It operates in a hybrid Kubernetes and AWS environment to meet high availability and compliance standards.

## Key Elements
- Patient Management Component (Go, Chi router)
- Scheduling Engine Component (Go)
- Data Access Repository (Go `pgx` driver)
- Event Publisher Component (Watermill Go library)
- External State Store (PostgreSQL / Redis Enterprise)
- Message Broker (Apache Kafka)

## Relationships
- API Gateway -> Patient Management Component / Scheduling Engine Component [gRPC with Istio mTLS and JWT]
- Scheduling Engine Component -> External State Store [PostgreSQL Wire Protocol over TLS 1.3]
- Patient Management Component -> Data Access Repository [Native Go `pgx` over TLS 1.3]
- Event Publisher Component -> Message Broker [Apache Kafka / AMQP over TLS 1.3 with client-side payload encryption]

## Technology Stack
- Go: Minimal footprint, fast startup times, and efficient memory management for 99.99% availability (R-06).
- PostgreSQL / Redis Enterprise: Centralized external state management to prevent split-brain issues in active-active deployments.
- Watermill: Go library for asynchronous domain event publishing.
- Apache Kafka: Event-driven decoupling for downstream EMR and FHIR brokers.
- Istio: Native circuit breakers, retries, and mTLS for secure service mesh routing.

## Rationale
This architecture uses Go components and externalized state to ensure active-active high availability (99.99%) across hybrid Kubernetes and AWS footprints. It enforces strict HIPAA and GDPR compliance via TLS 1.3, AES-256 encryption, JWT validation, and event payload tokenization.