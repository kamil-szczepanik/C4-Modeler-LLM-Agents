## Overview
The Clinic Management System is a hybrid cloud platform designed for medium-sized hospitals and clinics to manage patient admissions, electronic medical records, scheduling, and billing. It ensures HIPAA/GDPR compliance, 99.99% availability, and long-term data retention.

## Key Elements
- Frontend Container
- API Gateway
- Core Domain Containers
- Integration / FHIR Adapter Container
- Asynchronous Event Bus
- Shared Configuration & Secret Management Sidecar
- Redis Distributed Rate Limiting Store

## Relationships
- Frontend Container interacts with API Gateway via HTTPS/TLS
- API Gateway connects to Core Domain Containers via gRPC/REST with JWT/MFA
- Core Domain Containers communicate via Asynchronous Event Bus using AMQP (Kafka/RabbitMQ)
- Integration / FHIR Adapter Container connects to external systems using HL7 FHIR over HTTPS
- Shared Configuration & Secret Management Sidecar communicates with Core Domain Containers over local loopback

## Technology Stack
- Kubernetes (on-prem-k8s and eu-central-1): Enables active-active high availability and hybrid deployment.
- AES-256: Secures data at rest for strict HIPAA and GDPR compliance.
- HL7 FHIR: Standardizes interoperability with lab and imaging systems.
- Redis: Manages distributed rate limiting and caching.
- OpenTelemetry: Provides unified system observability.

## Rationale
This architecture uses an active-active hybrid cloud deployment with Kubernetes to achieve 99.99% uptime and low-latency performance. Strict protocol enforcement, encryption, and audit logging ensure full compliance with healthcare regulations.