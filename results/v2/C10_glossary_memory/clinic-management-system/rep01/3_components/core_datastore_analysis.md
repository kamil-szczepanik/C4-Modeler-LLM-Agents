## Overview
The Clinic Management System manages patient admissions, EMRs, scheduling, and billing while ensuring HIPAA/GDPR compliance and 99.99% availability. It utilizes a hybrid cloud architecture deploying core containers across Kubernetes and AWS.

## Key Elements
- Clinic Management System (CMS)
- Patients, Clinicians / Medical Staff, Administrative / Billing Staff
- External Labs/Imaging, Insurance Payment Gateways, Identity Provider (IdP)
- API Gateway (Kubernetes / AWS)
- Patient Portal, Clinical Workspace, Billing & Admin Suite, FHIR Integration Engine (Apache Camel / Node.js)
- Core Datastore (PostgreSQL with CQRS)
- Hardware Security Module (HSM) (FIPS 140-2 Hardware)
- WORM Audit Logging Service (Secure Storage)

## Relationships
- Patients, Clinicians, Staff -> API Gateway (HTTPS (TLS 1.3), OAuth 2.0 / OIDC, MFA)
- External Labs/Imaging -> API Gateway (HL7 FHIR RESTful APIs over HTTPS)
- Insurance Payment Gateways -> API Gateway (Secure API webhooks / REST)
- Identity Provider (IdP) -> API Gateway (OAuth 2.0 / OpenID Connect (OIDC))
- API Gateway -> Patient Portal, Clinical Workspace, Billing & Admin Suite, FHIR Integration Engine (gRPC over mTLS, SPIFFE/SPIRE X.509 certs)
- Clinical Workspace, Billing & Admin Suite, FHIR Integration Engine -> Core Datastore (PostgreSQL wire protocol over TLS 1.3, mTLS)
- CMS -> Hardware Security Module (FIPS 140-2 / AES-256)
- CMS -> WORM Audit Logging Service (Asynchronous secure logging)

## Technology Stack
- Kubernetes and AWS eu-central-1: Hybrid cloud runtime for high availability.
- PostgreSQL with CQRS: Separates read and write traffic for sub-second EMR performance.
- Apache Camel / Node.js: Powers the FHIR Integration Engine for HL7 interoperability.
- FIPS 140-2 HSM & AES-256: Ensures cryptographic key management and data protection.
- WORM Storage: Guarantees immutable audit logging for ≥ 10 years data retention.

## Rationale
This architecture uses hybrid Kubernetes deployment and PostgreSQL CQRS to meet 99.99% availability and <1s EMR load performance. Strict encryption, HSM integration, and WORM logging ensure compliance with HIPAA, GDPR, and long-term data retention mandates.