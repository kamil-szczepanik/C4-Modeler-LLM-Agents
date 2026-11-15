## Overview
The Clinic Management System provides patient registration, EMR, scheduling, and billing for healthcare facilities with high availability. It uses a hybrid architecture spanning on-premise Kubernetes and AWS (`eu-central-1`) to meet strict HIPAA and GDPR mandates.

## Key Elements
- **Users**: Patient, Clinician / Doctor, Receptionist / Admin, Billing Specialist, Compliance / IT Auditor, Hospital Executive
- **External Systems**: External Lab & Imaging Systems, Payment Gateway & Insurance Clearinghouse, Identity Provider (IdP), Business Analytics / Reporting Service
- **Containers**: Frontend (React, TypeScript), Edge (Kong / Envoy), Clinical Service (Go), Scheduling (Node.js), Billing (Java/Spring Boot), Audit Service (Go), Integration Service (Go), Kafka/RabbitMQ, Databases (PostgreSQL, MongoDB, Redis), Object Storage (MinIO / Ceph)
- **Object Storage Components**: Storage Gateway, Encryption & Key Management (Vault/AWS KMS), Lifecycle & Tiering Engine, Audit & Compliance Guardrail

## Relationships
- **Clinical Service -> Storage Gateway**: Uploads/retrieves EMR assets via HTTPS / S3 API
- **Storage Gateway -> Audit & Compliance Guardrail**: Validates immutability policies via Internal gRPC
- **Storage Gateway -> Encryption Component**: Applies AES-256 via Internal gRPC
- **Storage Gateway -> MinIO / Ceph Cluster**: Persists objects across hybrid nodes via S3 API

## Technology Stack
- **MinIO / Ceph**: Cloud-agnostic S3-compatible backend ensuring identical hybrid behavior
- **AES-256 & WORM**: Mandatory encryption and Write-Once-Read-Many object locking for compliance
- **Prometheus & PagerDuty**: Metrics, tracing, and alerting for 99.99% availability SLAs
- **Go & Java**: High-performance backend runtime stack

## Rationale
This hybrid architecture uses cloud-agnostic S3 storage with automated tiering and WORM locking to satisfy strict 10-year retention and compliance mandates. Component-level separation guarantees sub-second active record retrieval and robust disaster recovery across on-premise and cloud environments.