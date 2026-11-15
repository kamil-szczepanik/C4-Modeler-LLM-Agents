## Overview
The Clinic Management System is a hybrid cloud platform designed to manage patient admissions, electronic medical records (EMR), scheduling, and billing for medium-sized healthcare facilities. It ensures high availability, strict HIPAA/GDPR compliance, and sub-second performance for clinical workflows.

## Key Elements
- Patients, Clinicians, Receptionists, Billing Specialists, Hospital Administrators
- External Lab & Imaging Systems, Payment Gateway / Insurance Clearinghouse, Identity Provider (IdP)
- API Gateway (Nginx / Envoy), Patient Web/Mobile App (React / Flutter), Clinical Workstation App (Angular / Electron)
- Core Services Container (Java / Spring Boot), Integration Service (Node.js / Apache Camel), Notification Container (Python / Celery), Reporting & Analytics Container (Analytics Platform)
- Redis Master/Replica Cluster (in-memory data store for caching and scheduling locks)
- PostgreSQL (OLTP with AES-256), ClickHouse (OLAP), Apache Kafka

## Relationships
- Patient Web/Mobile App & Clinical Workstation App -> API Gateway: Client requests [HTTPS / WSS]
- API Gateway -> Core Services Container: Routes internal traffic [gRPC / REST]
- Core Services Container -> PostgreSQL: Persists transactional data [PostgreSQL Wire Protocol over TLS]
- Core Services Container -> Redis: Manages scheduling locks and transient caching [Redis Protocol over mTLS with TLS]
- Core Services Container -> Apache Kafka: Streams clinical and audit events [Kafka Protocol]
- Integration Service -> External Lab & Imaging Systems: Interoperates using HL7 FHIR APIs [HTTPS]

## Technology Stack
- Kubernetes (on-prem-k8s and AWS eu-central-1): Hybrid cloud orchestration ensuring 99.99% high availability.
- Java / Spring Boot: Core business logic and EMR processing.
- PostgreSQL & ClickHouse: Relational OLTP storage and analytical OLAP workloads.
- Redis (Redis Operator): Ephemeral caching and distributed scheduling locks with `volatile-lru` eviction.
- Apache Kafka: Durable event streaming for critical clinical alerts and notifications.
- AES-256 & mTLS: Data-at-rest encryption for persistence files (RDB/AOF) and secure in-flight transport.

## Rationale
This hybrid microservices architecture meets the 99.99% availability requirement through active-active Kubernetes clusters and automated failover mechanisms like Redis Sentinel. Strict adherence to HIPAA and GDPR is enforced via AES-256 encryption, mTLS, Redis ACLs, and dedicated audit trails.