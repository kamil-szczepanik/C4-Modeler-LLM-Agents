## Overview
The Clinic Management System is a hybrid cloud platform designed for medium-sized hospitals and clinics to manage patient admissions, electronic medical records, scheduling, and billing. It provides high availability, secure clinical workflows, and strict compliance with HIPAA and GDPR data mandates.

## Key Elements
- Front Desk Administrator
- Clinician
- Billing Specialist
- Patient
- External Lab & Imaging Systems
- Patient Registration (Kubernetes container, REST API)
- Appointment Scheduling (Kubernetes container, REST API)
- EMR (Kubernetes container, Encrypted Distributed Storage)
- Billing & Claims (Kubernetes container, Encrypted Distributed Storage)
- HL7 FHIR Interoperability (Kubernetes container, HL7 FHIR APIs)
- Patient Portal (Kubernetes container, REST API)

## Relationships
- Front Desk Administrator -> Patient Registration: Accesses via web interface for admissions [HTTPS (TLS 1.3), OAuth2/OIDC MFA]
- Patient Registration -> EMR: Creates and updates patient records [gRPC / REST via mTLS]
- Patient Portal -> Patient Registration: Submits self-service intake and demographics [HTTPS (TLS 1.3), OAuth2/OIDC]
- EMR -> External Lab & Imaging Systems: Exchanges clinical data [HL7 FHIR APIs via mTLS]

## Technology Stack
- Kubernetes (on-prem-k8s and AWS eu-central-1): Deploys stateless container replicas for active-active high availability (99.99% uptime).
- REST & gRPC: Enables synchronous internal and external service communication with TLS 1.3 and mTLS security.
- HL7 FHIR APIs: Standardizes interoperability with external laboratory and imaging systems.
- AES-256: Enforces field-level and at-rest encryption for PII/PHI to meet HIPAA and GDPR requirements.
- Prometheus & OpenTelemetry: Powers metrics collection, admission latency tracking, and distributed tracing across hybrid infrastructure boundaries.

## Rationale
This architecture combines active-active Kubernetes clusters across hybrid environments to ensure 99.99% uptime and disaster recovery for mission-critical clinical workflows. Strict zero-trust security boundaries, mTLS, and AES-256 encryption satisfy stringent HIPAA and GDPR compliance requirements while supporting sub-second P95 performance targets.