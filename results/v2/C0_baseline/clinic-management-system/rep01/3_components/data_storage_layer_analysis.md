## Overview
[The Clinic Management System manages patient admissions, EMRs, scheduling, and billing for healthcare clinics, ensuring HIPAA and GDPR compliance with 99.99% availability. It utilizes a hybrid cloud architecture spanning local Kubernetes clusters and AWS eu-central-1.]

## Key Elements
- Patients / Consumers
- Receptionists / Front Desk
- Clinicians / Doctors
- Billing Specialists
- Clinic Administrators
- Compliance Auditors / Data Protection Officers (DPOs)
- Lab & Imaging Systems, Insurance Payment Gateways, Identity Provider (IdP)
- API Gateway / Reverse Proxy (Kong / NGINX Ingress)
- Patient Portal (Next.js (TypeScript))
- Core Clinical Service (Java (Spring Boot))
- Billing & Scheduling Service (Node.js / TypeScript)
- Integration / Interoperability Service (Apache Camel / Spring Boot)
- Data Storage Layer (PostgreSQL v15+, PgBouncer, AWS S3 WORM Storage, HashiCorp Vault)
- Messaging & Observability Infrastructure (Apache Kafka, Prometheus, Grafana, OpenTelemetry, Istio, ArgoCD)

## Relationships
- Core Clinical Service -> Data Storage Layer: Reads and writes clinical data via TLS-encrypted SQL
- Billing & Scheduling Service -> Data Storage Layer: Reads and writes billing and schedule data via TLS-encrypted SQL
- Integration Service -> Lab & Imaging Systems: Exchanges clinical data via HL7 FHIR APIs
- Services -> Data Storage Layer: Connects securely via Istio mTLS and PgBouncer connection pooler

## Technology Stack
- PostgreSQL v15+: Relational storage with CloudNativePG for automated failover
- AWS S3 Object Lock (Compliance Mode): WORM storage ensuring 10-year retention for compliance audit logs
- HashiCorp Vault: Dynamic secret management and AES-256 envelope encryption at rest
- PgBouncer: Connection pooling for high-throughput concurrency
- Apache Kafka: Event streaming and messaging backbone

## Rationale
[The hybrid architecture balances strict HIPAA/GDPR security and 10-year data retention mandates with high-performance clinical workflows. A hybrid replication strategy and dedicated connection pooling ensure <1s P95 EMR load times while maintaining 99.99% availability.]