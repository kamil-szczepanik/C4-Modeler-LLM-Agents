## Overview
The Clinic Management System is a clinical IT platform that manages patient admissions, electronic medical records, scheduling, and billing for medium-sized hospitals and clinics. It ensures high availability, security, and interoperability across hybrid cloud environments.

## Key Elements
- **API Gateway (NGINX / Envoy)**: Routes incoming requests.
- **Integration Service (Apache Camel / Spring Integration)**: Handles HL7 FHIR translations.
- **FHIR Router & Validator Component**: Validates payloads against US Core FHIR profiles.
- **HL7 v2/v3 Translation Engine Component**: Converts domain events to legacy HL7 messages using HAPI FHIR / HAPI HL7.
- **Outbound Dispatcher Component**: Manages retries and circuit breaking using resilience4j.
- **Integration Audit & DLQ Component**: Captures failed payloads for compliance auditing and reconciliation.
- **PostgreSQL Database**: Stores transactional and audit data with AES-256 encryption.

## Relationships
- **API Gateway -> Integration Service**: Routes requests via gRPC over mTLS.
- **FHIR Router -> HL7 Translation Engine**: Transforms message formats in-memory.
- **Outbound Dispatcher -> External Lab & Imaging Systems**: Transmits diagnostics via HL7 FHIR / v2 over HTTPS/TLS 1.3.
- **Outbound Dispatcher -> Integration Audit & DLQ Component**: Forwards failed delivery payloads via asynchronous messaging.
- **Integration Audit & DLQ Component -> PostgreSQL Database**: Stores failed transaction logs via JDBC over TLS 1.3.

## Technology Stack
- **Apache Camel / Spring Integration**: Powers the Integration Service for routing and integration patterns.
- **HAPI FHIR / HAPI HL7**: Provides clinical message translation.
- **Resilience4j**: Ensures reliable outbound dispatching through circuit breaking and retries.
- **PostgreSQL**: Guarantees secure, persistent storage with AES-256 encryption for HIPAA and GDPR compliance.

## Rationale
This architecture ensures 99.99% availability and robust interoperability with external lab and imaging systems via HL7 FHIR standards. It meets strict healthcare security, audit, and retention constraints using encrypted storage and dead-letter queuing.