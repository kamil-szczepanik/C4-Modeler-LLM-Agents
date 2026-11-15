## Overview
The Clinic Management System is an asynchronous messaging architecture utilizing RabbitMQ to handle patient admissions, electronic medical records, scheduling, and billing for medium-sized hospitals. It ensures 99.99% high availability and strict compliance with HIPAA and GDPR across a hybrid Kubernetes deployment.

## Key Elements
- RabbitMQ Message Broker
- RabbitMQ Cluster Operator for Kubernetes
- Direct and Topic Exchanges (`billing.direct`, `claims.topic`, `dlx.direct`)
- Quorum Queues & Dead-Letter Component
- RabbitMQ Federation Plugin
- TLS Termination & mTLS Component
- HashiCorp Vault Secrets Engine

## Relationships
- Billing & Claims Service -> Exchanges & Queues: Publishes encrypted payload events [AMQP 0-9-1 over TLS 1.3]
- Quorum Queues -> Insurance Clearinghouse: Forwards claims asynchronously via outbound connectors [AMQP/HTTPS]
- Dead-Letter Exchange -> Forensic Audit Queue: Quarantines invalid or poison messages [AMQP]

## Technology Stack
- **RabbitMQ**: Message broker chosen for reliable asynchronous messaging.
- **Quorum Queues (Raft-based)**: Selected over classical mirrored queues for zero message loss and high availability.
- **TLS 1.3 & mTLS**: Enforced for in-transit encryption to satisfy HIPAA and GDPR security mandates.
- **HashiCorp Vault**: Integrated for dynamic credential rotation and secret management.
- **Kubernetes Cluster Operator**: Deployed across a 3-node topology with anti-affinity rules for high availability.

## Rationale
This architecture ensures 99.99% uptime and fault tolerance through Raft-based quorum queues, Kubernetes operator deployments, and hybrid cloud federation. It guarantees HIPAA and GDPR compliance by enforcing end-to-end encryption (TLS 1.3, application-layer message encryption), strict access controls, and comprehensive SIEM audit logging.