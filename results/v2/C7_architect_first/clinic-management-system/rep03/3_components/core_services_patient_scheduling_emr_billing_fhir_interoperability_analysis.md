## Overview
The Clinic Management System is a hybrid cloud platform providing patient registration, scheduling, Electronic Medical Records (EMR), and billing for healthcare facilities. It ensures high availability, strict HIPAA/GDPR compliance, and 10-year data retention.

## Key Elements
- **Users**: Doctors, Nurses, Receptionists, Billing Staff, Clinic Administrators, Patients
- **External Systems**: Identity Provider (IdP), External Labs & Imaging Systems, Payment Gateway / Insurance Clearinghouse
- **Containers**: API Gateway (Nginx / Kong), Web Application (React / TypeScript), Core Services (NestJS Modular Monolith), PostgreSQL (Active-Passive), Redis, Apache Kafka, AWS S3 Object Lock
- **Core Components**: Patient & Scheduling Component, EMR Component, Billing Component, FHIR Interoperability Component

## Relationships
- API Gateway -> Core Services: Routes traffic securely via gRPC over mTLS
- Core Services -> PostgreSQL: Reads/writes relational data with AES-256 at rest using SQL over TLS with dedicated component roles
- Core Services -> Redis: Caches edge data using the Redis Protocol encrypted with TLS 1.3
- Core Services -> Apache Kafka: Publishes and consumes asynchronous domain events using Kafka Protocol with SASL/SCRAM authentication and application-layer encryption
- Core Services -> AWS S3 Object Lock: Stores immutable audit logs and compliance data via HTTPS / AWS API
- FHIR Interoperability Component -> External Labs & Imaging Systems: Exchanges medical data using HL7 FHIR APIs and SMART-on-FHIR scopes

## Technology Stack
- **Backend**: NestJS (TypeScript) utilizing a Modular Monolith pattern for clean boundary isolation
- **Database**: PostgreSQL with isolated schemas per component and Flyway for schema migrations
- **Caching**: Redis for low-latency resource-clash checks and edge data caching
- **Messaging**: Apache Kafka for asynchronous workflows, event streaming, and dead-letter queues
- **Storage**: AWS S3 Object Lock for write-once, tamper-proof 10-year audit compliance
- **Infrastructure**: Kubernetes (on-prem-k8s and AWS eu-central-1) utilizing OpenTelemetry and Prometheus/Grafana

## Rationale
This architecture uses a NestJS modular monolith deployed on a hybrid Kubernetes infrastructure to isolate resource-heavy clinical operations and guarantee sub-second EMR responses. Strong cryptographic controls, isolated database schemas, and immutable object storage satisfy strict HIPAA/GDPR compliance and 99.99% availability requirements.