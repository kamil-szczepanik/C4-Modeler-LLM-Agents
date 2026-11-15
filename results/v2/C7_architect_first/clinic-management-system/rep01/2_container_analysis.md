## Overview
The Clinic Management System (CMS) manages patient admissions, EMRs, scheduling, and billing for healthcare providers. It provides a secure, highly available hybrid-cloud architecture ensuring strict HIPAA and GDPR compliance.

## Key Elements
* API Gateway / Edge Proxy (Kong/Envoy)
* Patient & Scheduling Service (Node.js/TypeScript)
* EMR Core Service (Java/Spring Boot)
* Billing Service (Python/FastAPI)
* FHIR Interoperability Service (Java/HAPI FHIR)
* Data Storage Layer (PostgreSQL with Row-Level Security, MinIO/AWS S3 Object Storage)
* Infrastructure & Security (Istio Service Mesh, HashiCorp Vault/AWS KMS, ArgoCD)

## Relationships
* Users -> API Gateway via HTTPS/REST
* API Gateway -> Internal Services via mTLS/gRPC
* EMR Core Service -> PostgreSQL via TLS/SQL with RLS
* FHIR Interoperability Service -> External Lab & Imaging Systems via HTTPS/TLS with client certificate pinning
* Billing Service -> External Payment Gateway & Insurance Clearinghouse via HTTPS

## Technology Stack
* Kubernetes: Hybrid deployment across on-prem-k8s and AWS eu-central-1 for high availability
* PostgreSQL: Primary-Replica topology with localized read caching for transactional integrity and low latency
* Istio: Service mesh providing mTLS and circuit breaking across hybrid boundaries
* Vault/AWS KMS: Envelope encryption for AES-256 data protection at rest
* ArgoCD: Declarative GitOps engine for hybrid infrastructure management

## Rationale
This architecture uses hybrid Kubernetes, Istio mTLS, and encrypted distributed storage to achieve 99.99% availability and robust HIPAA/GDPR compliance. Primary-replica replication and localized caching ensure sub-second EMR performance while maintaining strict data isolation.