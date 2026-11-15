## Overview
The Clinic Management System is a hybrid cloud platform designed to manage patient admissions, electronic medical records, scheduling, and billing for medium-sized healthcare facilities. It ensures high availability, strict security compliance, and robust interoperability for clinical operations.

## Key Elements
- Patients, Receptionists, Clinicians, Billing Specialists, and Hospital Administrators
- WAF Container (Web Application Firewall)
- API Gateway (Kubernetes Ingress / Gateway API)
- Patient Portal Container (Web / Mobile Frontend)
- EMR Container, Scheduling Container, Billing Container, Notification Container, Analytics & Reporting Container
- PostgreSQL Databases (Patroni/etcd), Event Broker (Apache Kafka / RabbitMQ), Immutable Audit Storage Sink, HashiCorp Vault

## Relationships
- API Gateway -> Patient Portal Container: Routes client requests via HTTPS and mTLS (SPIFFE/SPIRE)
- Patient Portal Container -> API Gateway: Communicates using REST and gRPC over mTLS
- API Gateway -> WAF Container: Inspects inbound traffic via HTTPS
- Patient Portal Container -> PostgreSQL Databases: Persists data via encrypted connections (AES-256)

## Technology Stack
- Hybrid Kubernetes (`on-prem-k8s` and AWS `eu-central-1`) for high availability and workload portability
- PostgreSQL with Patroni/etcd for clustered, fault-tolerant relational data storage
- Apache Kafka / RabbitMQ for event-driven asynchronous messaging
- HashiCorp Vault for secrets management and AES-256 encryption keys
- HL7 FHIR APIs for standardized healthcare data interoperability

## Rationale
This architecture uses active-active hybrid Kubernetes deployment patterns to guarantee the mandated 99.99% uptime and low-latency performance. Strict adherence to OAuth 2.0, mTLS, and encrypted storage fulfills rigorous HIPAA and GDPR compliance requirements.