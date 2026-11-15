## Overview
The Clinic Management System manages patient admissions, electronic medical records (EMR), scheduling, and billing for healthcare facilities. It provides high availability, stringent compliance, and sub-second clinical data access across a hybrid cloud infrastructure.

## Key Elements
- **Users**: Receptionists, Clinicians, Billing Officers, Patients
- **External Systems**: Lab & Imaging Systems, Payment Gateway & Insurance Clearinghouses, Identity Provider (IdP)
- **Containers**: API Gateway (Kong / Nginx), Patient-Facing UI (React / Next.js), Clinical Core Services (Spring Boot / Java), Interoperability Service (Apache Camel / Node.js), Billing & Claims Service (Spring Boot / Java)
- **Components (Clinical Core Services)**: EMR Engine, Scheduling Engine, Authorization Interceptor, Audit Logger, Event Dispatcher

## Relationships
- Patient-Facing UI -> API Gateway: HTTPS / REST [TLS 1.3]
- API Gateway -> Clinical Core Services: gRPC over mTLS [gRPC, mTLS]
- Clinical Core Services -> Billing & Claims Service: gRPC over mTLS [gRPC, mTLS]
- Clinical Core Services -> Interoperability Service: gRPC over mTLS [gRPC, mTLS]
- Clinical Core Services -> External Lab & Imaging Systems: HL7 FHIR APIs [HTTPS]

## Technology Stack
- **Backend**: Java / Spring Boot for microservices business logic
- **Database & Caching**: PostgreSQL with Spring Data JPA and Hazelcast L2 cache (AES-256 encrypted) for <1s P95 EMR reads
- **Resilience**: Resilience4j for circuit breakers and fallback mechanisms during network partitions
- **Infrastructure**: Kubernetes (on-prem-k8s and AWS eu-central-1) with HashiCorp Vault for secret management
- **Observability**: OpenTelemetry and Prometheus for distributed tracing and metrics

## Rationale
This architecture uses active-active hybrid cloud replication and Hazelcast caching to guarantee 99.99% availability and sub-second EMR performance. It enforces HIPAA and GDPR compliance through mTLS, AES-256 encryption at rest and in memory, RBAC/ABAC authorization, and WORM audit logging.