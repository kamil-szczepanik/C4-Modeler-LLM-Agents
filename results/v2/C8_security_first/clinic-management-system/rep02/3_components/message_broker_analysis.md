## Overview
The Clinic Management System provides patient admissions, electronic medical records, scheduling, and billing for clinical environments. It ensures HIPAA/GDPR compliance, 99.99% availability, and a 10-year data retention window via a hybrid cloud architecture.

## Key Elements
- Patients, Receptionists, Clinicians, Billing Specialists (Actors)
- Identity Provider (IdP), Lab & Imaging Systems, Insurance Clearinghouse (External Systems)
- API Gateway (Kong/Envoy, Rust/Go)
- Patient Portal Container (Node.js/NestJS, Go)
- EMR Core Service (Java/Spring Boot, .NET 8)
- Billing Integration Service (Java/Spring Boot)
- Audit & Compliance Daemon (Go)
- Data Tier (PostgreSQL with Citus/Multi-Master)
- Message Broker (NATS JetStream / Kafka container)
  - Connection & Auth Manager component
  - Routing & Delivery Engine component
  - Replication & Persistence Engine component

## Relationships
- Patient Portal Container -> Message Broker: Publishes asynchronous events [NATS/Kafka protocol]
- EMR Core Service -> Message Broker: Publishes transactional outbox events [TCP / NATS JetStream or Kafka protocol]
- Billing Integration Service -> Message Broker: Publishes billing events [NATS/Kafka protocol]
- Connection & Auth Manager -> Routing & Delivery Engine: Forwards authenticated client frames [gRPC]
- Routing & Delivery Engine -> Replication & Persistence Engine: Persists message streams and commits offsets [Raft consensus protocol / JetStream API]
- Routing & Delivery Engine -> Audit & Compliance Daemon: Streams real-time telemetry logs [Syslog over TLS]

## Technology Stack
- NATS JetStream / Kafka: Durable messaging supporting at-least-once delivery and distributed consensus.
- TLS 1.3 / mTLS & AES-256: Secures data in transit and at rest for HIPAA compliance.
- PostgreSQL with Citus: Multi-master database configuration for high-availability data storage.
- NVMe Storage: Provisioned IOPS for write-ahead logging performance.
- OAuth2/JWT & X.509: Strict token and certificate-based authentication.

## Rationale
The hybrid active-active architecture guarantees 99.99% availability across on-premise Kubernetes and AWS eu-central-1. Strict encryption, immutable auditing, and transactional messaging meet rigorous HIPAA, GDPR, and 10-year data retention mandates.