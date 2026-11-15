## Overview
The Clinic Management System is a hybrid cloud platform designed to manage patient admissions, electronic medical records (EMR), scheduling, and billing for medium-sized hospitals and clinics. It ensures high availability, strict compliance, and rapid clinical workflows.

## Key Elements
- Patients, Clinicians, Receptionists, Billing Specialists, Auditors, and Executives
- Frontend Container (React, TypeScript, Nginx/CDN)
- Edge Container (Kong / Envoy API Gateway with Authentication, Rate Limiting, and Telemetry plugins)
- Clinical Service, Scheduling Service, Billing Service, Audit Log Service, and Integration Service (Go, Node.js, Java Spring Boot)
- Apache Kafka / RabbitMQ Event Bus
- PostgreSQL, MongoDB, Redis, and Encrypted S3-compatible Object Storage
- External Identity Provider (IdP), Payment Gateway, and Lab/Imaging Systems

## Relationships
- Frontend Container -> Edge Container: API requests [HTTPS / JSON]
- Edge Container -> Internal Services: Internal routing [gRPC and REST over mTLS]
- Edge Container -> Identity Provider: User authentication [OAuth 2.0 / OIDC with MFA]
- Integration Service -> Lab & Imaging Systems: Interoperability [HL7 FHIR APIs]

## Technology Stack
- Kong / Envoy: API gateway and edge routing for high performance and security
- Redis: Tenant-aware rate limiting and token validation cache with L2 fallback
- Go, Java Spring Boot, Node.js: Microservices backend implementation
- Kubernetes (on-prem-k8s) & AWS (eu-central-1): Hybrid cloud infrastructure
- Prometheus: Telemetry and observability metrics monitoring

## Rationale
This architecture uses a hybrid cloud deployment with active-active edge routing to meet stringent 99.99% availability and 1-second EMR load time requirements. Centralized mTLS routing and robust encryption satisfy HIPAA and GDPR compliance mandates.