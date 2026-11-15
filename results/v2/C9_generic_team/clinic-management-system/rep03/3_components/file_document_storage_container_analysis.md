## Overview
The Clinic Management System is a hybrid cloud platform designed to manage patient admissions, EMRs, scheduling, and billing for healthcare facilities. It ensures high availability, strict HIPAA/GDPR compliance, and 10-year data retention.

## Key Elements
- Patients, Clinicians, Administrative Staff
- External Identity Providers (IdPs), Third-Party Billing Gateways, HL7 FHIR-Compliant Lab/Imaging Systems
- API Gateway Container (Kubernetes Ingress / Custom Proxy)
- Domain Containers (Microservices / Kubernetes)
- Integration Service Container (Asynchronous Worker)
- Event Bus / Message Broker Container (Apache Kafka or RabbitMQ)
- Caching Container (Redis Enterprise)
- File/Document Storage Container (Object Storage with WORM support)
- Data Archival & Purging Container (Background Worker)
- Observability & Configuration Container (Prometheus, Fluentbit, Secret Manager)

## Relationships
- Patients & Staff interact with API Gateway via HTTPS / TLS 1.3
- Domain Containers communicate via gRPC and Apache Kafka / RabbitMQ
- External Systems connect via HL7 FHIR APIs and HTTPS
- Storage Container interacts with Object Storage using S3 API / Storage Abstraction Layer

## Technology Stack
- Kubernetes / Hybrid Cloud (on-prem-k8s, AWS eu-central-1): Ensures high availability (99.99%) and infrastructure portability.
- Apache Kafka / RabbitMQ: Enables decoupled asynchronous messaging and integration workflows.
- Redis Enterprise: Delivers low-latency caching for rapid EMR screen loads (<1s P95).
- Object Storage with WORM support (MinIO/Ceph / AWS S3): Mandated for secure, immutable 10-year data retention.
- Prometheus & Fluentbit: Provides centralized observability and logging.

## Rationale
This hybrid microservices architecture guarantees 99.99% active-active availability, sub-second EMR performance, and strict HIPAA/GDPR compliance. Decoupling storage and messaging layers ensures long-term interoperability and data integrity.