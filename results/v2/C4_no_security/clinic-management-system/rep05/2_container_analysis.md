## Overview
The Clinic Management System manages patient admissions, EMRs, scheduling, and billing for clinical IT environments. It ensures 99.99% availability, strict HIPAA/GDPR compliance, and sub-second EMR performance via a secure hybrid architecture.

## Key Elements
- **Users**: Receptionists, Clinicians, Billing Specialists, Compliance Officers, Patients
- **External Systems**: Lab & Imaging Systems, Insurance Clearinghouses, Enterprise IdP, Patient Portal
- **Containers**: SPA Frontend (React/TypeScript/Nginx), EMR Core Service, Billing & Claims Service, Audit & Compliance Service, Integration Gateway (Apache Camel/Spring Cloud Gateway)
- **Data & Messaging**: PostgreSQL (primary-replica with Patroni), Redis Cluster, Apache Kafka
- **Infrastructure**: on-prem-k8s cluster, AWS eu-central-1 (backup vault), Cilium/Istio service mesh

## Relationships
- **SPA Frontend** to **API Containers**: HTTPS / WSS
- **Internal Microservices** (EMR, Billing, Audit): gRPC over mTLS with eBPF routing
- **Integration Gateway** to **External Systems**: HL7 FHIR APIs over HTTPS
- **Services** to **PostgreSQL/Redis**: TCP with AES-256 encryption at rest
- **Services** to **Apache Kafka**: TCP event streaming

## Technology Stack
- **Frontend**: React, TypeScript, Nginx (for rapid UI rendering)
- **Backend**: Spring Boot, Java (modular microservices architecture)
- **Database & Cache**: PostgreSQL with Patroni, Redis Cluster (for low-latency EMR caching and data integrity)
- **Messaging & Integration**: Apache Kafka, Apache Camel / Spring Cloud Gateway (for asynchronous workflows and HL7 FHIR interoperability)
- **Infrastructure & Security**: Kubernetes (on-prem-k8s), Cilium/Istio (eBPF service mesh), Terraform, ArgoCD, Prometheus, Grafana Loki, OpenTelemetry, AES-256 encryption

## Rationale
This architecture balances strict healthcare data integrity and regulatory compliance via a primary-replica PostgreSQL setup and dedicated audit containers. Simultaneously, it guarantees sub-second EMR performance and 99.99% availability through decoupled microservices, in-memory caching, and optimized on-prem Kubernetes networking.