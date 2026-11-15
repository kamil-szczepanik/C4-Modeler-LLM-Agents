## Overview
The Clinic Management System is a hybrid, containerized platform designed for medium-sized hospitals and clinics to manage patient admissions, EMRs, scheduling, and billing. It ensures HIPAA/GDPR compliance, 99.99% availability, and sub-second EMR performance via a secure, distributed microservices architecture.

## Key Elements
- **Users**: Patients, Receptionists, Clinicians, Billing Specialists
- **External Systems**: Third-Party Lab & Imaging Systems, External Payment Gateways, Insurance Clearinghouses
- **Containers**: React SPA Frontend, NGINX/Kong API Gateway, Domain Microservices (`Patient Service`, `Scheduling Service`, `EMR Service`, `Billing Service`), Apache Camel Integration Service, Distributed PostgreSQL Database, Apache Kafka Event Broker

## Relationships
- Patients & Staff -> API Gateway: HTTPS/WSS via OAuth2/OIDC authentication and MFA
- API Gateway -> Domain Microservices: gRPC with mTLS via service mesh
- Integration Service -> External Systems: HL7 FHIR APIs over TLS
- Domain Microservices -> Apache Kafka: SASL/SCRAM authenticated event streaming
- Domain Microservices -> PostgreSQL: AES-256 encrypted persistent volumes with schema-per-service partitioning

## Technology Stack
- **Frontend**: React Single Page Application (hosted via CDN/Nginx for rapid UI loads)
- **API Gateway**: NGINX/Kong (for single entry point, token exchange, and routing)
- **Backend**: Java / Spring Boot microservices with gRPC (for low-latency internal communication)
- **Integration**: Apache Camel & Apache Kafka (for resilient asynchronous event streaming and HL7 FHIR translation)
- **Database**: PostgreSQL with active-active hybrid replication (for distributed, partitioned transactional storage)
- **Infrastructure**: Kubernetes on-prem and AWS eu-central-1 with service mesh (for 99.99% high availability)

## Rationale
This architecture decouples domain-driven microservices to isolate failures, ensuring third-party outages do not halt clinical workflows while meeting sub-second EMR performance SLAs. Hybrid Kubernetes deployment, strict mTLS service mesh boundaries, and AES-256 encryption satisfy rigorous HIPAA and GDPR compliance mandates.