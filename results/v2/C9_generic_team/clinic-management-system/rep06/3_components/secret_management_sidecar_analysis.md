## Overview
[The Clinic Management System manages patient records, scheduling, and billing for medium-sized healthcare facilities. It utilizes a hybrid cloud architecture to ensure HIPAA and GDPR compliance with 99.99% availability.]

## Key Elements
- Patients, Clinical Staff, Billing Administrators
- External Labs, Imaging Systems, Identity Provider (IdP)
- API Gateway / FHIR Facade Container (Apache Camel)
- Security/Auth Proxy Container (OAuth2 / OpenID Connect)
- Domain Services Containers (Microservices, gRPC / REST over TLS)
- Async Event Bus Container (Kafka / RabbitMQ)
- Secret Management Sidecar (HashiCorp Vault)
- Observability Stack (Prometheus, Grafana, OpenTelemetry)

## Relationships
- Patients & Staff -> API Gateway / FHIR Facade Container [HTTPS / TLS 1.3]
- API Gateway / FHIR Facade Container -> Security/Auth Proxy Container [OAuth2 / OpenID Connect]
- API Gateway / FHIR Facade Container -> Domain Services Containers [gRPC / REST over TLS]
- Domain Services Containers -> Async Event Bus Container [AMQP / Kafka Protocol]
- Domain Services Containers -> Secret Management Sidecar [Local loopback interface localhost:8200 / Vault Agent templates]

## Technology Stack
- Kubernetes (on-prem-k8s and AWS eu-central-1): Hybrid deployment for high availability (99.99%)
- HashiCorp Vault: Secret Management Sidecar securing AES-256 encryption keys and credentials with automated rotation
- Apache Camel / custom FHIR facade: Interoperability via HL7 FHIR APIs
- Prometheus, Grafana, OpenTelemetry: Comprehensive observability and audit trail logging

## Rationale
- The hybrid cloud setup ensures regional redundancy and high availability across on-premise and AWS environments.
- HashiCorp Vault integration with local tmpfs caching meets strict HIPAA/GDPR security standards for data protection and auditability without degrading performance.