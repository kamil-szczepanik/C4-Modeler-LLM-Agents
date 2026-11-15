## Overview
The Clinic Management System manages patient admissions, EMRs, scheduling, and billing for healthcare providers. It operates in a hybrid cloud environment requiring strict HIPAA/GDPR compliance and 99.99% availability.

## Key Elements
- Users: Patients, Clinicians, and Staff
- API Gateway / Reverse Proxy: Envoy
- Service Mesh: Istio
- Microservices: Patient & Scheduling Service, EMR Core Service, Billing & Integration Service
- Data & Storage: PostgreSQL with Patroni, NATS / RabbitMQ, AWS Kafka, WORM-compliant S3 / MinIO
- Security: HashiCorp Vault
- External Systems: External Lab & Imaging Systems, Payment Gateway / Insurance Clearinghouse

## Relationships
- Patients & Clinicians -> Envoy: Clients access API Gateway via HTTPS / JSON
- Envoy -> Patient & Scheduling Service: Routes requests via gRPC over Istio mTLS
- Envoy -> EMR Core Service: Routes requests via gRPC over Istio mTLS
- Envoy -> Billing & Integration Service: Routes requests via gRPC over Istio mTLS

## Technology Stack
- Node.js/Go: Chosen for Patient & Scheduling Service due to concurrent request handling
- Java/Spring Boot: Chosen for EMR Core Service for enterprise reliability
- Python/FastAPI: Chosen for Billing & Integration Service for rapid API development
- PostgreSQL with Patroni: Chosen for high availability relational data storage
- AWS Kafka & RabbitMQ/NATS: Chosen for event-driven messaging and streaming
- HashiCorp Vault: Chosen for secure secret management and encryption keys

## Rationale
This architecture uses microservices and an active-active hybrid deployment to achieve 99.99% uptime and low latency. Strict encryption and WORM storage ensure compliance with HIPAA and GDPR regulations.