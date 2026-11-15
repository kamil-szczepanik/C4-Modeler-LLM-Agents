## Overview
[The Clinic Management System manages patient admissions, EMR, scheduling, and billing for medium-sized hospitals and clinics. It delivers a HIPAA and GDPR-compliant, highly available hybrid cloud architecture.]

## Key Elements
[
- Hospital Staff (User)
- Web Application Frontend (React SPA, Nginx Container)
- API Gateway & Edge Router (Kong/Envoy)
- Microservices (Patient, Scheduling, EMR, Billing Services via Spring Boot/Kubernetes)
- Data Persistence Layer (PostgreSQL with AES-256 and HSM-managed column encryption)
- Message Broker Container (Geo-local Apache Kafka clusters with MirrorMaker)
- External Systems (Patient Portal, External Lab & Imaging Systems, Insurance Clearinghouses, Identity Provider, Regulatory Audit System)
]

## Relationships
[
- Hospital Staff -> Web Application Frontend: Accesses system functionality [HTTPS]
- Web Application Frontend -> API Gateway & Edge Router: Routes frontend requests [REST/JSON over HTTPS]
- Microservices -> Data Persistence Layer: Reads and writes encrypted data [JDBC/TLS]
- Microservices -> Message Broker Container: Publishes and consumes domain events [Kafka Protocol/TLS]
]

## Technology Stack
[
- Frontend: React SPA served via Nginx for decoupled delivery and performance.
- Backend Services: Spring Boot on Kubernetes for scalable microservices.
- Database: PostgreSQL with AES-256 and HSM-managed encryption for data security at rest.
- Messaging: Apache Kafka with MirrorMaker for geo-distributed, real-time event streaming.
- Infrastructure: Hybrid cloud (on-premise Kubernetes and AWS eu-central-1) ensuring 99.99% availability.
]

## Rationale
[This architecture uses a hybrid Kubernetes deployment with active-active replication to satisfy strict 99.99% uptime availability requirements. Microservices combined with AES-256 database encryption ensure compliance with HIPAA/GDPR data protection and long-term retention mandates.]