## Overview
The Clinic Management System is a hybrid-cloud platform designed to manage patient admissions, EMRs, scheduling, and billing for clinics while ensuring HIPAA and GDPR compliance. It provides high availability (99.99%) and secure interoperability with external clinical and billing systems.

## Key Elements
- FHIR Transformer Engine (Apache Camel/Java)
- External Protocol Adapter
- Resilience & Circuit Breaker Manager (Resilience4j)
- Outbox Message Publisher
- DLQ Exception Router
- Message Broker (Kafka)
- External Lab & Imaging Systems

## Relationships
- FHIR Transformer Engine -> External Protocol Adapter: Forwards normalized payloads [Direct Route]
- Resilience & Circuit Breaker Manager -> External Protocol Adapter: Protects against external cascading failures [In-memory wrapper]
- Outbox Message Publisher -> Message Broker (Kafka): Publishes integration audit events [TCP/Kafka]
- DLQ Exception Router -> Message Broker (Kafka): Routes poisoned or failed payloads to the DLQ topic [TCP/Kafka]
- External Protocol Adapter -> External Lab & Imaging Systems: Exchanges health data [mTLS over HTTPS/REST]

## Technology Stack
- Apache Camel: Selected for robust enterprise integration patterns and out-of-the-box routing for HL7 FHIR transformations.
- Resilience4j: Implemented for circuit breaking, timeouts, and backoff retry policies.
- OpenTelemetry: Utilized with W3C trace context for distributed tracing across hybrid boundaries.
- AES-GCM / KMS: Applied for envelope encryption of PHI payloads in the DLQ.

## Rationale
This architecture leverages Apache Camel and Resilience4j to guarantee resilient, fault-tolerant external communications without degrading core clinical performance. Strict cryptographic sanitization and mTLS protocols fulfill stringent HIPAA and GDPR compliance mandates across hybrid infrastructure.