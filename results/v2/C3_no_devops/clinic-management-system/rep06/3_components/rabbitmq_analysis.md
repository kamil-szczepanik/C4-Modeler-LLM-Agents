## Overview
The Clinic Management System is a hybrid cloud platform designed to manage patient admissions, electronic medical records, scheduling, and billing for medium-sized hospitals and clinics. It ensures HIPAA/GDPR compliance, high availability (99.99%), and robust asynchronous messaging using RabbitMQ.

## Key Elements
- **RabbitMQ**: Core message broker container.
- **Erlang/RabbitMQ Core**: Direct and Topic Exchanges, AMQP 0-9-1 Connection Listener (`Erlang/Ranch`), and Dead-Letter Exchanges (DLX).
- **RabbitMQ Quorum Queues / Raft**: Durable queues providing consensus across nodes.
- **RabbitMQ auth_backend_oauth2**: OAuth2/LDAP-based authorization and access control plugin.
- **RabbitMQ Webhooks / Shovel plugin**: Secure HTTPS webhook integration route.
- **DLQ Notification Webhook / Consumer**: Python/FastAPI worker for business alerts.
- **Enterprise Identity Provider (IdP) & SIEM System**: External security integration systems.

## Relationships
- **EMR, Scheduling, & Billing Services -> RabbitMQ**: Publishes and consumes asynchronous events via AMQP 0-9-1 using TLS 1.3 / mTLS.
- **RabbitMQ -> Enterprise IdP**: Validates access permissions using `auth_backend_oauth2`.
- **RabbitMQ -> DLQ Notification Worker**: Forwards dead-lettered payloads via HTTPS webhooks.
- **RabbitMQ -> Audit Archival / SIEM System**: Forwards real-time audit logs over TLS.

## Technology Stack
- **RabbitMQ & Erlang/Ranch**: High-performance message broker core for asynchronous event processing.
- **Quorum Queues (Raft Consensus)**: Ensures zero data loss and high availability (99.99%) across Kubernetes nodes.
- **TLS 1.3 & mTLS**: Secures all inter-service AMQP transport traffic.
- **OAuth2 (`auth_backend_oauth2`)**: Enforces RBAC/ABAC integrated with the Enterprise IdP.
- **AES-256**: Encrypts Kubernetes persistent storage volumes and Raft logs at rest.
- **Python/FastAPI**: Powers the DLQ notification consumer for administrative alerts.

## Rationale
This architecture uses RabbitMQ with Quorum Queues, mTLS, and OAuth2 to guarantee HIPAA/GDPR compliance and 99.99% availability. Integrating Dead-Letter Queues with a FastAPI webhook consumer ensures zero silent message loss for critical clinical and billing workflows.