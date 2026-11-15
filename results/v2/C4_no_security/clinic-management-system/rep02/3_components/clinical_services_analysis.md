## Overview
The Clinic Management System manages patient admissions, electronic medical records (EMR), scheduling, and billing for medium-sized healthcare facilities. It ensures high availability, strict HIPAA/GDPR compliance, and sub-second clinical workflows.

## Key Elements
- **API Gateway:** Nginx / Kong managing external ingress.
- **Service Mesh:** Istio / Linkerd enforcing mTLS and zero-downtime deployments.
- **Clinical Services:** Java / Spring Boot core backend containing Patient Registration, Scheduling, EMR Management, Event Publisher, and Caching components.
- **Caching Layer:** Redis with encryption for EMR data.
- **Message Broker:** Apache Kafka for asynchronous domain events.
- **Database:** PostgreSQL with AES-256 encryption.
- **Storage & Security:** S3-compatible Tiered Storage and AWS KMS/HSM.

## Relationships
- **API Gateway -> Clinical Services:** Routes HTTP/gRPC traffic via gRPC over mTLS.
- **Clinical Services -> PostgreSQL:** Reads and writes clinical data via JDBC over TLS.
- **EMR Management -> Redis:** Caches clinical views via TCP over TLS.
- **EMR Management -> AWS KMS/HSM:** Retrieves cryptographic keys via HTTPS over mTLS.
- **Clinical Services -> Apache Kafka:** Publishes asynchronous domain events via TCP.

## Technology Stack
- **Java / Spring Boot:** Chosen for robust enterprise patterns and high-performance EMR retrieval.
- **PostgreSQL & Redis:** Provides transactional reliability and encrypted sub-second caching.
- **Apache Kafka:** Ensures decoupled, resilient asynchronous event processing.
- **Istio Service Mesh:** Guarantees zero-downtime deployments and secure mTLS communication.

## Rationale
This hybrid architecture combines robust Spring Boot services with cryptographic controls, satisfying strict HIPAA/GDPR constraints. Distributed tracing and active-active scaling ensure 99.99% availability and sub-second EMR performance.