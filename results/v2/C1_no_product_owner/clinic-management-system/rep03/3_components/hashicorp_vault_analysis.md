## Overview
The Clinic Management System is a hybrid cloud platform designed to manage patient admissions, electronic medical records (EMR), scheduling, and billing for medium-sized healthcare facilities. It ensures high availability, strict compliance, and interoperability across on-premises Kubernetes and AWS (`eu-central-1`).

## Key Elements
- **Actors**: Patient, Clinician, Receptionist, Billing Specialist
- **External Systems**: Third-Party Payment Gateway, External Lab & Imaging Systems, Insurance Clearinghouse, Enterprise IdP
- **Core Containers**: API Gateway (Traefik/NGINX), EMR Service (Node.js/Fastify), Patient & Scheduling Service (Node.js/Fastify), Billing & Claims Service (Java/Spring Boot), FHIR Interoperability Service (.NET)
- **Data & Infrastructure Containers**: CockroachDB, RabbitMQ, ArgoCD / Helm, OpenTelemetry Collector
- **HashiCorp Vault Components**: Secrets Engine, Auth Methods, Audit Log, Storage Backend Integration

## Relationships
- *API Gateway* -> *Services* via HTTPS/REST for client request routing
- *Services* -> *Vault Auth Methods* via HTTPS/REST for mTLS token acquisition
- *Services* -> *Vault Secrets Engine* via HTTPS/REST for dynamic credential retrieval
- *Vault Secrets Engine* -> *CockroachDB* via native SQL protocol using dynamic credentials
- *Vault Audit Component* -> *OpenTelemetry Collector* via syslog/file tailing for SIEM ingestion
- *Storage Backend Integration Component* -> *AWS S3* via HTTPS for disaster recovery snapshots

## Technology Stack
- **Compute**: Hybrid Kubernetes (`on-prem-k8s` and AWS `eu-central-1`) for active-active multi-region deployment supporting 99.99% uptime
- **Secrets Management**: HashiCorp Vault (AppRole, Kubernetes Auth, KV/Database Secrets Engines, Raft storage, AWS KMS/HSM auto-unseal) for encryption and dynamic credentials
- **Database**: CockroachDB for distributed, resilient transactional data storage with AES-256 at rest
- **Messaging**: RabbitMQ for asynchronous event processing between services
- **Interoperability**: HL7 FHIR APIs for lab and imaging system integration
- **Observability**: OpenTelemetry Collector and Prometheus for telemetry and metrics collection

## Rationale
This architecture uses active-active hybrid Kubernetes deployment paired with HashiCorp Vault for secure, dynamic credential management to achieve 99.99% availability and meet strict HIPAA and GDPR compliance mandates. Distributed services and HL7 FHIR standards ensure sub-second EMR performance and seamless interoperability with external clinical systems.