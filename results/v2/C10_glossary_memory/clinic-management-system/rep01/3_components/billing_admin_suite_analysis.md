## Overview
[The Clinic Management System manages patient admissions, EMRs, scheduling, and billing for medium-sized healthcare facilities. It provides high availability, stringent security, and interoperability across hybrid cloud environments.]

## Key Elements
- Clinic Management System (CMS) [system, context]
- Patients, Clinicians / Medical Staff, Administrative / Billing Staff [person, context]
- External Labs/Imaging, Insurance Payment Gateways, Identity Provider (IdP) [externalSystem, context]
- API Gateway, Hardware Security Module (HSM), WORM Audit Logging Service, FHIR Integration Engine [container]
- Patient Portal, Clinical Workspace, Billing & Admin Suite [container]
- Core Datastore [container]

## Relationships
- Patients / Staff -> API Gateway (HTTPS TLS 1.3, OAuth 2.0 / OIDC, MFA)
- External Labs/Imaging -> API Gateway (HL7 FHIR RESTful APIs over HTTPS)
- Insurance Payment Gateways -> API Gateway (Secure API webhooks / REST)
- Identity Provider (IdP) -> API Gateway (OAuth 2.0 / OIDC)
- API Gateway -> Billing & Admin Suite (gRPC over mTLS 1.3, SPIFFE/SPIRE X.509 certs)
- Billing & Admin Suite -> Core Datastore (PostgreSQL with CQRS)
- Billing & Admin Suite -> Hardware Security Module (HSM) (FIPS 140-2 / AES-256)
- Billing & Admin Suite -> WORM Audit Logging Service (Asynchronous secure logging)

## Technology Stack
- Kubernetes [container orchestration]: Provides active-active deployment across hybrid regions (`on-prem-k8s` and `eu-central-1`) for 99.99% availability.
- PostgreSQL with CQRS [datastore]: Separates read and write workloads to optimize EMR screen performance under 1 second P95.
- Apache Camel / Node.js [integration]: Implements HL7 FHIR APIs for external lab and imaging interoperability.
- FIPS 140-2 Hardware HSM [security]: Secures data at rest with AES-256 encryption and hardware-backed key management.
- Istio Service Mesh [networking]: Manages mTLS 1.3, traffic shaping, and cross-region failover.

## Rationale
[This hybrid architecture ensures 99.99% uptime through active-active Kubernetes clusters while strictly adhering to HIPAA and GDPR compliance via end-to-end encryption, mTLS, and immutable WORM audit logs.]