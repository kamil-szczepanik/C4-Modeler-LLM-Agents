## Overview
The Clinic Management System is a hybrid-cloud healthcare platform designed to manage patient admissions, electronic medical records, scheduling, and billing for medium-sized clinics. Its core purpose is to deliver high-availability clinical operations while strictly adhering to HIPAA and GDPR compliance mandates.

## Key Elements
- React Single Page Application (SPA)
- NGINX / Kong API Gateway
- Go EMR Service
- Node.js Scheduling Service
- Apache Camel ESB & Apache Kafka Event Bus
- PostgreSQL Cluster & Redis Cluster (Redis Sentinel, TLS)
- Third-Party Payment Gateways & External Insurance Systems

## Relationships
- React SPA -> API Gateway: HTTPS / REST for client requests
- API Gateway -> Go EMR Service: gRPC for internal medical records processing
- API Gateway -> Node.js Scheduling Service: REST for appointment management
- Node.js Scheduling Service -> Redis Cluster: TCP with TLS (ioredis) for distributed slot locking
- Apache Camel ESB -> External Lab Systems: HL7 FHIR APIs for interoperability

## Technology Stack
- Frontend: React with CDN distribution for fast user interface delivery
- Backend Services: Go for high-performance EMR operations; Node.js for scheduling logic
- Messaging & Integration: Apache Kafka for event streaming; Apache Camel for HL7 FHIR integration
- Databases & Caching: PostgreSQL Cluster with read replicas; Redis Cluster with Redis Sentinel for real-time locking
- Security: OAuth2, MFA, AES-256 storage encryption, and mTLS for data protection

## Rationale
The hybrid architecture utilizes on-premises Kubernetes and AWS eu-central-1 to meet strict data residency and 99.99% availability requirements. Redis clustering and PostgreSQL read replicas ensure sub-second performance for critical EMR and scheduling workflows under heavy clinical loads.