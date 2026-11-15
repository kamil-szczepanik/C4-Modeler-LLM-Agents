## Overview
The Clinic Management System is a hybrid cloud platform designed to manage patient admissions, electronic medical records, scheduling, and billing for medium-sized hospitals and clinics. It ensures high availability, strict compliance, and seamless interoperability.

## Key Elements
- Patients, Practitioners, and Billing Staff (System Users)
- External Lab and Imaging Systems (External Systems)
- API Gateway / Reverse Proxy Container
- Core Domain Containers (Kubernetes Microservices)
- Integration Engine Container (HL7 FHIR Translator)
- Data Access & Governance Container Layer (AES-256 Storage)
- Asynchronous Event Bus Container (Kafka / RabbitMQ with DLQ)
- Shared Observability & Telemetry Container (Prometheus, Fluentbit, OpenTelemetry)
- Configuration and Secrets Management Container (Vault / Kubernetes Secrets)

## Relationships
- Patients & Staff -> API Gateway / Reverse Proxy Container: Accesses system features [HTTPS / TLS 1.3]
- API Gateway -> Core Domain Containers: Routes client requests [gRPC / REST]
- Integration Engine Container -> External Lab and Imaging Systems: Exchanges clinical data [HL7 FHIR APIs]
- Core Domain Containers <-> Asynchronous Event Bus Container: Publishes and consumes domain events [Kafka Protocol]
- Integration Engine Container -> Asynchronous Event Bus Container: Routes translation events and Dead Letter Queues [Kafka Protocol]

## Technology Stack
- Kubernetes (on-prem-k8s and AWS eu-central-1): Hybrid orchestration enforcing resource quotas, health probes, and canary rollouts via Argo Rollouts.
- Apache Kafka / RabbitMQ: Event bus ensuring asynchronous decoupling, Dead Letter Queues (DLQ), and transactional outbox patterns.
- Redis: Distributed caching for stateless Integration Engine translation lookups.
- Resilience4j: Circuit breaking and bulkhead patterns for outbound fault tolerance.
- Prometheus, Fluentbit, OpenTelemetry: Shared observability stack with HIPAA-compliant PHI payload sanitization in logs.
- Vault / Kubernetes Secrets: Secure configuration and credential management.

## Rationale
This architecture uses an asynchronous event-driven model combined with strict circuit breakers, schema validation gateways, and dead letter queues to prevent external system failures from impacting core clinical workflows. The hybrid Kubernetes deployment with stateless integration containers and active-active replication directly satisfies the 99.99% availability, HIPAA/GDPR compliance, and sub-second EMR performance requirements.