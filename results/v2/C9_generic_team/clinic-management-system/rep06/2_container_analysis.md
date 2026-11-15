## Overview
The Clinic Management System is a hybrid cloud-deployed platform built for medium-sized hospitals and clinics to streamline clinical, administrative, and financial operations. Its core purpose is to securely manage patient admissions, electronic medical records (EMR), appointment scheduling, and billing while ensuring strict regulatory compliance.

## Key Elements
* Patients, Clinical Staff, and Billing Administrators (Actors)
* External Labs, Imaging Systems, and Identity Provider / IdP (External Systems)
* API Gateway / FHIR Facade Container (Apache Camel / custom FHIR facade)
* Security/Auth Proxy Container (OAuth2 / OpenID Connect)
* Domain Services Containers (Patient/EMR, Scheduling, Billing)
* Async Event Bus Container (Kafka / RabbitMQ)
* Background Worker Container and Database Migration Init-Containers
* Observability Stack (Prometheus, Grafana, OpenTelemetry)
* Secret Management Sidecar (Vault)

## Relationships
* Patients and Staff interact with the API Gateway via HTTPS (TLS 1.3, OAuth2/OIDC via IdP).
* API Gateway routes traffic to Domain Services via gRPC / REST over TLS.
* Domain Services publish and consume asynchronous messages via the Async Event Bus.
* API Gateway/FHIR Facade communicates with External Labs and Imaging Systems using HL7 FHIR APIs over HTTPS.
* Domain Services connect to isolated PostgreSQL databases managed via PgBouncer and encrypted with AES-256.

## Technology Stack
* Kubernetes (on-prem-k8s and AWS eu-central-1): Chosen for active-active high availability (≥ 99.99%).
* PostgreSQL with PgBouncer: Provides database-per-service isolation and connection pooling for the 10-year data retention requirement.
* Apache Kafka / RabbitMQ: Enables asynchronous decoupling for high throughput and sub-second EMR response times.
* Prometheus, Grafana, OpenTelemetry: Delivers centralized observability, metrics, and distributed tracing.
* HashiCorp Vault: Secures AES-256 encryption keys and credentials for HIPAA/GDPR compliance.

## Rationale
This containerized microservices architecture utilizes database isolation, event-driven decoupling, and a hybrid Kubernetes deployment to guarantee 99.99% availability and sub-second EMR performance. Built-in security layers, automated migrations, and robust observability ensure strict HIPAA/GDPR compliance and long-term maintainability.