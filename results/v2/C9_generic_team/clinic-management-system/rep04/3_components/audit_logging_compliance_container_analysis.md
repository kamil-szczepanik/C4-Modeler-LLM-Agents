## Overview
The Clinic Management System is a hybrid cloud platform designed for medium-sized hospitals and clinics to manage patient admissions, electronic medical records, scheduling, and billing. It ensures high availability (99.99%) and strict HIPAA/GDPR compliance with a 10-year data retention mandate.

## Key Elements
- **Users**: Hospital Staff and Patients
- **External Systems**: External Lab and Imaging Systems
- **Containers**: Frontend Container, API Gateway, Core Domain Containers, Integration / FHIR Adapter Container, Asynchronous Event Bus (Kafka/RabbitMQ), Audit Logging & Compliance Container, Observability Container, Shared Configuration & Secret Management Sidecar, Database Migration Container, Data Archival Worker, Redis Distributed Rate Limiting Store

## Relationships
- **Users to Frontend Container**: Interacts via HTTPS/TLS
- **Frontend Container to API Gateway**: Communicates via HTTPS with JWT/MFA authentication
- **API Gateway to Core Domain Containers**: Routes requests via gRPC/REST over Kubernetes internal network
- **Core Domain Containers to Asynchronous Event Bus**: Publishes events via AMQP (Kafka/RabbitMQ)
- **Integration / FHIR Adapter Container to External Systems**: Connects using HL7 FHIR APIs via HTTPS

## Technology Stack
- **Compute**: Kubernetes (on-prem-k8s and AWS eu-central-1) for active-active high availability
- **Security & Compliance**: AES-256 encryption at rest, WORM storage (AWS S3 Object Lock) for audit logs, and JWT/MFA for access control
- **Interoperability**: HL7 FHIR APIs for integration with external lab and imaging systems
- **Caching & Rate Limiting**: Redis distributed rate limiting store

## Rationale
The hybrid cloud Kubernetes architecture provides the 99.99% uptime and active-active scaling required for continuous clinical operations. Furthermore, WORM storage and AES-256 encryption directly satisfy rigorous HIPAA and GDPR 10-year data retention and tamper-resistance mandates.