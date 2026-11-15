## Overview
The Clinic Management System manages patient admissions, EMRs, scheduling, and billing for healthcare facilities. It delivers high availability, strict regulatory compliance, and sub-second performance across hybrid cloud environments.

## Key Elements
- Personas: Front Desk Staff, Clinicians, Billing Officers, Patients, Regulatory Auditors
- External Systems: Identity Provider, External Lab & Imaging Systems, Payment Gateway, Centralized SIEM, Global Traffic Manager, SD-WAN
- Containers: React SPA / React Native Mobile Client, Envoy API Gateway, EMR & Scheduling Service, Billing & Claims Service, FHIR Interoperability Service, PostgreSQL, Apache Kafka / RabbitMQ Message Brokers, AWS S3 / WORM Object Storage, HashiCorp Vault
- Broker Components: Event Streaming Core (Apache Kafka), Task & Routing Broker (RabbitMQ), Broker Encryption & Access Manager, Local Edge Buffer Component, Dead-Letter & Quarantine Router

## Relationships
- EMR & Scheduling Service -> Event Streaming Core: Publishes/consumes domain events [TCP / Kafka Protocol, TLS 1.3]
- Billing & Claims Service -> Task & Routing Broker: Dispatches task commands [AMQP 0-9-1, TLS 1.3]
- Event Streaming Core -> Centralized SIEM & Observability Platform: Streams audit logs and metrics [OTLP / HTTPS, TLS 1.3]
- FHIR Interoperability Service -> Localized Message Brokers: Exchanges clinical data [Kafka/AMQP protocol]

## Technology Stack
- React & React Native: Frontend UI for web and mobile clients
- Node.js & Java / Spring Boot: Backend microservices and business logic
- Apache Kafka & RabbitMQ: Asynchronous, decoupled messaging with local edge buffering and quorum queues
- PostgreSQL: Region-local relational data persistence
- AWS S3 & WORM Object Storage: Immutable long-term data retention (≥ 10 years)
- HashiCorp Vault: Dynamic secret management, mTLS certificate rotation, and SCRAM-SHA-512 authentication

## Rationale
This hybrid architecture guarantees 99.99% uptime and zero data loss during network partitions through active-active multi-region deployments and localized message buffering. Strict adherence to HIPAA and GDPR is enforced via end-to-end TLS 1.3 encryption, AES-256 storage, field-level PHI protection, and isolated topic-level ACLs.