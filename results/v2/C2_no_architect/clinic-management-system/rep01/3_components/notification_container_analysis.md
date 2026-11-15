## Overview
[The Clinic Management System manages patient admissions, EMR, scheduling, and billing for medium-sized healthcare facilities. The Notification Container dispatches multi-channel alerts while ensuring strict HIPAA/GDPR compliance and 99.99% availability.]

## Key Elements
- Patients, Receptionists, Clinicians, Billing Specialists, Hospital Administrators
- API Gateway (Kubernetes Ingress / Gateway API)
- Notification Container (Stateless Microservice / REST / gRPC)
- Event Broker (Apache Kafka / RabbitMQ)
- Immutable Audit Storage Sink
- HashiCorp Vault (Secrets Management)
- Third-party SMS, Email, and Push Gateway APIs

## Relationships
- Patient Portal Container -> API Gateway: HTTP/REST/gRPC requests [OAuth2/JWT]
- Notification Container -> Event Broker: Consumes clinical and operational events [Apache Kafka / RabbitMQ]
- Notification Container -> Third-party Gateways: Dispatches multi-channel alerts [TLS 1.3, HTTPS]
- Notification Container -> Immutable Audit Storage Sink: Emits delivery receipts for 10-year retention [Secure Protocol]
- Notification Container -> HashiCorp Vault: Dynamically fetches provider API keys and secrets [mTLS / API]

## Technology Stack
- Kubernetes: Horizontally autoscaled runtime for high availability (R-06)
- Apache Kafka / RabbitMQ: Event broker with dead-letter queue (DLQ) for resilient messaging
- OpenTelemetry & Structured Logging: Distributed tracing with automated PII/PHI log scrubbing
- HashiCorp Vault: Dynamic secret injection and encryption key management
- Redis/PostgreSQL: Caching layer for idempotency tracking and deduplication

## Rationale
[Stateless container design on Kubernetes paired with Kafka ensures active-active 99.99% availability and fault tolerance. Strict PII/PHI payload minimization, Vault-backed secrets, and immutable audit logging satisfy rigorous HIPAA and GDPR compliance constraints.]