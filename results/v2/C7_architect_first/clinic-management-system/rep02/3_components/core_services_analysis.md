## Overview
The Clinic Management System is a hybrid cloud platform designed to manage patient admissions, electronic medical records (EMR), scheduling, and billing for medium-sized hospitals and clinics. It ensures strict HIPAA/GDPR compliance, 99.99% availability, and a 10-year data retention policy.

## Key Elements
- **Users**: Patients, Doctors, Nurses, Clinic Staff, Hospital Administrators, Billing Specialists / Revenue Cycle Managers
- **Containers**: API Gateway (Nginx / Envoy), Identity & Access Management (Keycloak / OAuth2 Proxy), Core Services (Spring Boot / Java), Integration Service (Node.js / Apache Camel), Message Broker (Kafka / RabbitMQ), Data Tier (PostgreSQL), Storage (WORM Object Storage)
- **Core Services Components**: Patient Registry Component, Scheduling Engine, EMR Management Component, Billing Processor
- **Infrastructure & Security**: Linkerd (Service Mesh), HashiCorp Vault, OpenTelemetry, ArgoCD

## Relationships
- API Gateway -> Core Services: Routes internal API requests via gRPC over mTLS with propagated OAuth2/JWT tokens.
- EMR Management -> Data Tier: Writes encrypted patient records and tamper-evident audit logs via JDBC with AES-256.
- Scheduling Engine -> Message Broker: Emits appointment lifecycle events using Kafka.
- Core Services -> WORM Storage: Archives cryptographically signed audit logs for long-term retention.

## Technology Stack
- **Spring Boot / Java**: Powers the modular Core Services container for robust clinical workflows.
- **PostgreSQL**: Stores transactional patient and billing data securely with AES-256 at rest.
- **Kafka**: Manages asynchronous event-driven messaging for decoupled billing and scheduling.
- **Linkerd**: Enforces zero-trust mTLS internally within service boundaries.
- **HashiCorp Vault**: Manages dynamic database credentials and envelope encryption keys.
- **OpenTelemetry**: Provides unified hybrid telemetry and distributed tracing.
- **Kubernetes & ArgoCD**: Orchestrates containers across on-prem and AWS (`eu-central-1`) via GitOps.

## Rationale
This architecture uses a secure modular monolith-within-container design to meet strict 99.99% uptime and <1s EMR performance SLAs without WAN lock contention. It integrates robust zero-trust security and automated WORM backups to satisfy mandatory HIPAA/GDPR compliance.