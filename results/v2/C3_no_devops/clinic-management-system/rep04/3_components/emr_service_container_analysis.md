## Overview
The Clinic Management System manages patient admissions, electronic medical records, scheduling, and billing for medium-sized hospitals and clinics. It ensures strict HIPAA/GDPR compliance, high availability (99.99%), and robust data retention using a hybrid cloud architecture.

## Key Elements
- Patients, Clinic Staff, Clinicians, Billing Specialists, System Administrators
- Frontend Container (React, TypeScript)
- API Gateway (Kong / Envoy, Istio Service Mesh)
- EMR Service Container (Go) containing:
  - EMR Management Component (Go)
  - Access Control Enforcer Component (Go)
  - Timeline Aggregator Component (Go)
- Audit & Compliance Container (Go, Apache Kafka)
- PostgreSQL Database (AES-256)
- Encrypted Redis Cache (TLS/mTLS)

## Relationships
- API Gateway -> EMR Service Container: Routes requests [gRPC/REST over Istio mTLS]
- EMR Management Component -> PostgreSQL Database: Persists clinical data [Encrypted AES-256 connection]
- EMR Service Container -> Audit & Compliance Container: Streams audit and break-glass events [Kafka, TLS + SASL]
- EMR Query/Timeline Component -> PostgreSQL / Encrypted Redis Cache: Retrieves aggregated patient history [Encrypted connection]

## Technology Stack
- Go: Chosen for the EMR service components to ensure minimal memory footprint, fast execution, and high concurrency.
- PostgreSQL: Provides reliable relational data storage with AES-256 encryption at rest.
- Encrypted Redis: Used for low-latency read caching with mandatory in-memory encryption and mTLS.
- Apache Kafka: Enables secure, asynchronous event streaming for audit and compliance trails.
- Istio Service Mesh: Secures service-to-service communication via mTLS.

## Rationale
This architecture uses Go-based microservices and a hybrid cloud deployment to achieve sub-second EMR performance (<1s P95) while meeting strict HIPAA/GDPR compliance. Local stateless JWT validation and encrypted caching protect patient health information without introducing latency bottlenecks.