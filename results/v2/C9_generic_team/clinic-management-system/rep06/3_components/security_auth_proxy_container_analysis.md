## Overview
The Clinic Management System is a hybrid cloud platform designed for medium-sized hospitals and clinics to manage patient admissions, electronic medical records (EMR), scheduling, and billing securely. It ensures high availability, strict HIPAA/GDPR compliance, and interoperability via HL7 FHIR standards.

## Key Elements
- **Users**: Patients, Clinical Staff, Billing Administrators
- **External Systems**: External Labs, Imaging Systems, Identity Provider (IdP)
- **API Gateway / FHIR Facade Container**: Apache Camel / custom FHIR facade
- **Security/Auth Proxy Container**: OAuth2 / OpenID Connect reverse proxy (Envoy)
- **Domain Services Containers**: Microservices using gRPC / REST over TLS
- **Async Event Bus Container**: Kafka / RabbitMQ
- **Supporting Containers**: Background Worker, Kubernetes Init-Containers, Prometheus, Grafana, OpenTelemetry, HashiCorp Vault Sidecar

## Relationships
- **API Gateway / FHIR Facade Container -> Security/Auth Proxy Container**: Validates requests and authenticates sessions via OAuth2 / OpenID Connect [gRPC / REST over TLS]
- **Security/Auth Proxy Container -> Identity Provider (IdP)**: Authenticates users and retrieves JWKS public keys [OAuth2 / OIDC]
- **Security/Auth Proxy Container -> Domain Services Containers**: Enforces mTLS and forwards authenticated requests [gRPC / REST over TLS]
- **Domain Services Containers -> Async Event Bus Container**: Publishes and consumes domain events [Kafka / RabbitMQ]

## Technology Stack
- **Kubernetes**: Orchestration platform providing active-active deployment across on-prem-k8s and eu-central-1 for 99.99% availability.
- **Envoy**: Lightweight reverse proxy engine for mTLS, rate-limiting, and request schema validation.
- **OAuth2 / OpenID Connect with JWKS**: Stateless authentication using locally validated short-lived JWTs to minimize IdP bottlenecks.
- **HashiCorp Vault**: Secure runtime injection of dynamic configurations, secrets, and cryptographic keys.
- **OpenTelemetry, Prometheus, & Grafana**: Structured JSON logging and observability stack for comprehensive audit trails.

## Rationale
This hybrid architecture isolates security perimeters and leverages stateless proxy containers with local token caching to meet strict sub-second performance goals. Strict adherence to mTLS, Vault secrets management, and automated health probing ensures compliance with HIPAA/GDPR while guaranteeing 99.99% high availability.