## Overview
The Clinic Management System is a hybrid cloud clinical IT platform designed to handle patient admissions, electronic medical records (EMR), scheduling, and billing. It provides high availability, stringent security, and interoperability for medium-sized hospitals and clinics.

## Key Elements
- Patients, Clinical Staff, Billing Administrators (Users)
- External Labs, Imaging Systems, Identity Provider (IdP)
- API Gateway / FHIR Facade Container (Apache Camel / custom FHIR facade)
- Security/Auth Proxy Container (OAuth2 / OpenID Connect)
- Domain Services Containers (Microservices: Patient/EMR, Scheduling, Billing)
- Async Event Bus Container (Kafka / RabbitMQ)
- Background Worker Container and Database Migration Init-Containers
- Observability Stack (Prometheus, Grafana, OpenTelemetry)
- Secret Management Sidecar (HashiCorp Vault)

## Relationships
- API Gateway / FHIR Facade Container -> Domain Services Containers: Route traffic [gRPC / REST over TLS]
- Domain Services Containers -> Async Event Bus Container: Publish/consume asynchronous events [Kafka / RabbitMQ]
- Domain Services Containers -> Secret Management Sidecar: Retrieve keys and secrets [HashiCorp Vault API]
- Domain Services Containers -> External Labs / Imaging Systems: Interoperate via HL7 FHIR APIs

## Technology Stack
- Kubernetes / Hybrid Cloud (on-prem-k8s, eu-central-1): Orchestration and hybrid deployment supporting 99.99% availability.
- gRPC & Protocol Buffers: High-performance internal communication meeting the <1s P95 EMR performance constraint.
- Apache Kafka / RabbitMQ: Asynchronous messaging supporting the transactional outbox pattern.
- OpenTelemetry, Prometheus, Grafana: Distributed tracing and monitoring for real-time observability.
- HashiCorp Vault: Secure secret management and AES-256 data encryption support.

## Rationale
This architecture uses microservices with strict Domain-Driven Design (DDD) bounded contexts to achieve independent scalability, fault isolation, and 99.99% availability. Implementing zero-trust mTLS, transactional outbox patterns, and rigorous audit logging ensures full HIPAA and GDPR compliance for sensitive clinical data.