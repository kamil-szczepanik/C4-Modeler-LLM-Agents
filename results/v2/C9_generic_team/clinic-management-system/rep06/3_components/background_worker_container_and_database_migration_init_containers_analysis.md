## Overview
The Clinic Management System is a hybrid cloud platform managing patient records, scheduling, billing, and admissions for healthcare facilities. It ensures HIPAA/GDPR compliance, 99.99% availability, and 10-year data retention.

## Key Elements
* Patients, Clinical Staff, Billing Administrators
* External Labs, Imaging Systems, Identity Provider (IdP)
* API Gateway / FHIR Facade Container (Apache Camel / custom FHIR facade)
* Security/Auth Proxy Container (OAuth2 / OpenID Connect)
* Domain Services Containers (Microservices, gRPC / REST over TLS)
* Async Event Bus Container (Kafka / RabbitMQ)
* Background Worker Container and Database Migration Init-Containers (Kubernetes Jobs / Init-Containers)
* Observability Stack (Prometheus, Grafana, OpenTelemetry)
* Secret Management Sidecar (HashiCorp Vault)

## Relationships
* Patients and Staff interact via UI/API through Security/Auth Proxy Container using OAuth2 / OpenID Connect over TLS.
* Domain Services communicate internally using gRPC and REST over TLS.
* Background Workers and Migration Containers process tasks asynchronously via Kafka / RabbitMQ and access databases with dynamic HashiCorp Vault credentials.
* External systems integrate via HL7 FHIR APIs through the API Gateway.

## Technology Stack
* Kubernetes & Hybrid Cloud: On-premise Kubernetes and AWS (eu-central-1) for active-active high availability (99.99% uptime).
* Kafka / RabbitMQ: Async event bus for reliable message queuing and task processing.
* OpenTelemetry, Prometheus, & Grafana: End-to-end tracing, structured JSON logging, and metrics monitoring.
* HashiCorp Vault: Dynamic database credential leasing and secret management.
* PostgreSQL / Redis: Persistent data storage and execution state tracking for idempotent job processing.

## Rationale
This architecture uses decoupled Kubernetes background jobs, strict idempotency controls, and OpenTelemetry tracing to guarantee data integrity and fault tolerance. Hybrid active-active replication and rigorous resource isolation ensure strict HIPAA compliance, secure auditing, and sub-second performance under high concurrency.