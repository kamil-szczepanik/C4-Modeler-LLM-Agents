## Overview
The Clinic Management System is a hybrid cloud platform designed to securely manage patient admissions, EMRs, scheduling, and billing for healthcare clinics. It ensures strict HIPAA/GDPR compliance, 99.99% availability, and high-performance clinical workflows.

## Key Elements
- Hospital Staff and Patients (Users)
- External Lab and Imaging Systems (External Systems)
- Frontend Container
- API Gateway
- Core Domain Containers
- Integration / FHIR Adapter Container
- Asynchronous Event Bus
- Audit Logging & Compliance Container
- Observability Container
- Redis Distributed Rate Limiting Store

## Relationships
- Frontend Container -> API Gateway: Sends requests via HTTPS with JWT/MFA validation
- API Gateway -> Core Domain Containers: Routes requests using internal gRPC/REST
- Integration / FHIR Adapter Container -> External Systems: Connects via HL7 FHIR APIs over HTTPS
- Core Domain Containers -> Asynchronous Event Bus: Publishes and consumes messages via AMQP

## Technology Stack
- Kubernetes (on-prem-k8s and AWS eu-central-1): Hybrid cloud orchestration ensuring high availability (99.99%).
- gRPC & REST: Internal and external communication protocols for low-latency performance.
- HL7 FHIR: Interoperability standard for lab and imaging system integration.
- Redis: Distributed rate limiting store for edge throttling.
- OpenTelemetry: Distributed tracing and observability across hybrid clusters.

## Rationale
This hybrid architecture combines on-premise Kubernetes clusters with cloud infrastructure to satisfy strict data residency regulations and data retention policies. Decoupling core domain services from edge concerns via an API Gateway guarantees the required 99.99% availability and high-performance EMR delivery.