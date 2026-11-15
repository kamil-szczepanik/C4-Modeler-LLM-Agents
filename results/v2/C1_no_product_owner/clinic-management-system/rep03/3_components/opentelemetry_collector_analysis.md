## Overview
[The Clinic Management System manages patient admissions, EMRs, scheduling, and billing for medium-sized hospitals and clinics. It ensures high availability, HIPAA/GDPR compliance, and interoperability via FHIR APIs across a hybrid cloud infrastructure.]

## Key Elements
- Patients, Clinicians, Receptionists, Billing Specialists
- Third-Party Payment Gateway, External Lab & Imaging Systems, Insurance Clearinghouse, Enterprise IdP
- API Gateway (Traefik/NGINX), EMR Service, Patient & Scheduling Service, Billing & Claims Service, FHIR Interoperability Service
- CockroachDB, RabbitMQ, HashiCorp Vault, ArgoCD / Helm, OpenTelemetry Collector

## Relationships
- Microservices -> API Gateway: Client requests routed via HTTPS/gRPC
- Microservices -> CockroachDB: Transactional persistence via PostgreSQL wire protocol
- Microservices -> RabbitMQ: Asynchronous messaging via AMQP
- Backend Services -> OpenTelemetry Collector: Telemetry transmission via OTLP/gRPC with mTLS
- FHIR Interoperability Service -> External Lab & Imaging Systems: HL7 FHIR APIs over HTTPS

## Technology Stack
- Node.js / TypeScript (Fastify): High-performance microservice development
- Java / Spring Boot: Robust enterprise billing and claims processing
- .NET: FHIR interoperability standards compliance
- CockroachDB: Distributed, resilient SQL database meeting 99.99% uptime and data retention needs
- OpenTelemetry Collector: Unified metrics, traces, and logs pipeline with built-in PII/PHI redaction
- HashiCorp Vault: Secure secrets management for HIPAA/GDPR compliance
- Kubernetes (On-prem & AWS eu-central-1): Hybrid cloud orchestration platform

## Rationale
[This hybrid cloud architecture leverages distributed SQL and active-active clustering to meet stringent 99.99% availability and 10-year data retention mandates. Strict security patterns, including mTLS, AES-256, and automated PII/PHI redaction, ensure continuous HIPAA and GDPR compliance.]