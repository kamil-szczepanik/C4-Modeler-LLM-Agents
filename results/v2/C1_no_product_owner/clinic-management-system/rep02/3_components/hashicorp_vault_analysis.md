## Overview
The Clinic Management System is a hybrid cloud platform designed to securely manage patient admissions, electronic medical records (EMR), scheduling, and billing for healthcare providers. It ensures high availability, strict regulatory compliance, and seamless interoperability with external clinical systems.

## Key Elements
*   **Users:** Patient, Clinician/Staff
*   **External Systems:** External Lab & Imaging Systems, Payment Gateway / Insurance Clearinghouse
*   **Containers:** Envoy (API Gateway), Istio (Service Mesh), Patient & Scheduling Service (Node.js/Go), EMR Core Service (Java/Spring Boot), Billing & Integration Service (Python/FastAPI), PostgreSQL with Patroni, NATS / RabbitMQ and AWS Kafka, WORM-compliant S3 / MinIO, HashiCorp Vault
*   **Vault Components:** Secrets Engine Component, Auth Method Component, Audit Device Component, Transit Secrets Engine Component, Raft Storage Manager Component

## Relationships
*   *EMR Core Service* -> *Auth Method Component*: Authenticates via **HTTPS/REST (JWT/Token)** over **mTLS**.
*   *EMR Core Service* -> *Transit Secrets Engine Component*: Requests cryptographic operations via **mTLS/HTTPS**.
*   *Vault Nodes* -> *Vault Nodes (Raft)*: Replicates encrypted state via **mTLS gRPC/TCP**.
*   *Audit Device Component* -> *WORM-compliant S3 / MinIO*: Streams immutable audit logs via **HTTPS**.

## Technology Stack
*   **Hybrid Infrastructure:** Kubernetes (on-prem) and AWS (eu-central-1) for active-active multi-region deployment.
*   **Service Mesh & Gateway:** Istio and Envoy for mutual TLS and traffic management.
*   **Databases:** PostgreSQL with Patroni for high availability relational data storage.
*   **Secret Management:** HashiCorp Vault with Integrated Raft Storage and AWS KMS / on-prem HSM Auto-Unseal.
*   **Interoperability:** HL7 FHIR APIs for integration with lab and imaging systems.

## Rationale
This hybrid architecture guarantees HIPAA and GDPR compliance through AES-256 encryption, immutable audit trails, and strict IAM boundaries enforced by HashiCorp Vault and Istio. The active-active multi-region setup with native Raft storage and auto-unseal mechanisms ensures 99.99% high availability and fault tolerance.