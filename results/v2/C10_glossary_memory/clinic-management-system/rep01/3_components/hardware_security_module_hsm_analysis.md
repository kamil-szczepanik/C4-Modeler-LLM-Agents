## Overview
The Clinic Management System (CMS) manages patient admissions, EMRs, scheduling, and billing for healthcare facilities. It ensures HIPAA/GDPR compliance, 10-year data retention, and 99.99% uptime via a hybrid cloud architecture.

## Key Elements
- Patients, Clinicians / Medical Staff, Administrative / Billing Staff
- External Labs/Imaging, Insurance Payment Gateways, Identity Provider (IdP)
- API Gateway, FHIR Integration Engine, Patient Portal, Clinical Workspace, Billing & Admin Suite
- Core Datastore (PostgreSQL with CQRS), WORM Audit Logging Service
- Hardware Security Module (HSM): Cryptographic Engine, Key Management Service (KMS) Daemon, Secure Hardware Vault, Key Version Registry

## Relationships
- Patients / Staff -> API Gateway via HTTPS (TLS 1.3), OAuth 2.0 / OIDC, MFA
- API Gateway -> Containers via gRPC over mTLS (Mutual TLS 1.3), SPIFFE/SPIRE X.509 certs
- Clinical Workspace & Billing & Admin Suite -> Core Datastore (PostgreSQL with CQRS)
- Clinical Workspace & Billing & Admin Suite -> Cryptographic Engine via PKCS#11 over TLS 1.3 (mTLS)
- Key Management Service (KMS) Daemon -> Secure Hardware Vault via internal proprietary bus
- Key Management Service (KMS) Daemon -> Key Version Registry via internal secure database read/write

## Technology Stack
- Kubernetes / AWS: Powers scalable container orchestration across hybrid regions (`on-prem-k8s` and `eu-central-1`)
- PostgreSQL with CQRS: Provides persistent storage with localized read replicas and primary master for writes
- FIPS 140-2 Level 3 Hardware: Ensures hardware-accelerated cryptographic operations and tamper-resistant key storage
- PKCS#11 / KMIP & TLS 1.3: Facilitates secure cryptographic operations and transport encryption

## Rationale
This architecture meets 99.99% availability and HIPAA/GDPR compliance via active-active HSM partitioning, strict least-privilege separation of duties, and zero-downtime key rotation. The hybrid infrastructure ensures resilient data protection across on-premises and AWS environments.