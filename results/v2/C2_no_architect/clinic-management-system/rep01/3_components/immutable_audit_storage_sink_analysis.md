## Overview
The Clinic Management System is a hybrid cloud platform designed for medium-sized hospitals to handle patient admissions, electronic medical records (EMR), scheduling, and billing. It provides high availability, stringent regulatory compliance, and secure data retention.

## Key Elements
- Patients, Receptionists, Clinicians, Billing Specialists, Hospital Administrators, Compliance Officers, Risk Managers
- Web Application Firewall (WAF Container) & API Gateway (Kubernetes Ingress / Gateway API)
- Frontend (Patient Portal Container) & Microservices (EMR, Scheduling, Billing, Notification, Analytics & Reporting Containers)
- Data & Security Infrastructure: PostgreSQL (Patroni/etcd), Apache Kafka / RabbitMQ Event Broker, HashiCorp Vault
- Compliance Infrastructure: Immutable Audit Storage Sink with S3 Object Lock and Compliance Reporting Dashboard

## Relationships
- Users access the system via HTTPS/TLS through the API Gateway and WAF Container
- Frontend and microservices communicate internally using REST and gRPC protocols
- Analytics & Reporting Container writes compliance records to the Immutable Audit Storage Sink via mTLS (SPIFFE/SPIRE)
- Compliance Officers query the Immutable Audit Storage Sink via the Compliance Reporting Dashboard using ephemeral HashiCorp Vault read-only credentials

## Technology Stack
- Kubernetes (`on-prem-k8s` and `eu-central-1`) for container orchestration across hybrid infrastructure
- PostgreSQL with Patroni and etcd for resilient, high-availability relational data storage
- Apache Kafka / RabbitMQ for event-driven asynchronous messaging and pipeline backpressure
- AWS S3 Object Lock (Standard-IA) and on-premise MinIO for 10-year WORM data retention
- HashiCorp Vault for dynamic credentials, SPIFFE/SPIRE for mTLS, and client-side envelope encryption (AES-256)

## Rationale
This architecture uses hybrid Kubernetes deployment and active-active patterns to guarantee 99.99% availability and meet strict 1-second EMR performance SLAs. Client-side envelope encryption, WORM storage, and strict tokenization ensure comprehensive HIPAA and GDPR compliance with zero-knowledge data protection.