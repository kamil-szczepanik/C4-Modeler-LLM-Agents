## Overview
The Clinic Management System is a hybrid cloud platform providing patient registration, scheduling, EMR, and billing for healthcare facilities. It ensures high availability, strict HIPAA/GDPR compliance, and interoperability via HL7 FHIR APIs.

## Key Elements
- Patients, Clinical Staff, Billing Administrators (Actors)
- External Labs, Imaging Systems, Identity Provider (IdP) (External Systems)
- API Gateway / FHIR Facade Container (Apache Camel / custom FHIR facade)
- Security/Auth Proxy Container (OAuth2 / OpenID Connect)
- Domain Services Containers (Microservices)
- Async Event Bus Container (Kafka / RabbitMQ)
- Observability Stack Container (Prometheus, Grafana, OpenTelemetry)
- Background Worker and Database Migration Init-Containers (Kubernetes Jobs / Init-Containers)
- Secret Management Sidecar (HashiCorp Vault)

## Relationships
- Patients and Staff interact with the API Gateway and Security Proxy via HTTPS/TLS.
- Domain Services communicate via gRPC/REST over TLS and publish events over Kafka/RabbitMQ.
- External Labs and Imaging Systems connect via HL7 FHIR APIs over HTTPS.
- Observability Stack collects telemetry via OpenTelemetry Protocol (OTLP) from all containers.

## Technology Stack
- Kubernetes (on-prem-k8s and AWS eu-central-1): Hybrid deployment for 99.99% availability.
- OpenTelemetry, Prometheus, Grafana: Centralized metrics, tracing, and monitoring with local buffering collectors.
- Apache Camel / Custom FHIR Facade: Interoperability and API management.
- Kafka / RabbitMQ: Asynchronous event-driven messaging.
- HashiCorp Vault: Secure secret management and AES-256 encryption at rest.

## Rationale
This architecture combines active-active hybrid Kubernetes infrastructure with robust observability and strict security controls to satisfy 99.99% uptime, 10-year data retention, and HIPAA/GDPR compliance. Decoupled telemetry and strict API standards ensure core clinical execution paths remain protected during high-load scenarios.