## Overview
The Clinic Management System is a clinical IT platform managing patient admissions, EMR, scheduling, and billing for medium-sized healthcare facilities. It ensures high availability, strict security, and hybrid cloud operations.

## Key Elements
- Patients, Doctors, Billing Staff
- API Gateway (Kubernetes Ingress)
- Patient/EMR Service, Scheduling Service, Billing Service (Kubernetes Microservices)
- HashiCorp Vault with Vault Agent sidecars
- PostgreSQL Databases with database-per-service pattern
- Redis (Distributed Cache) and Kafka / RabbitMQ (Message Broker)
- External Systems (Third-party Insurance Gateways, Lab/Imaging Systems via HL7 FHIR APIs, External Identity Providers)
- Observability & Security Stack (Prometheus, OpenTelemetry, Falco/Trivy Operator, centralized SIEM)

## Relationships
- Patients & Staff -> API Gateway: Accesses services securely [HTTPS / mTLS]
- Microservices -> Vault Agent Sidecar: Retrieves encrypted configurations and secrets locally [HTTPS / Vault Agent API]
- Vault Agent Sidecar -> HashiCorp Vault Server: Authenticates and fetches secrets [Kubernetes Auth Method / HTTPS]
- Microservices -> PostgreSQL: Persists transactional data [PostgreSQL Wire Protocol / Dynamic Secrets]
- Clinic Management System -> Lab/Imaging Systems: Exchanges medical data [HL7 FHIR APIs]

## Technology Stack
- Kubernetes (on-prem-k8s and AWS eu-central-1): Core container orchestration for hybrid cloud deployment ensuring high availability.
- HashiCorp Vault: Centralized secrets management, dynamic database credentials, and Transit Secrets Engine for envelope encryption.
- Vault Agent Sidecar: Local caching and template rendering via `tmpfs` volumes to prevent network bottlenecks.
- Terraform: Configuration-as-Code for declarative management of Vault policies and mounts.
- PostgreSQL: Relational storage utilizing dynamic database credentials managed by Vault.

## Rationale
The architecture combines a hybrid Kubernetes deployment with Vault Agent sidecars and auto-unseal mechanisms to guarantee 99.99% availability and low-latency local resilience. Envelope encryption, dynamic credentials, and zero-trust network policies enforce HIPAA and GDPR compliance without sacrificing P95 performance targets.