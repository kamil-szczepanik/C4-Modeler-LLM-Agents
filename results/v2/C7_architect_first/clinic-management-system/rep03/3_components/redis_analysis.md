## Overview
The Clinic Management System is a hybrid cloud platform designed for medium-sized hospitals and clinics to manage patient admissions, EMRs, scheduling, and billing. It provides high availability, stringent security, and clinical efficiency to meet strict healthcare regulations.

## Key Elements
- Users: Doctors, Nurses, Receptionists, Billing Staff, Clinic Administrators, Patients
- External Systems: Identity Provider (IdP), External Labs & Imaging Systems, Payment Gateway / Insurance Clearinghouse
- Containers: API Gateway (Nginx / Kong), Web Application (React / TypeScript, Nginx), Core Services (Node.js / NestJS / Spring Boot), PostgreSQL (Active-Passive), Redis Cluster, Apache Kafka, AWS S3 Object Lock
- Redis Components: Redis Cluster Coordinator / Proxy, In-Memory Data Store, Persistence Engine

## Relationships
- Web Application -> API Gateway: HTTPS / REST / WebSockets
- API Gateway -> Core Services: gRPC / HTTP
- Core Services -> PostgreSQL: PostgreSQL Wire Protocol (TCP)
- Core Services -> Redis Cluster Coordinator: Redis Protocol over mTLS (TCP)
- Core Services -> Apache Kafka: Kafka Protocol (TCP)
- Core Services -> AWS S3 Object Lock: HTTPS / S3 API
- Core Services -> External Systems: HL7 FHIR APIs / HTTPS

## Technology Stack
- Frontend: React / TypeScript on Nginx for responsive client-side rendering
- Backend Core Services: Node.js / NestJS or Java / Spring Boot for scalable business logic
- Database: PostgreSQL with active-passive replication for relational data integrity
- Caching: Redis Cluster with mTLS and AES-256 encrypted persistence for low-latency EMR access
- Messaging: Apache Kafka for event-driven asynchronous processing
- Storage: AWS S3 Object Lock for immutable 10-year data retention
- Infrastructure: Hybrid Kubernetes (`on-prem-k8s` and AWS `eu-central-1`)

## Rationale
This hybrid architecture guarantees 99.99% uptime and sub-second EMR performance across distributed clinical environments. It ensures rigorous HIPAA and GDPR compliance through end-to-end encryption, mTLS, and immutable audit logs.