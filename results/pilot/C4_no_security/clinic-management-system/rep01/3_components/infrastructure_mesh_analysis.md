## Overview
The Clinic Management System is a hybrid cloud clinical IT platform providing patient admissions, electronic medical records (EMR), scheduling, and billing. Its core purpose is to deliver secure, highly available hospital workflows complying with HIPAA, GDPR, and a 99.99% uptime SLA.

## Key Elements
- Patients, Clinical Staff, Hospital Administrators
- Global Anycast Load Balancer and API Gateways (Kong)
- Patient Portal (Node.js, React)
- EMR & Scheduling Service (Java Spring Boot)
- Billing & Insurance Claim Service (Python FastAPI)
- HL7 FHIR Interoperability Engine (Apache Camel)
- Database Tier (PostgreSQL with PgBouncer, AES-256)
- Messaging & Audit Layer (Apache Kafka, FluentBit, S3)
- Infrastructure & Mesh (Kubernetes, AWS eu-central-1, on-prem-k8s, Envoy sidecar, Istio, ArgoCD)
- External Systems: Lab/Imaging Systems, Insurance Clearinghouses

## Relationships
- Patients and Staff access Patient Portal and EMR via HTTPS/MFA through Global Anycast Load Balancer and API Gateways.
- Microservices communicate internally and across hybrid boundaries via gRPC and HTTPS over mutual TLS (mTLS) enforced by Envoy sidecars and Istio.
- Database and messaging operations use PostgreSQL wire protocol with AES-256 and Kafka protocols.
- Interoperability Engine connects to external lab/imaging systems via HL7 FHIR APIs over HTTPS.

## Technology Stack
- Kubernetes & Istio: Hybrid orchestration and service mesh for multi-cluster routing and mTLS.
- ArgoCD: GitOps synchronization across on-premise clusters and AWS `eu-central-1`.
- PostgreSQL & PgBouncer: Relational data storage with AES-256 encryption at rest.
- Apache Kafka & FluentBit: Event streaming and audit log shipping to immutable S3 storage.
- Node.js/React, Java Spring Boot, Python FastAPI: Containerized application runtimes.

## Rationale
This hybrid architecture guarantees high availability (99.99% active-active) and disaster recovery by distributing workloads across on-premise Kubernetes and AWS `eu-central-1`. Strict compliance with HIPAA and GDPR is enforced via mTLS, cryptographic workload identities, AES-256 encryption, and immutable audit logs.