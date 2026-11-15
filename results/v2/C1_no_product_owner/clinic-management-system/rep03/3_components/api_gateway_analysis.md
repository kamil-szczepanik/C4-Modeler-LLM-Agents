## Overview
[The Clinic Management System manages patient admissions, EMRs, scheduling, and billing for medium-sized clinics. It uses a secure hybrid cloud architecture to ensure high availability and regulatory compliance.]

## Key Elements
- **Users**: Patient, Clinician, Receptionist, Billing Specialist
- **External Systems**: Third-Party Payment Gateway, External Lab & Imaging Systems, Insurance Clearinghouse, Enterprise IdP
- **Containers**: API Gateway (Traefik/NGINX), EMR Service (Node.js/Fastify), Patient & Scheduling Service (Node.js/Fastify), Billing & Claims Service (Java/Spring Boot), FHIR Interoperability Service (.NET)
- **Data & Infrastructure**: CockroachDB, RabbitMQ, HashiCorp Vault, ArgoCD / Helm, OpenTelemetry Collector

## Relationships
- **Users -> API Gateway**: Secure access via HTTPS/REST using OAuth2/OIDC with MFA
- **API Gateway -> EMR Service**: Internal routing via gRPC over mTLS (SPIFFE/SPIRE)
- **API Gateway -> Patient & Scheduling Service**: Internal routing via gRPC over mTLS (SPIFFE/SPIRE)
- **API Gateway -> Billing & Claims Service**: Internal routing via gRPC over mTLS (SPIFFE/SPIRE)
- **API Gateway -> FHIR Interoperability Service**: Internal routing via gRPC over mTLS (SPIFFE/SPIRE)

## Technology Stack
- **Traefik/NGINX**: Selected for high-performance ingress routing, SSL termination, and active-active hybrid deployment.
- **Node.js (Fastify) & Java (Spring Boot)**: Used for robust backend microservices handling clinical and financial workflows.
- **CockroachDB**: Chosen for distributed, highly available data storage meeting the 10-year retention mandate.
- **OpenTelemetry & Prometheus**: Deployed for comprehensive distributed tracing and metrics collection.

## Rationale
[This hybrid architecture ensures 99.99% active-active availability across on-premises Kubernetes and AWS eu-central-1. Strict adherence to HIPAA/GDPR is enforced via AES-256 encryption, OAuth2/MFA, and immutable audit logs.]