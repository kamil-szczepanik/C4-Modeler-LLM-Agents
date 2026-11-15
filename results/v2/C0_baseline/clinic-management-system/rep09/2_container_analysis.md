## Overview
The Clinic Management System is a hybrid cloud platform designed for medium-sized hospitals and clinics to manage patient admissions, EMRs, scheduling, and billing. It ensures HIPAA/GDPR compliance, high availability (99.99%), and 10-year data retention.

## Key Elements
- **Users**: Patient, Clinician, Receptionist/Admin, Billing Specialist, Compliance Officer
- **External Systems**: Enterprise Identity Provider (IdP), External Labs & Imaging Systems, Insurance Claim Gateways
- **Containers**: Nginx Web App, API Gateway (Kong/Envoy), Core Clinical & EMR Container, Billing & Claims Container, HL7 FHIR Interoperability Container, Patient Portal Container, Sync/Replication Container, Audit Sidecar Container

## Relationships
- **Patient/Staff to Web App/Patient Portal**: HTTPS (TLS)
- **Web App/Patient Portal to API Gateway**: HTTPS / REST / GraphQL via TLS
- **API Gateway to Core Containers**: gRPC over mTLS (Istio/Linkerd service mesh)
- **Core Clinical Container to PostgreSQL**: Encrypted connection with AES-256
- **Billing Container to Insurance Claim Gateways**: HTTPS / TLS with message queues
- **HL7 FHIR Container to External Labs**: HL7 FHIR APIs over TLS

## Technology Stack
- **Orchestration**: Kubernetes (`on-prem-k8s` and AWS `eu-central-1`) for active-active multi-region HA
- **Backend**: Spring Boot / Go for microservices, Node.js / Apache Camel for HL7 integration
- **Frontend**: Single Page Application (Nginx), Next.js/React for Patient Portal
- **Database**: Multi-region PostgreSQL cluster with AES-256 encryption at rest
- **Integration & Sync**: Apache Kafka / Outbox pattern for offline resilience and replication
- **Security & Observability**: OAuth2/OIDC, HashiCorp Vault for secrets, OpenTelemetry for distributed tracing

## Rationale
This hybrid architecture isolates critical clinical workflows and patient portals behind an API gateway while supporting offline resilience for on-premise clinics via asynchronous sync. Strict mTLS segmentation, encryption, and immutable audit logs ensure high performance (<1s P95) and strict HIPAA/GDPR compliance.