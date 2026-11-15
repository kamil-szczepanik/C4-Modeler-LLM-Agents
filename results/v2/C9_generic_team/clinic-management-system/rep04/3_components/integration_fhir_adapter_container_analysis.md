## Overview
The Clinic Management System is a clinical IT platform that manages patient admissions, electronic medical records, scheduling, and billing for medium-sized hospitals and clinics. It ensures HIPAA and GDPR compliance with 99.99% high availability.

## Key Elements
- Frontend Container
- API Gateway
- Core Domain Containers
- Integration / FHIR Adapter Container
- Asynchronous Event Bus
- Audit Logging & Compliance Container
- Observability Container
- Redis Distributed Rate Limiting Store
- External Lab and Imaging Systems

## Relationships
- Frontend Container -> API Gateway (HTTPS/TLS)
- API Gateway -> Core Domain Containers (gRPC/REST, JWT/MFA)
- Core Domain Containers <-> Asynchronous Event Bus (AMQP)
- Integration / FHIR Adapter Container -> External Lab and Imaging Systems (HL7 FHIR over HTTPS)
- Integration / FHIR Adapter Container <-> Redis Distributed Rate Limiting Store (TCP)

## Technology Stack
- Kubernetes: Hybrid deployment across on-premise clusters and AWS eu-central-1 for high availability
- HL7 FHIR: Standardized protocol for external lab and imaging interoperability
- gRPC & REST: Internal microservices communication
- Redis: Distributed rate limiting, idempotency caching, and caching proxy layer
- Kafka/RabbitMQ: Asynchronous event bus messaging
- OpenTelemetry: End-to-end distributed tracing and observability

## Rationale
The hybrid architecture utilizes Kubernetes and active-active replication to meet the 99.99% availability and high-performance requirements. Implementing an Anti-Corruption Layer with HL7 FHIR standards ensures strict interoperability and regulatory compliance for healthcare workflows.