## Overview
The Clinic Management System manages patient admissions, electronic medical records, scheduling, and billing for medium-sized healthcare facilities. It provides high availability, stringent security controls, and seamless interoperability for clinical operations.

## Key Elements
- Patients, Clinicians / Medical Staff, Administrative / Billing Staff
- External Labs/Imaging, Insurance Payment Gateways, Identity Provider (IdP)
- API Gateway (Kubernetes / AWS)
- FHIR Integration Engine (Apache Camel / Node.js)
- Patient Portal, Clinical Workspace, Billing & Admin Suite (Kubernetes)
- Core Datastore (PostgreSQL with CQRS)
- Hardware Security Module (HSM) (FIPS 140-2 Hardware)
- WORM Audit Logging Service (Secure Storage)

## Relationships
- Patients, Clinicians, Admin Staff -> API Gateway: HTTPS (TLS 1.3), OAuth 2.0 / OIDC, MFA
- External Labs/Imaging -> API Gateway: HL7 FHIR RESTful APIs over HTTPS with mTLS
- Insurance Payment Gateways -> API Gateway: Secure API webhooks / REST
- Identity Provider (IdP) -> API Gateway: OAuth 2.0 / OpenID Connect (OIDC)
- API Gateway -> FHIR Integration Engine: gRPC over mTLS (Mutual TLS 1.3), SPIFFE/SPIRE X.509 certs
- FHIR Integration Engine -> Core Datastore: PostgreSQL with CQRS
- CMS Containers -> Hardware Security Module (HSM): FIPS 140-2 / AES-256
- CMS Containers -> WORM Audit Logging Service: Asynchronous secure logging

## Technology Stack
- Kubernetes & AWS: Container orchestration and infrastructure hosting for high availability (99.99%)
- PostgreSQL with CQRS: Core database architecture optimizing read/write performance
- Apache Camel & Node.js: Integration routing and mapping for the FHIR Engine
- FIPS 140-2 Hardware HSM & AES-256: Cryptographic key management and data protection at rest
- Mutual TLS 1.3 & OAuth 2.0 / OIDC: Zero-trust network communication and identity federation

## Rationale
This hybrid cloud architecture combines on-premise Kubernetes clusters with AWS in eu-central-1 to guarantee 99.99% active-active uptime and strict data residency. It satisfies HIPAA/GDPR compliance via AES-256 encryption, HSM key management, and WORM audit logging while supporting <1s P95 EMR performance and HL7 FHIR interoperability.