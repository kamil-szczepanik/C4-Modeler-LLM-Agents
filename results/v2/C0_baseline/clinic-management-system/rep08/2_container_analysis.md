## Overview
The Clinic Management System is a hybrid cloud platform designed for medium-sized hospitals and clinics to manage patient admissions, EMRs, scheduling, and billing. It ensures high availability (99.99%), strict HIPAA/GDPR compliance, and uninterrupted clinical workflows during network partitions.

## Key Elements
- **Users**: Patients, Clinicians, Administrative Staff, Compliance Officers / Auditors
- **External Systems**: Identity Provider (IdP), External Lab & Imaging Systems, Payment Gateway / Insurance Clearinghouse, SIEM & Immutable Cold Storage
- **Containers**: API Gateway / Reverse Proxy (Envoy/NGINX), Patient Portal App (React/Node.js), Clinical Core Service (Go/Spring Boot with Redis/RocksDB edge cache), Interoperability Engine (HAPI FHIR/Apache Camel), Billing & Claims Service (Spring Boot), Sync Orchestrator

## Relationships
- **Patient Portal to API Gateway**: HTTPS / TLS 1.3
- **API Gateway to Internal Services**: gRPC over mTLS (Istio service mesh)
- **Clinical Core to External Lab Systems**: HL7 FHIR APIs
- **Billing Service to Payment Gateway**: Asynchronous messaging via RabbitMQ
- **All Services to SIEM**: Encrypted audit log streaming

## Technology Stack
- **Compute**: On-Premises Kubernetes & AWS (`eu-central-1`)
- **Languages/Frameworks**: Go, Spring Boot, React, Node.js
- **Databases & Caching**: PostgreSQL (AES-256 at rest), Redis / RocksDB (Edge Cache StatefulSets)
- **Messaging & Integration**: RabbitMQ, HAPI FHIR / Apache Camel
- **Security & Networking**: Envoy/NGINX, Istio, HashiCorp Vault / AWS KMS, OAuth2/JWT
- **Observability & DevOps**: OpenTelemetry, Prometheus, ArgoCD, LitmusChaos

## Rationale
Container segmentation and Istio mTLS enforce least-privilege access and zero-trust security required for HIPAA/GDPR compliance. The local edge cache sidecar and Sync Orchestrator guarantee 99.99% availability by maintaining offline EMR and scheduling workflows during hybrid network partitions.