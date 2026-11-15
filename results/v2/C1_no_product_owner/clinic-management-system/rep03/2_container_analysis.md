## Overview
The Clinic Management System is a hybrid cloud platform designed to manage patient admissions, electronic medical records (EMR), scheduling, and billing for medium-sized clinics. It ensures strict HIPAA/GDPR compliance, 99.99% availability, and a 10-year data retention policy.

## Key Elements
- **Users**: Patient, Clinician, Receptionist, Billing Specialist
- **External Systems**: Third-Party Payment Gateway, External Lab & Imaging Systems, Insurance Clearinghouse, Enterprise IdP
- **Containers**: API Gateway (Traefik/NGINX), EMR Service (Node.js/TypeScript), Patient & Scheduling Service (Node.js/TypeScript), Billing & Claims Service (Java/Spring Boot), FHIR Interoperability Service (.NET)
- **Data & Infrastructure**: CockroachDB, RabbitMQ, HashiCorp Vault, ArgoCD, OpenTelemetry Collector

## Relationships
- **Users to API Gateway**: Secure access via HTTPS/REST using OAuth2/OIDC with multi-factor authentication (MFA).
- **API Gateway to Containers**: Internal routing via gRPC over mTLS secured by SPIFFE/SPIRE workload identities.
- **Billing & Claims Service to External Systems**: Asynchronous messaging via RabbitMQ integrating with Payment Gateways and Insurance Clearinghouses.
- **FHIR Interoperability Service to External Systems**: HL7 FHIR APIs communicating with external Lab and Imaging systems.

## Technology Stack
- **Languages & Runtimes**: Node.js/TypeScript (Fastify) for EMR and Patient services; Java/Spring Boot for Billing service; .NET for FHIR interoperability.
- **Databases**: CockroachDB for distributed, ACID-compliant transactional and document data with row-level security.
- **Infrastructure & Orchestration**: Hybrid Kubernetes (`on-prem-k8s` and AWS `eu-central-1`) managed via ArgoCD and Helm.
- **Security & Observability**: HashiCorp Vault for dynamic secrets, Cosign/Kyverno for container security, OpenTelemetry for unified tracing.

## Rationale
This architecture uses a hybrid Kubernetes deployment with distributed CockroachDB to achieve active-active 99.99% availability while respecting GDPR data residency. Consolidating runtimes and enforcing mTLS via SPIFFE/SPIRE meets stringent HIPAA security, audit, and performance constraints.