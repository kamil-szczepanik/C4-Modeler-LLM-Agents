## Overview
The Clinic Management System is a hybrid cloud platform designed to manage patient admissions, electronic medical records, scheduling, and billing for healthcare clinics. It ensures high availability, strict HIPAA/GDPR compliance, and seamless interoperability.

## Key Elements
- **Users**: Billing Specialist, Clinic Administrator
- **External Systems**: Payment Gateway / Insurance Clearinghouse, External Lab & Imaging Systems, Audit Archival / SIEM System
- **Containers**: Billing & Integration Service (FastAPI), PostgreSQL, RabbitMQ
- **Components**: Billing API Controller, Claim Processing Engine, FHIR Integration Adapter, Payment & Reconciliation Worker, Billing Data Repository Layer

## Relationships
- Billing API Controller -> Claim Processing Engine: Invokes claim generation with user context [Python async call]
- Claim Processing Engine -> Billing Data Repository Layer: Persists data and audit logs [SQLAlchemy / AES-256]
- Payment & Reconciliation Worker -> Payment Gateway: Executes financial transactions [HTTPS/REST with mTLS & OAuth2]
- FHIR Integration Adapter -> External Lab & Imaging Systems: Transmits diagnostic data [HL7 FHIR APIs over mTLS]
- Payment & Reconciliation Worker <-> RabbitMQ: Processes billing events with DLQ fallback [AMQP]

## Technology Stack
- **FastAPI / Python**: Chosen for high-throughput asynchronous API handling and rapid endpoint development.
- **PostgreSQL**: Provides robust relational data storage with AES-256 encryption at rest.
- **RabbitMQ**: Enables reliable asynchronous event-driven messaging with dead-letter queue (DLQ) retry policies.
- **SQLAlchemy ORM**: Manages secure database mapping and connection management.
- **HL7 FHIR**: Standardizes interoperability with external clinical and imaging systems.

## Rationale
This architecture uses an asynchronous, component-decomposed microservices pattern to guarantee 99.99% uptime and low-latency billing operations. Strict mTLS, tokenization, and audit streaming satisfy rigorous healthcare security mandates.