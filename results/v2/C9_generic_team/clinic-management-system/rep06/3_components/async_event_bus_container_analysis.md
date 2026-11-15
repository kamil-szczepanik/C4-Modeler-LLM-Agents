## Overview
The Clinic Management System manages patient admissions, Electronic Medical Records (EMR), scheduling, and billing for medium-sized healthcare facilities. It utilizes a hybrid cloud architecture to ensure 99.99% availability and compliance with HIPAA and GDPR regulations.

## Key Elements
- Patients, Clinical Staff, Billing Administrators (Actors)
- External Labs, Imaging Systems, Identity Provider (IdP) (External Systems)
- API Gateway / FHIR Facade Container (Apache Camel / custom FHIR facade)
- Security/Auth Proxy Container (OAuth2 / OpenID Connect)
- Domain Services Containers (Microservices)
- Async Event Bus Container (Kafka / RabbitMQ)
- Observability Stack (Prometheus, Grafana, OpenTelemetry)
- HashiCorp Vault (Secret Management Sidecar)

## Relationships
- Patients & Staff -> Security/Auth Proxy Container: Authenticate via Multi-Factor Authentication (OAuth2 / OIDC over TLS)
- API Gateway -> Domain Services Containers: Route REST/gRPC traffic over TLS 1.3
- Domain Services Containers -> Async Event Bus Container: Publish and consume asynchronous events with AES-256 encryption [Kafka / RabbitMQ / TLS]
- Domain Services Containers -> HashiCorp Vault: Retrieve encryption keys and secrets [REST / TLS]
- API Gateway -> External Labs & Imaging Systems: Interoperate via HL7 FHIR APIs [HTTPS / TLS]

## Technology Stack
- Kubernetes (on-prem-k8s and eu-central-1): Selected for hybrid cloud deployment and 99.99% active-active uptime.
- Kafka / RabbitMQ: Provides asynchronous event streaming, high throughput, and cross-site mirroring for disaster recovery.
- HashiCorp Vault: Ensures AES-256 encryption at rest and secure key management for PHI.
- Prometheus, Grafana, OpenTelemetry: Delivers real-time observability, consumer lag tracking, and audit logging.

## Rationale
This architecture combines microservices on Kubernetes with an event-driven messaging bus to guarantee high availability and sub-second EMR performance. Robust security controls, encryption, and strict schema management ensure full HIPAA/GDPR compliance and a 10-year data retention audit trail.