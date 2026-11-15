## Overview
The Clinic Management System is a secure healthcare platform providing patient registration, appointment scheduling, EMR tracking, and billing. It ensures HIPAA/GDPR compliance and 99.99% availability via a hybrid cloud infrastructure.

## Key Elements
- Patients, Clinicians, Hospital Administrators
- API Gateway (Kong/Envoy)
- Web Frontend (React, TypeScript, Nginx, AWS CloudFront)
- Core Services Container (Java, Spring Boot)
- EMR Service (Node.js, TypeScript)
- Database Layer (PostgreSQL)
- Event Broker (Apache Kafka)
- Integration Worker (Apache Camel, Python)
- Key Management Service (HashiCorp Vault, AWS KMS)
- Background Job Scheduler (Temporal.io)
- Observability Collector (OpenTelemetry, Prometheus, Grafana Loki)

## Relationships
- Web Frontend -> API Gateway: Sends encrypted UI requests [HTTPS/WSS]
- API Gateway -> Core Services Container: Routes business logic traffic [gRPC over mTLS]
- API Gateway -> EMR Service: Routes electronic medical records traffic [gRPC over mTLS]
- API Gateway -> Key Management Service: Validates keys and secrets [HTTPS/REST]
- API Gateway -> Redis Sidecar: Tracks distributed rate limits [RESP over TCP with TLS]
- Core Services / EMR -> Database Layer: Persists clinical and administrative data [PostgreSQL Wire Protocol with SSL]
- Services -> Event Broker: Publishes and consumes domain events [Kafka Protocol with SASL/TLS]

## Technology Stack
- Kong/Envoy: Chosen for API Gateway routing and 99.99% availability
- Java / Spring Boot: Core business logic services for enterprise reliability
- Node.js / TypeScript: EMR service for high-performance record handling
- PostgreSQL: Relational storage meeting AES-256 encryption requirements
- Apache Kafka: Event broker for asynchronous, decoupled service communication
- HashiCorp Vault / AWS KMS: Cryptographic key management for AES-256 and TLS

## Rationale
This architecture uses an active-active hybrid setup to guarantee 99.99% uptime and low-latency performance. Strict mTLS, TLS termination, and AES-256 encryption satisfy mandatory HIPAA and GDPR security standards.