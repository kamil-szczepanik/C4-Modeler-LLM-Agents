## Overview
The Clinic Management System is a hybrid cloud platform designed for medium-sized hospitals and clinics to securely manage patient admissions, electronic medical records, appointments, and billing. It provides high-availability clinical workflows while adhering strictly to HIPAA and GDPR regulations.

## Key Elements
- **Users:** Patients, Doctors, Billing Staff.
- **External Systems:** Third-party Insurance Gateways, Lab/Imaging Systems, External Identity Providers.
- **Containers:** API Gateway (Kubernetes Ingress, Reverse Proxy), Patient/EMR Service (Microservice, Database-per-service), Scheduling Service (Microservice, Database-per-service), Billing Service (Microservice, Database-per-service).
- **Infrastructure & Tooling:** OpenTelemetry Collector (Sidecar), Envoy (Sidecar proxy), Falco & Trivy (Node-level DaemonSets), Redis (Distributed Cache), Kafka/RabbitMQ (Message Broker), HashiCorp Vault, OPA Gatekeeper.

## Relationships
- Patients & Staff interact with the API Gateway via HTTPS/TLS 1.3 for authentication (MFA) and core operations.
- Microservices communicate internally via gRPC and REST over Kubernetes internal networking, utilizing Envoy proxies with mTLS.
- Telemetry sidecars export traces and metrics asynchronously via local Unix domain sockets to OpenTelemetry collectors.
- EMR and Scheduling services integrate with Lab/Imaging Systems using HL7 FHIR APIs over TLS.

## Technology Stack
- **Orchestration & Hybrid Cloud:** Kubernetes (on-prem-k8s and AWS eu-central-1) for active-active high availability (99.99% uptime).
- **Observability & Security:** OpenTelemetry, Prometheus, Envoy, Falco, and Trivy for monitoring, tracing, and runtime security.
- **Policy & Secrets Management:** OPA Gatekeeper for pre-admission configuration validation and HashiCorp Vault for cryptographic checksum verification.
- **Data Persistence:** AES-256 encryption at rest, backed by database-per-service patterns supporting ≥ 10-year data retention.

## Rationale
This architecture guarantees 99.99% uptime and <1s EMR response times through decoupled, asynchronous sidecar patterns and local Unix sockets that prevent cascading failures. It enforces strict HIPAA/GDPR compliance via automated OPA validation, HashiCorp Vault integrity checks, and robust Tail-based telemetry sampling.