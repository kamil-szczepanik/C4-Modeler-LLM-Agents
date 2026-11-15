## Overview
The Clinic Management System manages patient admissions, EMRs, scheduling, and billing for healthcare facilities. It relies on a secure, highly available hybrid cloud architecture to ensure strict HIPAA/GDPR compliance and 99.99% uptime.

## Key Elements
- **Users**: Front-Desk Receptionist, Clinician/Doctor, Billing Specialist, Patient, Hospital Administrator, Compliance Officer
- **External Systems**: External Lab & Imaging Systems, Third-Party Payment & Insurance Gateway, Identity Provider (IdP)
- **Frontend Containers**: Patient Portal Frontend (React), Staff Web Application (React)
- **Backend Containers**: API Gateway (Kong/NGINX/Envoy), Core Clinical & EMR Service (Java Spring Boot), Scheduling Service (Node.js/Python), Billing & Claims Service (Java Spring Boot), FHIR Interoperability Adapter (HAPI FHIR), Audit & Compliance Service (Go/Spring Boot)
- **Data & Security Containers**: PostgreSQL databases, AWS S3 Object Lock, HashiCorp Vault

## Relationships
- Users access Frontend Containers and Staff Web Application via **HTTPS (TLS 1.3)**.
- API Gateway routes requests to backend services via **gRPC/REST over TLS 1.3**.
- Core services fetch secrets and encryption keys from HashiCorp Vault using **HTTPS (REST/gRPC)** via **Kubernetes Service Accounts (JWT/AppRole)** and **mTLS**.
- FHIR Interoperability Adapter communicates with External Lab & Imaging Systems using **HL7 FHIR REST APIs**.
- Core services persist and query data in PostgreSQL databases via **PostgreSQL wire protocol (TLS)**.
- Audit & Compliance Service streams tamper-proof logs from Vault and microservices.

## Technology Stack
- **Compute/Orchestration**: Kubernetes (`on-prem-k8s` and AWS `eu-central-1`) for scalable container deployment and high availability.
- **Frontend**: React for responsive user interfaces.
- **Backend Services**: Java Spring Boot (Core Clinical, Billing) and Node.js/Python (Scheduling) for robust business logic.
- **Interoperability**: HAPI FHIR for standardized healthcare data exchange.
- **Security & Secrets**: HashiCorp Vault with Transit and Database Secrets Engines for AES-256 encryption and dynamic credentials.
- **Storage & Backup**: PostgreSQL for relational data and AWS S3 Object Lock for 10-year immutable data retention.

## Rationale
Independent Vault clusters deployed across hybrid environments eliminate cross-cloud network partition risks, guaranteeing 99.99% availability. Client-side SDK caching and automated secret rotation maintain sub-second EMR screen load performance while strictly enforcing HIPAA and GDPR compliance.