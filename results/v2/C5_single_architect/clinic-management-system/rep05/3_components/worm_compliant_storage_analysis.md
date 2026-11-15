## Overview
The Clinic Management System is a clinical IT platform managing patient admissions, EMRs, scheduling, and billing. It features a hybrid cloud, active-active architecture ensuring high availability and regulatory compliance.

## Key Elements
- Users: Doctors, Nurses, Receptionists, Billing Specialists
- External Systems: Lab & Imaging Systems, Payment Gateway/Insurance Clearinghouse, Enterprise Identity Provider, Notification Service
- Containers: React Frontend, Kong API Gateway, Java/Node.js Core Services, EMR & Audit Service, Billing Worker, Apache Kafka/RabbitMQ, PostgreSQL DB
- WORM Storage Components: Ingestion & Validation Engine, Object Lock Manager, Encryption & Key Service, MinIO (On-Prem), AWS S3 (Cloud)

## Relationships
- Frontend -> API Gateway: HTTPS / TLS 1.3
- API Gateway -> Core Services: gRPC / REST
- EMR & Audit Service -> WORM Ingestion Engine: gRPC over TLS
- WORM Object Lock Manager -> MinIO / AWS S3: S3 API over TLS 1.3
- WORM Encryption Service -> Enterprise HSM/KMS: PKCS#11 / AWS KMS API

## Technology Stack
- Frontend: React / TypeScript served via CDN/Nginx
- Backend Services: Java Spring Boot and Node.js
- Database & Messaging: PostgreSQL with AES-256 and Apache Kafka/RabbitMQ
- Storage & Security: MinIO, AWS S3 with Object Lock, AES-256 encryption

## Rationale
This architecture uses active-active multi-region replication and WORM storage to meet 99.99% availability and 10-year data retention. Hybrid deployment ensures strict HIPAA and GDPR compliance across on-premise and cloud environments.