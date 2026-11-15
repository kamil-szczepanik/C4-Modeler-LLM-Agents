## Overview
The Clinic Management System is a hybrid cloud platform designed to manage patient admissions, electronic medical records, scheduling, and billing for medium-sized hospitals and clinics. It ensures strict data compliance, high availability, and seamless interoperability for clinical operations.

## Key Elements
- **Users**: Front Desk Staff, Clinicians, Billing Officers, Patients, Patient Portal Users
- **External Systems**: Lab Systems, Imaging Systems
- **Containers**: Ingress Controller (Kubernetes Ingress / Istio), Patient Registration Container, Appointment Scheduling Container, EMR Container, Billing & Insurance Claim Container, HL7 FHIR Interoperability Engine
- **Infrastructure & Storage**: PostgreSQL/MySQL Hybrid Databases, WORM-Compliant Log Storage, Kafka/RabbitMQ Message Broker, Redis Redlock for distributed locking, Fluentbit sidecar, Vault for secret management

## Relationships
- Front Desk Staff & Patients -> Ingress Controller: Access scheduling and registration via HTTPS / OAuth2 / JWT
- Ingress Controller -> Appointment Scheduling Container: Routes authenticated traffic via mTLS (Istio Service Mesh)
- Appointment Scheduling Container -> Redis Redlock: Performs distributed locking for concurrent multi-resource clash checks
- Appointment Scheduling Container -> Kafka/RabbitMQ Message Broker: Asynchronously decouples SMS/email reminders
- Appointment Scheduling Container -> WORM-Compliant Log Storage: Streams audit logs asynchronously via Fluentbit sidecar
- HL7 FHIR Interoperability Engine -> Lab & Imaging Systems: Exchanges clinical data via HL7 FHIR REST APIs

## Technology Stack
- **Orchestration & Mesh**: Kubernetes (`on-prem-k8s` and `eu-central-1`) with Istio Service Mesh for mTLS, circuit breaking, and traffic routing
- **Security & Auth**: OAuth2 / JWT with zero-trust local token validation, HashiCorp Vault for automated secret rotation, and AES-256 encryption at rest
- **State & Concurrency**: PostgreSQL/MySQL hybrid databases with Redis Redlock for distributed locking and conflict-free data handling
- **Messaging & Logging**: Kafka/RabbitMQ for asynchronous event-driven messaging; Fluentbit sidecars for asynchronous audit shipping to WORM-compliant storage
- **Observability**: OpenTelemetry for distributed tracing; Prometheus and Grafana for synthetic monitoring

## Rationale
This architecture guarantees 99.99% high availability and sub-second P95 performance through asynchronous event decoupling, distributed locking, and active-active hybrid cloud replication. Strict HIPAA and GDPR compliance are enforced via AES-256 encryption, zero-trust token validation, role-based access control, and tamper-evident WORM log storage.