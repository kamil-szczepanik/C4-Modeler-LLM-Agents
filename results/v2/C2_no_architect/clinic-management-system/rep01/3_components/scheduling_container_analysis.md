## Overview
The Clinic Management System manages patient admissions, EMR, scheduling, and billing for medium-sized healthcare facilities. It ensures high availability, strict HIPAA/GDPR compliance, and seamless interoperability.

## Key Elements
- Users: Patients, Receptionists, Clinicians, Billing Specialists, Hospital Administrators
- Containers: WAF Container, API Gateway (Kubernetes Ingress), Patient Portal, EMR, Scheduling, Billing, Notification, Analytics & Reporting
- Infrastructure: PostgreSQL Databases (Patroni/etcd), Apache Kafka / RabbitMQ Event Broker, HashiCorp Vault, Immutable Audit Storage Sink

## Relationships
- API Gateway -> Scheduling Container: Routes HTTPS and mTLS requests [SPIFFE/SPIRE]
- Scheduling Container -> Event Broker: Publishes and consumes asynchronous events [Apache Kafka / RabbitMQ]
- Scheduling Container -> PostgreSQL Databases: Executes atomic reservation locks and SQL reads/writes [Active-Active Consensus]

## Technology Stack
- Orchestration: Kubernetes (on-prem-k8s, eu-central-1) for high availability
- Security: HashiCorp Vault for AES-256 encryption and dynamic secrets
- Communication: gRPC and REST APIs secured via JWT and mTLS

## Rationale
This architecture uses hybrid Kubernetes deployment with distributed consensus to achieve 99.99% availability and prevent split-brain race conditions. It enforces multi-layered security and FHIR interoperability to meet rigorous HIPAA/GDPR standards.