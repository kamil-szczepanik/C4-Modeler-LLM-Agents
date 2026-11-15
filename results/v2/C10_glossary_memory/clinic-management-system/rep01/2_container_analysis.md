## Overview
The Clinic Management System (CMS) manages patient admissions, electronic medical records, scheduling, and billing for medium-sized hospitals and clinics. It ensures strict HIPAA/GDPR compliance, 10-year data retention, and 99.99% availability across a hybrid cloud architecture.

## Key Elements
- Patients, Clinicians / Medical Staff, Administrative / Billing Staff
- External Labs/Imaging, Insurance Payment Gateways, Identity Provider (IdP)
- API Gateway, FHIR Integration Engine, Patient Portal, Clinical Workspace, Billing & Admin Suite
- Core Datastore (PostgreSQL with Row-Level Security), Hardware Security Module (HSM), WORM Audit Logging Service

## Relationships
- Patients & Staff -> CMS: HTTPS (TLS 1.3), OAuth 2.0 / OIDC, MFA
- External Labs/Imaging -> CMS: HL7 FHIR RESTful APIs over HTTPS
- Insurance Payment Gateways -> CMS: Secure API webhooks / REST
- IdP -> CMS: OAuth 2.0 / OpenID Connect (OIDC)
- CMS -> API Gateway: mTLS (Mutual TLS 1.3), ZTNA
- CMS -> HSM: FIPS 140-2 / AES-256
- CMS -> WORM Audit Logging Service: Asynchronous secure logging
- Internal Microservices -> Internal Microservices: gRPC over mTLS (Mutual TLS 1.3), SPIFFE/SPIRE X.509 certs

## Technology Stack
- Kubernetes (`on-prem-k8s` and `eu-central-1`): Container orchestration providing high availability and autoscaling (HPA/PDB).
- PostgreSQL with CQRS: Database using localized read replicas for sub-second read performance and primary master for writes.
- Apache Camel / Node.js: FHIR Integration Engine for handling HL7 FHIR interoperability.
- OpenTelemetry: Distributed tracing with cryptographically signed JWT user identity and role claims.
- Hardware Security Module (HSM): FIPS 140-2 validated cryptographic operations and key management.

## Rationale
The hybrid Kubernetes deployment with CQRS pattern and localized read replicas ensures sub-second EMR load times while maintaining 99.99% uptime across regions. Strict mTLS, HSM encryption, and WORM auditing collectively satisfy rigorous HIPAA, GDPR, and data retention mandates.