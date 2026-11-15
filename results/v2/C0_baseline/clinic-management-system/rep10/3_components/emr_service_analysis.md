## Overview
- The system is an EMR Service container for the Clinic Management System designed to handle electronic medical records, clinical workflows, and HIPAA/GDPR-compliant data handling.
- Its core purpose is to provide clinicians with sub-second patient record access while ensuring immutable auditing, cryptographic security, and interoperability.

## Key Elements
- EMR API Controller (Go / Fiber)
- Clinical Workflow Engine (Go)
- Audit & Compliance Logger (Go)
- Data Access Repository (Go with `pgx`)
- Patient Consent & Preference Manager (Go)
- FHIR Serialization Mapper (Go)
- PostgreSQL (Encrypted with AES-256)
- RabbitMQ Message Broker
- HashiCorp Vault

## Relationships
- API Gateway -> EMR API Controller: Routes EMR requests [mTLS / REST / JSON over HTTPS]
- EMR API Controller -> Patient Consent & Preference Manager: Evaluates consent policies [Go interface]
- EMR API Controller -> Clinical Workflow Engine: Handles validated clinical notes [In-process function calls]
- Clinical Workflow Engine -> Audit & Compliance Logger: Generates immutable audit trails [Asynchronous event emission / Go channels]
- Clinical Workflow Engine -> Data Access Repository: Interfaces with storage [SQL over TLS 1.3]
- Clinical Workflow Engine -> FHIR Serialization Mapper: Transforms clinical models [In-process transformation]
- FHIR Serialization Mapper -> RabbitMQ: Publishes FHIR clinical events [AMQP over TLS 1.3]
- Data Access Repository -> PostgreSQL: Persists data via Transactional Outbox Pattern [SQL / TLS 1.3]
- Pods -> HashiCorp Vault: Injects secrets via Kubernetes CSI Secrets Store Provider [API / TLS]

## Technology Stack
- Go / Fiber: Chosen for low-latency request handling and high throughput.
- PostgreSQL (`pgx`): Utilized for robust relational data storage and transactional outbox support.
- RabbitMQ: Employed for reliable message brokering using AMQP over TLS 1.3.
- HashiCorp Vault: Selected for dynamic database credentials and cryptographic key management.
- OpenTelemetry: Implemented for distributed tracing to enforce sub-second P95 performance metrics.

## Rationale
- This architecture uses Go-based modular components to guarantee sub-second screen loads (P95 < 1s) while maintaining strict high availability (99.99%).
- It enforces robust HIPAA and GDPR compliance through local ABAC, mTLS, AES-256 storage, and tamper-evident dual-write audit logs.