## Overview
- Manages patient admissions, EMRs, scheduling, and billing for clinics.
- Ensures HIPAA/GDPR compliance with high availability.

## Key Elements
- Users: Patients, Receptionists, Clinicians, Billing Specialists, Administrators
- External Systems: Insurance Clearinghouses, External Labs/Imaging Vendors
- Containers: WAF Container, API Gateway, Patient Portal, EMR Container, Scheduling Container, Billing Container, Notification Container, Analytics & Reporting Container
- Data & Security: PostgreSQL Databases, Event Broker, Immutable Audit Storage Sink, HashiCorp Vault

## Relationships
- Patient Portal -> API Gateway: Client requests via HTTPS/TLS 1.3
- Microservices -> Event Broker: Publishes/consumes asynchronous events via mTLS and Apache Kafka / RabbitMQ
- Containers -> HashiCorp Vault: Fetches secrets and encryption keys via REST/gRPC
- Microservices -> PostgreSQL: Relational data persistence via TCP/PostgreSQL Protocol

## Technology Stack
- Hybrid Cloud: On-premises Kubernetes and AWS eu-central-1 for active-active multi-region deployment
- Event Broker: Apache Kafka / RabbitMQ with Avro/JSON Schema Registry for asynchronous messaging
- Security: HashiCorp Vault for envelope encryption (AES-256) and mTLS for zero-trust broker authentication
- Database: PostgreSQL with Patroni and etcd for high-availability clustering

## Rationale
- Active-active hybrid cloud deployment ensures 99.99% availability and zero data loss.
- Envelope encryption, mTLS, and event-driven decoupling guarantee HIPAA/GDPR compliance while achieving sub-second EMR performance.