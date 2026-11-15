## Overview
The Clinic Management System is a hybrid cloud platform designed to manage patient admissions, electronic medical records (EMR), scheduling, and billing for medium-sized healthcare facilities. It ensures high availability (99.99%), strict HIPAA/GDPR compliance, and seamless clinical interoperability.

## Key Elements
- **Users**: Patient, Clinician / Doctor, Receptionist / Admin, Billing Specialist, Compliance Officer
- **External Systems**: Insurance / Payer System, Lab & Imaging Systems
- **Containers & Services**: Web Frontend, Patient Portal / Mobile App, API Gateway, EMR Service, Billing / Claims Service
- **EMR Internal Components**: Audit & Compliance Tracker, Read-Only Offline Cache Component
- **Infrastructure & Security**: OpenTelemetry sidecars, Audit Logging sidecars (WORM), HashiCorp Vault, Kubernetes (`on-prem-k8s`), AWS (`eu-central-1`)

## Relationships
- **API Gateway -> EMR Service**: Forwards internal requests via gRPC/REST over mTLS and SPIFFE/SPIRE
- **EMR Service -> Lab & Imaging Systems**: Integrates clinical data via HL7 FHIR APIs with mutual TLS (mTLS)
- **EMR Service -> Audit Logging sidecars**: Writes asynchronous compliance logs to WORM storage
- **EMR Service -> HashiCorp Vault**: Retrieves dynamic secrets and ephemeral encryption keys

## Technology Stack
- **Languages & Frameworks**: Containerized microservices running on Kubernetes for active-active multi-region deployment
- **Security & Cryptography**: AES-256 encryption at rest, AWS KMS/Vault envelope encryption, OAuth2/OIDC, ABAC, and mTLS for zero-trust network security
- **Interoperability**: HL7 FHIR APIs with automated schema validation and XML/JSON bomb protection
- **Observability**: OpenTelemetry sidecars for distributed tracing and tail-latency tracking

## Rationale
This hybrid architecture uses active-active deployment across `on-prem-k8s` and AWS `eu-central-1` to guarantee the 99.99% availability required for critical clinical workflows. Asynchronous audit logging, local offline caching, and strict cryptographic controls ensure sub-second EMR performance while fully meeting HIPAA, GDPR, and 10-year data retention mandates.