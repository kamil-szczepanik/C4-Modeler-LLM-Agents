## Overview
The Clinic Management System is a hybrid cloud platform designed for medium-sized hospitals and clinics to securely manage patient admissions, electronic medical records (EMR), scheduling, and billing. It ensures strict HIPAA/GDPR compliance, 99.99% high availability, and sub-second EMR load times via an event-driven, decoupled container architecture.

## Key Elements
- Patients, Practitioners, Administrators (Users)
- API Gateway Container (Single entry point using JWT and rate limiting)
- Core Domain Containers (Patient registration, EMR, scheduling, billing)
- Read-Model / Query Container (CQRS pattern for high-throughput reads)
- Integration / Adapter Container (Anti-Corruption Layer for HL7 FHIR APIs)
- Background Worker Container (Asynchronous PDF generation and bulk claims)
- Data Archival & Migration Container (Offloads historical records for 10-year retention)
- Session & State Management Container (Redis-backed distributed locks)
- Envoy Sidecars (Circuit Breaker & Resilience Proxy)
- External Systems: Insurance Providers, External Labs/Imaging, IAM, Centralized Audit Logging, DR Storage

## Relationships
- Users communicate with the API Gateway Container via HTTPS (TLS 1.3).
- API Gateway routes traffic to Core Domain Containers and Read-Model Container via mTLS.
- Core Domain Containers emit events to an asynchronous message broker (Kafka/RabbitMQ).
- Integration / Adapter Container interfaces with External Labs/Imaging using HL7 FHIR over REST.
- Background Worker Container consumes async tasks from the message broker.
- Data Archival Container transfers historical data to Air-gapped DR Storage Targets.

## Technology Stack
- Hybrid Kubernetes (`on-prem-k8s` and AWS `eu-central-1`) for active-active multi-region deployment.
- Apache Kafka or RabbitMQ for asynchronous, event-driven messaging and decoupled workflows.
- Redis for in-memory session management, distributed locks, and localized caching.
- Envoy Sidecars for mTLS enforcement, telemetry injection, and circuit breaking.
- AES-256 encryption at rest combined with centralized Secrets Management.

## Rationale
The hybrid event-driven architecture with CQRS separates high-throughput reads from writes to consistently achieve sub-second EMR load times. Envoy sidecars, stateless compute nodes, and distributed locks guarantee active-active high availability (99.99%) and secure, compliant data handling.