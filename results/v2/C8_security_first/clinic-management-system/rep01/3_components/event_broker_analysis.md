## Overview
[The Clinic Management System manages patient admissions, EMR, scheduling, and billing for medium-sized hospitals and clinics. It ensures high availability, strict HIPAA/GDPR compliance, and long-term data retention across a hybrid cloud architecture.]

## Key Elements
- Users: Clinic Receptionist/Admin, Clinician, Billing Specialist, Patient, Hospital/Clinic Administrator, External Auditors
- External Systems: Lab & Imaging Systems, Insurance Claim Processors, Identity Provider (IdP)
- Containers: Envoy/NGINX API Gateway, Patient Intake Container, Scheduling Engine Container, EMR Workspace Container, Billing & Claims Container, Integration & FHIR Mediator, Primary Database (PostgreSQL with Citus), Event Broker (Redpanda)
- Event Broker Components: Kafka API Frontend, Storage & Raft Consensus Engine, Schema Registry, Partition Manager, Tiered Storage Encryption Interceptor, GDPR Purge & Tombstone Controller

## Relationships
- Inter-microservice communication: TCP/Kafka Protocol (TLS 1.3 with mTLS)
- External integrations: HL7 FHIR APIs for lab and imaging systems
- Administrative access: HTTPS for Hospital/Clinic Administrators accessing the DLQ Dashboard

## Technology Stack
- Event Broker: Redpanda (C++ thread-per-core core) for high-performance streaming
- Authentication/Security: mTLS, SASL/SCRAM, AES-256 encryption-in-transit (TLS 1.3) and at-rest, AWS KMS/on-prem HSM
- Storage: Raft consensus logs with S3-compatible Tiered Storage for 10-year retention
- Validation: Integrated Schema Registry for Apache Avro/JSON schemas
- Observability: OpenTelemetry, Prometheus, Grafana Mimir/Tempo, Falco

## Rationale
[The hybrid active-active architecture with Redpanda ensures 99.99% uptime and low-latency event processing for critical clinical workflows. Client-side envelope encryption and dedicated compliance controllers satisfy strict HIPAA and GDPR mandates.]