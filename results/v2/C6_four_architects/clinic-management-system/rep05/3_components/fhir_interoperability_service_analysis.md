## Overview
The Clinic Management System is a hybrid cloud platform designed to manage patient admissions, electronic medical records, scheduling, and billing for medium-sized hospitals and clinics. It ensures high availability, strict HIPAA/GDPR compliance, and interoperability with external clinical systems.

## Key Elements
- **FHIR API Controller (FastAPI Router)**: Handles incoming HTTP/REST requests and enforces JWT-based authorization scopes.
- **Resource Transformer Engine**: Maps internal domain models to/from standard HL7 FHIR JSON resources.
- **Terminology Mapper**: Translates local clinic codes to LOINC and SNOMED-CT reference tables.
- **Data Sync Outbox Client & Resilience Manager**: Interfaces with Apache Kafka and uses SQLite/WAL for at-least-once delivery.
- **External System Connector**: Manages outbound HTTP/2 client calls to external systems using mTLS.
- **Audit & Compliance Interceptor**: Captures requests, hashes PHI, and emits immutable audit events.

## Relationships
- **FHIR API Controller** -> **Resource Transformer Engine**: Direct async/await method calls.
- **Resource Transformer Engine** -> **Terminology Mapper**: Direct method calls with **Distributed Cache (Redis)** lookup.
- **External System Connector** -> **External Lab & Imaging Systems**: REST over HTTPS via mTLS.
- **Data Sync Outbox Client** -> **Message Broker (Apache Kafka)**: Publishes asynchronous events via SASL/SCRAM over TLS.

## Technology Stack
- **Python / FastAPI**: Core framework for the FHIR Interoperability Service container due to high async performance.
- **`fhir.resources` Python Library**: Ensures strict adherence to HL7 FHIR R4 specifications.
- **Redis Enterprise**: Provides low-latency caching for terminology mappings.
- **SQLite with WAL**: Enables localized transactional outbox persistence for resilience.
- **Apache Kafka**: Manages reliable, asynchronous event distribution.

## Rationale
This architecture ensures low-latency data transformations (<1s P95) and robust resilience patterns to meet strict 99.99% uptime availability constraints. It isolates sensitive clinical workflows while maintaining end-to-end HIPAA and GDPR compliance through mTLS, AES-256 encryption, and immutable audit logging.