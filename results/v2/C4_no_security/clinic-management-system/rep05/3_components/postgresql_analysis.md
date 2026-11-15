## Overview
The Clinic Management System is a hybrid cloud clinical IT platform designed to manage patient admissions, electronic medical records, appointment scheduling, and billing for medium-sized hospitals and clinics. It ensures high availability, strict regulatory compliance (HIPAA and GDPR), and rapid performance for clinical workflows.

## Key Elements
- **Users:** Receptionists, Clinicians, Billing Specialists, Compliance Officers, Patients
- **External Systems:** Lab & Imaging Systems, Insurance Clearinghouses, Enterprise Identity Provider, Patient Portal
- **Containers:** SPA Frontend, EMR Core Service, Billing & Claims Service, Audit & Compliance Service, Integration Gateway, PostgreSQL Database, Redis Cluster, Apache Kafka
- **Database Components:** Connection Pooler (PgBouncer), Database Engine (PostgreSQL 16), HA & Failover Manager (Patroni with etcd), Audit Logging Extension (pgAudit), Partitioning & Retention Manager

## Relationships
- **SPA Frontend -> Integration Gateway:** Routes HTTPS client requests [REST/JSON over TLS 1.3]
- **Integration Gateway -> EMR Core Service:** Forwards clinical requests [gRPC / REST]
- **EMR Core Service -> PostgreSQL Database:** Reads/writes relational records [TCP with AES-256]
- **Billing & Claims Service -> PostgreSQL Database:** Manages billing data [TCP with AES-256]
- **Audit & Compliance Service -> PostgreSQL Database:** Stores compliance audit logs [TCP with AES-256]
- **Integration Gateway -> External Lab & Imaging Systems:** Exchanges clinical data [HL7 FHIR REST APIs]

## Technology Stack
- **Frontend:** React, TypeScript, Nginx for fast responsive SPA delivery
- **Backend Services:** Spring Boot, Java for robust enterprise clinical microservices
- **Database:** PostgreSQL 16 with Patroni (etcd), PgBouncer, and pgAudit for high availability and security
- **Caching & Messaging:** Redis Cluster for session caching; Apache Kafka for event streaming
- **Infrastructure:** Hybrid Kubernetes (`on-prem-k8s` and AWS `eu-central-1`) with NVMe storage

## Rationale
This architecture uses active-active hybrid Kubernetes deployment and Patroni-managed PostgreSQL to meet 99.99% availability and RPO=0 requirements. Declarative partitioning, PgBouncer pooling, and encrypted storage guarantee sub-second EMR load times while satisfying HIPAA/GDPR 10-year data retention mandates.