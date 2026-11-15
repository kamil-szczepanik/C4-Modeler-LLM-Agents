## Overview
The Clinic Management System manages patient admissions, Electronic Medical Records (EMRs), scheduling, and billing for clinical environments. It ensures HIPAA and GDPR compliance while maintaining 99.99% availability across hybrid cloud infrastructure.

## Key Elements
- Patients, Receptionists, Clinicians, Billing Specialists (Users)
- Identity Provider (IdP), Lab & Imaging Systems, Insurance Clearinghouse (External Systems)
- API Gateway (Kong/Envoy, Rust/Go)
- Patient Portal Container (Node.js/NestJS, Go)
- EMR Core Service (Java/Spring Boot, .NET 8)
- Billing Integration Service (Java/Spring Boot)
- Audit & Compliance Daemon (Go)
- Message Broker (NATS JetStream / Kafka)
- Data Tier (PostgreSQL with Citus/Multi-Master)

## Relationships
- API Gateway -> Patient Portal Container: Routes client requests [gRPC over mTLS]
- Patient Portal Container -> EMR Core Service: Coordinates resource checks [gRPC over mTLS]
- Patient Portal Container -> Message Broker: Publishes asynchronous domain events [NATS/Kafka protocol over TLS with SASL/SCRAM]
- Patient Portal Container -> Redis Cluster: Manages stateless session data [Encrypted TCP]

## Technology Stack
- Node.js/NestJS & Go: Selected for high-performance microservices and rapid API routing
- PostgreSQL with Citus: Ensures scalable, multi-master distributed relational data storage
- NATS JetStream / Kafka: Provides high-throughput, fault-tolerant event streaming
- Kubernetes & ArgoCD: Manages hybrid cloud container deployments via GitOps

## Rationale
This architecture uses an active-active hybrid cloud deployment combined with stateless container design to meet stringent 99.99% availability requirements. Strict security controls, including local JWT validation, field-level PHI encryption, and mTLS, ensure full HIPAA and GDPR compliance without compromising sub-second P95 performance.