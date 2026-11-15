## Overview
The Clinic Management System manages patient admissions, electronic medical records, scheduling, and billing for medium-sized hospitals and clinics. It delivers high availability and regulatory compliance across hybrid cloud environments.

## Key Elements
- API Gateway (NGINX/Kong)
- Patient Registration Service (Microservice)
- EMR Service (Microservice)
- Scheduling Service (Microservice)
- Billing Service (Microservice)
- PostgreSQL Database & Redis Caching Layer
- Persistent Message Queues with Dead-Letter Routing

## Relationships
- API Gateway -> Patient Registration Service via REST/gRPC over TLS 1.3
- Patient Registration Service -> PostgreSQL via JDBC/TLS
- Patient Registration Service -> Message Brokers via AMQP/TCP
- External Labs/Imaging Systems -> EMR Service via HL7 FHIR APIs

## Technology Stack
- Kubernetes (Hybrid: on-premises and AWS eu-central-1) for container orchestration and active-active high availability
- PostgreSQL with AES-256 encryption at rest for transactional data storage meeting 10-year retention rules
- Redis for distributed caching and session management
- OpenTelemetry and structured JSON logging for distributed tracing and observability
- OpenAPI and Protocol Buffers for contract-first API design

## Rationale
The hybrid architecture utilizes Kubernetes and active-active deployments to guarantee the 99.99% uptime requirement. Microservices with Domain-Driven Design and CQRS ensure scalability, strict HIPAA/GDPR compliance, and sub-second performance.