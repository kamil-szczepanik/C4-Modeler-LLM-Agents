## Overview
The Clinic Management System is a hybrid cloud platform designed to manage patient admissions, electronic medical records (EMR), scheduling, and billing for medium-sized hospitals and clinics. It ensures high availability, strict compliance, and rapid data access for clinical staff.

## Key Elements
- **Users**: Patients, Practitioners, Administrators
- **Containers**: API Gateway Container, Core Domain Containers (Registration, Scheduling, EMR, Billing), Read-Model / Query Container, Integration / Adapter Container, Background Worker Container, Session & State Management Container (Redis), Asynchronous Message Broker (Kafka/RabbitMQ)
- **Infrastructure**: On-premise Kubernetes clusters and AWS eu-central-1 region
- **External Systems**: Identity & Access Management (IAM), Centralized Audit Logging Service, External Notification Providers, Air-gapped DR Storage Targets

## Relationships
- **API Gateway Container -> Core Domain Containers**: Routes incoming client traffic via mutual TLS (mTLS)
- **Core Domain Containers -> Asynchronous Message Broker**: Emits domain events using Apache Kafka or RabbitMQ
- **Core Domain Containers -> Session & State Management Container**: Offloads stateless session data via Redis
- **Core Domain Containers -> Integration / Adapter Container**: Connects to external labs and imaging systems via HL7 FHIR APIs and REST

## Technology Stack
- **Kubernetes**: Used for container orchestration across hybrid on-premise and AWS (eu-central-1) environments to achieve active-active high availability.
- **Redis**: Provides session and state management for stateless microservices to support horizontal scaling.
- **Apache Kafka / RabbitMQ**: Acts as the asynchronous message broker for decoupled event-driven workflows.
- **HL7 FHIR / REST**: Standardizes interoperability protocols with external lab and imaging systems.
- **AES-256 & JWT**: Enforces data-at-rest encryption and secure multi-factor authentication for HIPAA/GDPR compliance.

## Rationale
This architecture uses domain-driven microservices with database-per-service isolation to strictly enforce HIPAA and GDPR boundaries while supporting a 10-year data retention mandate. Asynchronous messaging, stateless container design, and strict read/write segregation protect core transactional databases to consistently achieve 99.99% uptime and sub-second EMR response times.