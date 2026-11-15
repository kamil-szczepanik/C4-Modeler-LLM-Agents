## Overview
The Clinic Management System manages patient admissions, electronic medical records, scheduling, and billing for medium-sized hospitals and clinics. It ensures high availability, strict HIPAA/GDPR compliance, and interoperability across hybrid cloud infrastructure.

## Key Elements
- Users: Front Desk Administrator, Clinician, Billing Specialist, Patient
- Containers: Patient Registration, Appointment Scheduling, EMR, Billing & Claims, HL7 FHIR Interoperability, Patient Portal
- External Systems: External Lab & Imaging Systems
- Infrastructure: Kubernetes (on-premise and AWS `eu-central-1`), Kafka/RabbitMQ message brokers, API Gateway, WAF

## Relationships
- HL7 FHIR Interoperability -> External Lab & Imaging Systems: Exchanges lab and imaging data [HL7 FHIR APIs over mTLS, TLS 1.3]
- HL7 FHIR Interoperability -> EMR: Ingests lab and imaging results [gRPC / REST via mTLS]
- Patient Portal / Clients -> Patient Registration & Scheduling: Manages admissions and appointments [HTTPS / REST API]

## Technology Stack
- Orchestration: Kubernetes for containerized microservices across hybrid environments
- Protocols: HL7 FHIR APIs, gRPC, REST, TLS 1.3, mTLS for secure communication
- Security: OAuth 2.0 with SMART-on-FHIR, JWKS token validation, AES-256 for data at rest, WAF with OWASP CRS
- Messaging & Storage: Kafka/RabbitMQ for asynchronous ingestion, Encrypted Distributed Storage for 10+ year data retention
- Observability: OpenTelemetry for distributed tracing and immutable audit logging

## Rationale
This architecture uses a hybrid Kubernetes deployment with active-active high availability (99.99% uptime) to meet strict clinical demands. Robust security controls like mTLS, SMART-on-FHIR, and AES-256 ensure full HIPAA and GDPR compliance without compromising sub-second performance.