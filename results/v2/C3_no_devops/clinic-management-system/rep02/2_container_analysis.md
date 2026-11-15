## Overview
The Clinic Management System is a hybrid cloud platform designed to manage patient admissions, electronic medical records (EMR), scheduling, and billing for medium-sized hospitals and clinics. It ensures high availability (99.99%), strict HIPAA/GDPR compliance, and interoperability with external clinical systems.

## Key Elements
* **Users:** Patient, Clinical Staff, Administrative Staff, Compliance Officer / Auditor
* **External Systems:** Payment Gateway, Insurance Clearinghouse, External Lab / Imaging Systems, Pharmacy Management System
* **Containers:** API Gateway, Patient Self-Service Container, EMR Backend Container, Scheduling & Resource Engine Container, Integration Broker Container, Audit & Compliance Daemon Container
* **Data Stores:** EMR Database (PostgreSQL), Redis Cluster, Cold Storage (10-year retention)

## Relationships
* **Patients & Staff to API Gateway:** HTTPS/REST with OAuth2/OIDC, JWT, and MFA
* **API Gateway to Containers:** Internal mTLS over gRPC/REST within Kubernetes clusters
* **Integration Broker to External Systems:** HL7 FHIR APIs over gRPC/REST
* **Containers to Databases:** Encrypted connections (TLS) with AES-256 storage and column-level encryption via HashiCorp Vault
* **Audit & Compliance Daemon to Kafka:** Asynchronous streaming for immutable audit logs

## Technology Stack
* **API Gateway:** Kong / Nginx in Kubernetes for ingress, TLS termination, and rate-limiting
* **Frontend:** React/Next.js Single Page Application (SPA) served via CDN for the Patient Portal
* **Backend Services:** Node.js, Java Spring Boot, and Go (for the Audit & Compliance Daemon) to isolate performance domains
* **Databases & Caching:** PostgreSQL with row-level security (RLS) and an in-memory Redis cluster with TLS for scheduling
* **Messaging & Integration:** Apache Kafka for log streaming and Apache Camel / Node-RED for HL7 FHIR translations
* **Security & Infrastructure:** HashiCorp Vault for KMS, Kubernetes for container orchestration across on-prem and AWS (`eu-central-1`)

## Rationale
This hybrid container architecture separates public-facing workflows from secure internal clinical networks, ensuring strict HIPAA/GDPR compliance and robust data protection. Decoupled containers and active-active replication guarantee 99.99% availability, while optimized backend services maintain sub-second EMR load times under high loads.