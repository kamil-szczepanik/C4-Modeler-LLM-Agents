## Overview
The Clinic Management System is a hybrid cloud platform designed to manage patient admissions, electronic medical records (EMR), scheduling, and billing for medium-sized clinics. It ensures strict HIPAA/GDPR compliance, 99.99% uptime, and sub-second EMR response times.

## Key Elements
- **Users**: Patient, Clinician, Receptionist/Admin, Billing Specialist, Compliance Auditor
- **External Systems**: Patient Portal App, Identity Provider (IdP), External Lab & Imaging Systems, Payment Gateway / Insurance Clearinghouse
- **Containers**: API Gateway, EMR Service, Appointment Service, Billing Container, Audit & Compliance Container, HL7 FHIR Interoperability Service
- **Data & Infrastructure**: PostgreSQL (with Redis caching), Apache Kafka, OpenTelemetry sidecars

## Relationships
- **API Gateway**: Interacts with Users and Patient Portal App via HTTPS/REST/gRPC with TLS termination and JWT validation.
- **EMR & Appointment Services**: Communicate with API Gateway and PostgreSQL over HTTPS/gRPC and mTLS.
- **Apache Kafka**: Asynchronously decouples EMR from Audit & Compliance and HL7 FHIR Interoperability services.
- **HL7 FHIR Service**: Connects to External Lab & Imaging Systems via HL7 FHIR APIs.
- **Billing Container**: Integrates securely with Payment Gateway / Insurance Clearinghouse via TLS 1.3.

## Technology Stack
- **API Gateway**: NGINX / Kong for rate limiting, JWT validation, and canary deployments.
- **Backend Services**: Node.js / Go for core EMR/Appointment services; Python / FastAPI for HL7 FHIR service.
- **Messaging & Caching**: Apache Kafka for async event streaming; Redis for high-performance EMR caching.
- **Databases & Security**: PostgreSQL with AES-256 envelope encryption; mTLS for all internal communication; Cosign/Sigstore for container signing.
- **Infrastructure**: Kubernetes (`on-prem-k8s` and `eu-central-1` hybrid cloud) with OpenTelemetry observability.

## Rationale
The hybrid architecture prioritizes local on-premise execution for critical clinical containers to maintain uninterrupted patient care during network partitions. A single-primary PostgreSQL write model with asynchronous replication prevents split-brain corruption while meeting strict data retention and security regulations.