## Overview
The Clinic Management System is a hybrid cloud platform designed for medium-sized hospitals and clinics to manage patient admissions, electronic medical records, scheduling, and billing. It provides high availability, stringent compliance, and robust interoperability for clinical IT operations.

## Key Elements
- Integration / Adapter Container (Anti-Corruption Layer)
- Core Domain Containers
- Asynchronous Message Broker (Apache Kafka / RabbitMQ)
- External Labs, Imaging Systems, and Insurance Providers
- Centralized Audit Logging Service

## Relationships
- External Labs/Imaging -> Integration / Adapter Container: Interfaces using HL7 FHIR over REST [HL7 FHIR over REST]
- Integration / Adapter Container -> Asynchronous Message Broker: Publishes domain events [Transactional Outbox Pattern]
- Integration / Adapter Container -> Centralized Audit Logging Service: Emits distributed traces and logs [W3C Trace Context]

## Technology Stack
- HL7 FHIR over REST: Standardized clinical interoperability protocol
- Apache Kafka / RabbitMQ: Asynchronous message broker ensuring at-least-once delivery
- JSONata / Liquid Templates: Declarative mapping rules for schema translations
- W3C Trace Context: Distributed tracing across hybrid boundaries

## Rationale
This architecture ensures 99.99% availability and HIPAA/GDPR compliance via resilient integration patterns like the Anti-Corruption Layer, Transactional Outbox, and circuit breakers. It isolates external vendor volatility while maintaining a 10-year data retention audit trail.