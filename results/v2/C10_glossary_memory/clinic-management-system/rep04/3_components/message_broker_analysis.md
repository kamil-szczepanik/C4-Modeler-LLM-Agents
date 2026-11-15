## Overview
- Clinic Management System: Hybrid cloud platform managing patient admissions, EMRs, scheduling, and billing for medium-sized clinics.
- Core Purpose: Ensures HIPAA/GDPR compliance, 99.99% uptime, and secure asynchronous messaging for clinical and billing workflows.

## Key Elements
- Entities: Patient, Clinician, Billing/Admin Staff, Compliance Officer, Lab & Imaging Systems, Insurance Clearinghouse / External Billing Provider.
- Containers: Patient Portal SPA/Mobile, Clinician/Admin Workspace SPA, API Gateway / BFF, Core Services Container, Billing Service Container, Integration Service Container, Audit & Compliance Logging Container, PostgreSQL & HL7 FHIR Compliant Data Stores, Message Broker.
- Message Broker Components: Ingestion & Authentication Gateway, Distributed Commit Log Engine, Offset & Consumer Group Coordinator.

## Relationships
- Patient, Clinician, Billing/Admin Staff, Compliance Officer -> API Gateway / BFF: HTTPS (TLS 1.3, OAuth2/OIDC, MFA)
- API Gateway / BFF -> Core Services Container: gRPC over mTLS
- API Gateway / BFF -> Billing Service Container: gRPC over mTLS
- Core Services Container -> PostgreSQL & HL7 FHIR Compliant Data Stores: JDBC (AES-256 at rest)
- Core Services Container -> Message Broker: Kafka Protocol over mTLS
- Billing Service Container -> Message Broker: Kafka Protocol over mTLS
- Integration Service Container -> Message Broker: Kafka Protocol over mTLS
- Clinic Management System -> Lab & Imaging Systems: HL7 FHIR over REST/JSON (TLS 1.3)
- Billing Service Container -> Insurance Clearinghouse / External Billing Provider: HTTPS / EDI X12

## Technology Stack
- Frontend: React/TypeScript for SPAs.
- Gateway: Envoy/Kong API Gateway.
- Backend Services: Java/Spring Boot (Core), Node.js/TypeScript (Billing), Apache Camel / Spring Integration (Integration & Audit).
- Databases & Storage: PostgreSQL with AES-256 at rest; WORM-compliant storage for audit logs.
- Message Broker: Apache Kafka with KRaft metadata quorum, AES-256 encryption at rest, and mTLS.
- Security & Infrastructure: Kubernetes (`on-prem-k8s` and AWS `eu-central-1`), HashiCorp Vault for ephemeral secrets, Prometheus for observability.

## Rationale
- Hybrid architecture ensures 99.99% uptime via active-active deployment and Kafka disaster recovery replication.
- Strict mTLS, AES-256 encryption, and topic-level ACLs guarantee HIPAA and GDPR compliance for PHI.