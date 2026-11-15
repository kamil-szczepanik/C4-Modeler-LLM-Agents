## Overview
The Clinic Management System is a hybrid cloud platform that manages patient admissions, electronic medical records, scheduling, and billing for medium-sized clinics. It ensures high availability (99.99%), strict HIPAA/GDPR compliance, and sub-second EMR performance.

## Key Elements
- **Users**: Front Desk Staff, Clinicians, Billing Specialists, Patients, Clinic Administrators
- **Frontend Containers**: React Single Page Application (SPA) served via CDN
- **API Gateway**: NGINX / Kong handling TLS termination, OAuth2, and MFA
- **Backend Containers**: Go-based EMR service, Node.js scheduling service, reporting container
- **Integration Containers**: Apache Camel ESB for HL7 FHIR translations and Apache Kafka event bus
- **Data & Caching**: Primary PostgreSQL cluster with read replicas and Redis cluster for slot locking
- **External Systems**: Third-Party Payment Gateways, External Insurance Verification Services, External Lab and Imaging Systems

## Relationships
- Patients & Staff access React SPA via HTTPS (TLS 1.3)
- SPA communicates with Go EMR and Node.js backend via gRPC and REST over mTLS
- API Gateway routes perimeter requests using OAuth2 with Multi-Factor Authentication
- Backend services persist transactional data to PostgreSQL using AES-256 storage encryption
- Scheduling service locks resources via Redis cache over TLS
- Camel ESB synchronizes data with External Lab and Imaging Systems using HL7 FHIR APIs over HTTPS

## Technology Stack
- **Orchestration**: Kubernetes (`on-prem-k8s` and `eu-central-1`) with ArgoCD for GitOps synchronization
- **Backend Languages**: Go and Node.js for high concurrency and performance
- **Frontend**: React SPA served via CDN
- **Databases**: PostgreSQL (relational storage with read replicas), Redis (real-time slot locking with Redis Sentinel)
- **Messaging & Integration**: Apache Kafka (event bus), Apache Camel (ESB for HL7 FHIR)
- **Security**: OAuth2, MFA, mTLS, AES-256 encryption at rest, External KMS
- **Observability**: OpenTelemetry, Prometheus, Grafana, PagerDuty

## Rationale
The hybrid Kubernetes architecture ensures active-active 99.99% availability and meets strict HIPAA/GDPR data residency mandates. Using gRPC, Go, and Redis guarantees sub-second EMR performance and robust real-time appointment scheduling without resource clashes.