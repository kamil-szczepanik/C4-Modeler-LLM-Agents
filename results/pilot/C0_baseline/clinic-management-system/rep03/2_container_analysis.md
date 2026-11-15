## Overview
- Manages patient admissions, electronic medical records, scheduling, and billing for clinics.
- Ensures HIPAA/GDPR compliance, 99.99% availability, and 10-year data retention.

## Key Elements
- Users: Patients, Front Desk Staff, Clinicians, Billing Specialists
- External Systems: Payment Gateway, Insurance Verification/RTE APIs, Lab & Imaging Systems
- Containers: Patient Portal SPA, Clinician Workspace SPA, API Gateway (Kong/Envoy), Core Clinical Services, Finance & Billing
- Infrastructure: Hybrid Kubernetes, PostgreSQL cluster, Elasticsearch, Redis Enterprise cluster, Kafka event bus (Confluent/MSK)

## Relationships
- Patient Portal SPA to API Gateway via HTTPS (TLS 1.3)
- Clinician Workspace SPA to API Gateway via HTTPS (TLS 1.3)
- API Gateway to Backend Containers (Core Clinical Services, Finance & Billing) via gRPC over mTLS
- Core Clinical Services to Kafka event bus for asynchronous billing decoupling
- Core Clinical Services and Finance & Billing to PostgreSQL, Elasticsearch, and Redis via secure TCP/TLS connections
- External Lab & Imaging Systems to API Gateway via HL7 FHIR over HTTPS REST

## Technology Stack
- React: Powers Patient Portal and Clinician Workspace SPAs for interactive UI
- Kong/Envoy: Acts as secure API Gateway handling OAuth2/OIDC and RBAC/ABAC
- Spring Boot: Implements Core Clinical Services and Finance & Billing business logic
- PostgreSQL: Provides transactional persistence with AES-256 encryption at rest and PgBouncer
- Elasticsearch: Enables indexed EMR full-text searches and audit log queries
- Redis Enterprise: Delivers low-latency caching and appointment locking
- Apache Kafka (Confluent/MSK): Handles asynchronous event messaging between clinical and billing domains
- Kubernetes (Hybrid On-Prem & AWS `eu-central-1`): Orchestrates containerized microservices with ArgoCD GitOps

## Rationale
- Isolating front-end portals from back-end engines protects PHI and ensures continuous revenue operations.
- Hybrid Kubernetes orchestration with active-active scaling guarantees 99.99% uptime and sub-second EMR response times.