## Overview
The Clinic Management System is a hybrid cloud platform designed for medium-sized hospitals and clinics to manage patient admissions, electronic medical records (EMR), scheduling, and billing. It ensures high availability (99.99%), strict HIPAA/GDPR compliance, and 10-year data retention.

## Key Elements
- **Users**: Patients, Receptionists, Attending Physicians, Billing Specialists, Clinic Administrators
- **Containers**: Web Application Gateway (NGINX), Core API Service (Node.js/NestJS), EMR Engine (Java/Spring Boot), Billing Worker (Python/Celery), Audit Logging Sidecar
- **Data & Caching**: PostgreSQL cluster with read-replicas, Redis for caching and locking, Kafka message broker
- **External Systems**: Identity Provider, Third-Party Payment Gateways/Clearinghouses, External Laboratory & Imaging Systems

## Relationships
- Users access the system via HTTPS/TLS through the Web Application Gateway (NGINX).
- Internal microservices communicate using gRPC over TLS and mTLS via sidecar proxies.
- External lab and imaging systems integrate via HL7 FHIR REST APIs.
- Core API Service and EMR Engine connect to PostgreSQL and Redis for persistence and caching.
- Billing Worker processes messages via Kafka from the Core API Service.

## Technology Stack
- **Orchestration**: Kubernetes (`on-prem-k8s` and AWS `eu-central-1`) managed via ArgoCD GitOps pipelines for active-active high availability.
- **Backend Services**: Node.js/NestJS (Core API), Java/Spring Boot (EMR Engine), Python/Celery (Billing Worker).
- **Persistence**: PostgreSQL with AES-256 and LUKS encryption for transactional data; Redis for session caching and distributed locking.
- **Integration & Security**: HL7 FHIR for interoperability, gRPC for internal RPC, OAuth2/JWT for RBAC, and TLS 1.3 for transport security.

## Rationale
The hybrid Kubernetes microservices architecture guarantees 99.99% uptime and low-latency performance (<1s P95 EMR load) through active-active deployments and database read-replicas. Strict data isolation, encryption at rest (AES-256/LUKS), and WORM audit logging ensure full compliance with HIPAA and GDPR mandates.