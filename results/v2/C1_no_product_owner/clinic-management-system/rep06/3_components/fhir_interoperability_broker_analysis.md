## Overview
The Clinic Management System is a hybrid cloud-based clinical IT platform managing patient admissions, EMRs, scheduling, and billing. It provides high availability, stringent HIPAA/GDPR compliance, and interoperability for medium-sized healthcare facilities.

## Key Elements
- **FHIR API Route Controller**: Exposes standard RESTful FHIR endpoints and validates incoming payloads.
- **Transformation Engine**: Maps internal domain models to HL7 FHIR resources (R4/STU3).
- **External Connector Client**: Manages outbound mTLS connections, retries, and circuit-breaking.
- **Audit & Compliance Interceptor**: Captures immutable audit logs and streams redacted events.
- **Kubernetes (on-prem-k8s / eu-central-1)**: Hybrid hosting environment for stateless deployments.

## Relationships
- **FHIR API Route Controller -> Transformation Engine**: Passes raw payloads [In-memory Java objects]
- **Transformation Engine -> External Connector Client**: Sends mapped FHIR bundles [In-memory]
- **FHIR API Route Controller -> Audit & Compliance Interceptor**: Triggers audit event capture [In-memory]
- **Audit & Compliance Interceptor -> Central SIEM/Audit Store**: Streams redacted audit logs [Syslog over TLS / Kafka]
- **External Connector Client -> External Lab / Imaging Systems**: Exchanges lab and imaging data [HL7 FHIR APIs over HTTPS with mTLS]

## Technology Stack
- **Apache Camel**: Core integration framework for routing, protocol translation, and REST DSL.
- **Spring AOP / Apache Camel Interceptor**: Implements audit capture mechanisms.
- **Resilience4j**: Handles circuit breaking and retry logic for external dependencies.
- **Kafka / JMS**: Powers asynchronous streaming and persistent disk-backed Dead Letter Queues (DLQs).
- **OAuth 2.0 / JWT / SMART-on-FHIR**: Enforces API authentication, scope validation, and identity verification.
- **AES-256 & TLS 1.3**: Secures data at rest (including DLQ volumes) and in transit.

## Rationale
This architecture uses Apache Camel and Kubernetes to ensure 99.99% active-active uptime and robust hybrid scaling. Integrated encryption, mTLS, and cryptographic audit interceptors directly satisfy strict HIPAA and GDPR compliance mandates.