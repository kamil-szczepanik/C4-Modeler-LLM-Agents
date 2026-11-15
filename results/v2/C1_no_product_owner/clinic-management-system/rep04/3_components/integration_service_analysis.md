## Overview
The Integration Service component securely connects the Clinic Management System to external lab and imaging providers. It translates, encrypts, and validates clinical data streams to ensure regulatory compliance and high availability.

## Key Elements
- FHIR Adapter Component (Spring Boot / Apache Camel)
- Outbox Processor Component (Spring Boot)
- Secure Transport Client Component (HttpClient / Netty)
- Payload Sanitizer & Encryption Component (Spring Security / JOSE)
- Event Broker (Apache Kafka / RabbitMQ)
- External Lab & Imaging Systems
- WORM Audit Log Store

## Relationships
- FHIR Adapter -> Secure Transport Client: Dispatches standardized payloads [Internal Method Calls]
- FHIR Adapter -> Payload Sanitizer & Encryption: Sanitizes and encrypts clinical payloads [Internal Method Calls]
- Payload Sanitizer & Encryption -> Outbox Processor: Hands off encrypted domain events [Internal Method Calls]
- Outbox Processor -> Event Broker: Publishes domain events [Kafka Protocol]
- Secure Transport Client -> External Lab & Imaging Systems: Exchanges data [HL7 FHIR over HTTPS with mTLS]

## Technology Stack
- Spring Boot & Apache Camel: Chosen for robust enterprise integration and native FHIR support.
- Spring Security & JOSE: Utilized for JSON Web Encryption (JWE) of PHI payloads.
- Apache Kafka / RabbitMQ: Provides reliable, asynchronous event streaming.
- Kubernetes (on-prem-k8s): Deployed locally to minimize WAN dependency and meet availability targets.
- HSM-backed KMS: Ensures secure key management for 10-year data retention compliance.

## Rationale
This architecture ensures HIPAA and GDPR compliance through strict mTLS, JWE payload encryption, and immutable WORM audit logs. Deploying the service locally on Kubernetes mitigates WAN latency risks to achieve 99.99% availability.