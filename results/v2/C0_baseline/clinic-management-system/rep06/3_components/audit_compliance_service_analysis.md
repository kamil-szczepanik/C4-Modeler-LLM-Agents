## Overview
The Audit & Compliance Service ensures regulatory compliance for the Clinic Management System by enforcing immutable audit logging and data retention. It securely processes high-throughput audit streams and provides secure reporting and data request tools for compliance officers.

## Key Elements
- Compliance Officer (User)
- Audit & Compliance Service (Go container)
- Event Ingestion Controller (Go gRPC Server)
- Compliance Reporting Engine (Go Native Package)
- Retention Policy Enforcer (Go Worker)
- DSAR Query Processor (Go Native Package)
- Report Scheduler (Go Cron/Worker)
- Audit Data Repository (AWS S3 Object Lock & PostgreSQL)
- Asynchronous Buffer (NATS JetStream)
- Secrets Management (HashiCorp Vault)

## Relationships
- Core Clinical & EMR Service -> Asynchronous Buffer: Sends audit events [gRPC, mTLS]
- Billing & Claims Service -> Asynchronous Buffer: Sends audit events [gRPC, mTLS]
- Asynchronous Buffer -> Event Ingestion Controller: Streams audit events [gRPC]
- Retention Policy Enforcer -> AWS S3 Object Lock: Applies WORM policies [HTTPS, IAM]
- Compliance Officer -> Compliance Reporting Engine & DSAR Query Processor: Accesses reports and queries [HTTPS, JWT/RBAC]
- DSAR Query Processor -> Audit Data Repository: Queries metadata [SQL over TLS]

## Technology Stack
- Go: Chosen for low-latency, high-throughput event processing and microservice implementation
- AWS S3 Object Lock: Provides write-once-read-many (WORM) storage to satisfy the 10-year retention mandate
- PostgreSQL: Stores indexed metadata and queryable audit trails
- NATS JetStream: Acts as a durable asynchronous buffer for network partitioning resilience
- HashiCorp Vault: Manages customer-managed encryption keys (CMK) for data at rest

## Rationale
This architecture uses Go and an asynchronous buffering pattern to guarantee high performance and availability without risking clinical transaction failures. Immutable storage tiers and strict RBAC controls ensure adherence to HIPAA and GDPR compliance mandates.