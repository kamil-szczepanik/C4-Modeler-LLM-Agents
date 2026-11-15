## Overview
The Clinic Management System is a hybrid cloud platform designed for medium-sized hospitals and clinics to manage patient admissions, electronic medical records (EMR), scheduling, and billing securely. It ensures high availability, strict compliance, and reliable offline-resilient operations for clinical staff.

## Key Elements
- Users: Doctors, Nurses, Receptionists, Billing Staff, Clinic Administrators, Patients
- External Systems: Identity Provider (IdP), External Labs & Imaging Systems, Payment Gateway / Insurance Clearinghouse
- Containers: API Gateway, Web Application (SPA), Core Services (Patient & Scheduling, EMR, Billing, FHIR Interoperability)
- Data & Integration Tier: PostgreSQL, Redis, Apache Kafka, AWS S3 Object Lock

## Relationships
- Users access the Web Application via HTTPS/TLS terminated at the API Gateway.
- API Gateway authenticates requests via OAuth2/OIDC interacting with the IdP and routes traffic using gRPC over mTLS.
- Core Services communicate securely via Istio/Linkerd service mesh and interact with PostgreSQL (AES-256 at rest).
- FHIR Interoperability Service connects external labs and imaging systems using HL7 FHIR APIs.
- Billing Service submits claims to external clearinghouses asynchronously via Apache Kafka.

## Technology Stack
- API Gateway: Nginx / Kong for rate limiting and TLS termination
- Frontend: React / TypeScript served via Nginx
- Backend Services: Node.js / NestJS or Java / Spring Boot microservices
- Databases & Caching: PostgreSQL (active-passive), Redis for edge caching
- Messaging: Apache Kafka for event-driven workflows and Transactional Outbox Pattern
- Infrastructure & Security: Kubernetes (on-prem & AWS EKS), ArgoCD, HashiCorp Vault / AWS Secrets Manager, Istio/Linkerd, OpenTelemetry

## Rationale
This hybrid architecture isolates critical edge services to guarantee local survivability and sub-second check-ins during WAN outages. It enforces robust security, active-passive failover, and immutable storage to strictly satisfy HIPAA, GDPR, and 99.99% availability constraints.