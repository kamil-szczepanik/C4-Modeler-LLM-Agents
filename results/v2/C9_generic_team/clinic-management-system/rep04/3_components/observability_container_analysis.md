## Overview
The Clinic Management System is a hybrid cloud platform managing patient admissions, EMRs, scheduling, and billing for healthcare facilities. Its core purpose is to provide highly available, secure, and interoperable clinical IT operations.

## Key Elements
- Hospital Staff and Patients (Actors)
- Frontend Container
- API Gateway
- Core Domain Containers
- Integration / FHIR Adapter Container
- Asynchronous Event Bus
- Audit Logging & Compliance Container
- Observability Container
- Shared Configuration & Secret Management Sidecar
- External Lab and Imaging Systems (External Systems)

## Relationships
- Frontend Container communicates with API Gateway via HTTPS/TLS
- API Gateway routes requests to Core Domain Containers via gRPC/REST and Kubernetes
- Integration / FHIR Adapter Container connects to External Lab and Imaging Systems via HL7 FHIR and HTTPS
- Core Domain Containers publish events to Asynchronous Event Bus via AMQP (Kafka/RabbitMQ)
- Observability Container collects metrics and traces from all containers using OpenTelemetry and Prometheus

## Technology Stack
- Kubernetes (on-prem-k8s and AWS eu-central-1): Hybrid cloud orchestration ensuring high availability and multi-region deployment.
- OpenTelemetry: Vendor-neutral framework for metrics, logs, and distributed tracing.
- W3C Trace Context: Standard for propagating trace correlation IDs across synchronous and asynchronous boundaries.
- Prometheus & Grafana: Scraping and visualization backend for operational metrics and SLO tracking.
- Kafka/RabbitMQ: Asynchronous event bus supporting message processing and event-driven workflows.

## Rationale
This architecture uses hybrid Kubernetes and active-active deployment patterns to meet the strict 99.99% uptime requirement. OpenTelemetry integration combined with strict PHI/PII data sanitization ensures comprehensive observability while maintaining HIPAA and GDPR compliance.