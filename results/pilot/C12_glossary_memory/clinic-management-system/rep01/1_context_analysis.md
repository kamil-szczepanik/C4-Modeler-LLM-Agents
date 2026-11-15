## Overview
The Clinic Management System is a hybrid cloud clinical IT solution designed to manage patient admissions, electronic medical records, appointment scheduling, and billing for medium-sized hospitals and clinics. It ensures high availability, strict regulatory compliance, and seamless interoperability with external healthcare systems.

## Key Elements
- **Users**: Front Desk Staff, Clinicians, Billing Specialists, Patients, Clinic Administrators, Practice Managers
- **Frontends**: Web Application Frontend, Patient Portal Mobile/Web Client
- **Core Services**: Patient Registration, Appointment Scheduling, EMR, Billing, Analytics Dashboards
- **Integration & Infrastructure**: API Gateway, Apache Kafka Event Streaming Bus, CockroachDB Distributed Database
- **External Systems**: Laboratory Information Systems (LIS), PACS Imaging Archives, Insurance Payment Gateways

## Relationships
- Users to Frontends via HTTPS (TLS 1.3) with OAuth 2.0 / OIDC and MFA
- Frontends to Core Services via REST and GraphQL
- Core Services to External Systems via HL7 FHIR APIs and secure mutual TLS (mTLS)
- Internal microservices communication secured via SPIFFE/SPIRE-based mTLS and envelope encryption

## Technology Stack
- **Compute**: Hybrid deployment across On-Premises Kubernetes and AWS (`eu-central-1`) for active-active redundancy
- **Database**: CockroachDB for distributed, active-active data persistence ensuring zero-data-loss failover
- **Messaging**: Apache Kafka for asynchronous event streaming and HL7 FHIR integration
- **Security**: AES-256 storage encryption, WORM storage for immutable audit logs, OAuth 2.0 / OIDC authentication

## Rationale
This hybrid active-active architecture guarantees 99.99% availability and meets sub-second P95 performance targets for EMR access. Robust encryption, WORM storage, and strict access controls ensure complete HIPAA and GDPR compliance while supporting a 10-year data retention mandate.