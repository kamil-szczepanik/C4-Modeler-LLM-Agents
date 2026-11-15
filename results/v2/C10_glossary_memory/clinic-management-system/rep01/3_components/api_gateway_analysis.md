## Overview
The Clinic Management System is a hybrid cloud platform designed to manage patient admissions, electronic medical records, scheduling, and billing. It ensures high availability and strict compliance with healthcare regulations.

## Key Elements
- Patients
- Clinicians / Medical Staff
- Administrative / Billing Staff
- External Labs/Imaging
- Insurance Payment Gateways
- Identity Provider (IdP)
- API Gateway
- Hardware Security Module (HSM)
- WORM Audit Logging Service
- FHIR Integration Engine
- Patient Portal
- Clinical Workspace
- Billing & Admin Suite
- Core Datastore

## Relationships
- Patients -> API Gateway (HTTPS (TLS 1.3), OAuth 2.0 / OIDC, MFA)
- Clinicians / Medical Staff -> API Gateway (HTTPS (TLS 1.3), OAuth 2.0 / OIDC, MFA)
- Administrative / Billing Staff -> API Gateway (HTTPS (TLS 1.3), OAuth 2.0 / OIDC, MFA)
- External Labs/Imaging -> API Gateway (HL7 FHIR RESTful APIs over HTTPS with mTLS)
- Insurance Payment Gateways -> API Gateway (Secure API webhooks / REST)
- Identity Provider (IdP) -> API Gateway (OAuth 2.0 / OpenID Connect (OIDC))
- API Gateway -> Patient Portal (gRPC over mTLS 1.3, SPIFFE/SPIRE X.509)
- API Gateway -> Clinical Workspace (gRPC over mTLS 1.3, SPIFFE/SPIRE X.509)
- API Gateway -> Billing & Admin Suite (gRPC over mTLS 1.3, SPIFFE/SPIRE X.509)
- API Gateway -> FHIR Integration Engine (gRPC over mTLS 1.3, SPIFFE/SPIRE X.509)

## Technology Stack
- Envoy / NGINX: Provides high-performance ingress routing, payload sanitization, and TLS termination.
- Lua / WASM: Executes low-latency JWT validation, MFA verification, and scope-based access checks.
- Redis (Cluster): Powers token-bucket rate limiting and distributed token revocation checks.
- PostgreSQL with CQRS: Separates read and write workloads for optimized performance and data persistence.
- FIPS 140-2 Hardware HSM: Secures cryptographic operations and AES-256 encryption keys.

## Rationale
This architecture uses a zero-trust model with mTLS and token validation to satisfy HIPAA and GDPR security mandates. Distributed services and active-active components ensure 99.99% availability and high-performance EMR retrieval.