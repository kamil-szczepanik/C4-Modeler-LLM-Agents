## Overview
The Clinic Management System manages patient admissions, electronic medical records, scheduling, and billing for medium-sized hospitals and clinics. The hybrid architecture guarantees 99.99% availability, HIPAA/GDPR compliance, and seamless interoperability.

## Key Elements
- Patients, Clinical Staff, Hospital Administrators
- Global Anycast Load Balancer and API Gateways (Kong)
- Patient Portal (Node.js, React)
- EMR & Scheduling Service (Java Spring Boot)
- Billing & Insurance Claim Service (Python FastAPI)
- HL7 FHIR Interoperability Engine (Apache Camel)
- Database Tier (PostgreSQL with PgBouncer, AES-256)
- Messaging & Audit Layer (Apache Kafka, FluentBit, S3)
- Infrastructure & Mesh (Kubernetes, AWS eu-central-1, on-prem-k8s, Envoy sidecar)
- Third-Party Insurance Clearinghouses

## Relationships
- Global Anycast Load Balancer and API Gateways -> Billing & Insurance Claim Service [HTTPS]
- Patient Portal -> Billing & Insurance Claim Service [gRPC over mutual TLS]
- Billing & Insurance Claim Service -> Messaging & Audit Layer [Apache Kafka]
- Billing & Insurance Claim Service -> Database Tier [Encrypted TCP]
- Claim Generation Engine -> Clearinghouse Integration Adaptor [Asyncio/HTTPS with mTLS]

## Technology Stack
- Python FastAPI: High-performance framework for the billing and insurance service.
- PostgreSQL & SQLAlchemy: Relational data persistence with AES-256 encryption at rest.
- Apache Kafka: Asynchronous event streaming and ledger updates.
- Kubernetes: Hybrid container orchestration across on-prem and AWS eu-central-1.
- OpenTelemetry & Prometheus: Distributed tracing and metric monitoring.

## Rationale
The hybrid architecture leverages Kubernetes and active-active replication to meet strict 99.99% availability and HIPAA/GDPR data protection mandates. Asynchronous event-driven messaging via Apache Kafka ensures high throughput and fault tolerance for critical clinical workflows.