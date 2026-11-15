## Overview
The Clinic Management System is a hybrid cloud platform managing patient admissions, EMRs, scheduling, and billing for clinics while ensuring HIPAA and GDPR compliance. It provides high-availability clinical workflows and consumer-grade patient access.

## Key Elements
- Patients & Clinical Staff (Receptionists, Physicians, Billing Specialists)
- API Gateway (Kong / Node.js)
- Patient Portal BFF (Node.js / GraphQL, Apollo Server, Redis)
- Patient & Scheduling Service (Go)
- EMR Core Service (Spring Boot)
- Billing & Integration Service (FastAPI)
- Databases & Brokers: PostgreSQL (AES-256), RabbitMQ
- External Systems: Enterprise IdP, External Lab & Imaging Systems, Payment Gateway, Audit Archival / SIEM

## Relationships
- Patient -> Patient Portal BFF: Views health records and schedules appointments [HTTPS/REST]
- API Gateway -> Patient Portal BFF: Routes patient portal traffic [HTTPS]
- Patient Portal BFF -> Patient & Scheduling Service: Fetches scheduling data [gRPC over mTLS]
- Patient Portal BFF -> EMR Core Service: Fetches medical records [gRPC over mTLS]
- Audit Event Emitter -> Audit Archival / SIEM System: Streams audit logs [HTTPS/REST or AMQP]

## Technology Stack
- Node.js & GraphQL (Apollo Server): Powers the Patient Portal BFF for efficient, tailored data payloads
- Redis: Caches read-heavy static clinical data with AES-256 encryption at rest
- PostgreSQL: Provides persistent storage secured with AES-256 encryption at rest
- gRPC over mTLS: Secures high-performance internal service-to-service communication
- Kubernetes: Orchestrates services across on-premise clusters and AWS eu-central-1

## Rationale
This architecture uses a BFF pattern and gRPC to meet sub-second EMR load times while isolating security controls. Hybrid cloud deployment and active-active replication ensure 99.99% availability and rigorous regulatory compliance.