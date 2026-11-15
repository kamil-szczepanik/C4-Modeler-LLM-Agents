## Overview
The Patient Notification Service is a microservice within the Clinic Management System that asynchronously dispatches secure, compliant patient alerts and appointment reminders. It ensures 99.99% availability and strict adherence to HIPAA and GDPR regulations.

## Key Elements
- Notification Router Component (Spring Cloud Gateway/Routing)
- Channel Adapter Component (Apache Camel)
- Template Engine Component (Thymeleaf)
- Delivery Status Tracker Component (Redis Streams)
- Consent & Preference Manager Component (Redis caching layer)

## Relationships
- Core Business Services invokes Notification Router via gRPC with mTLS and OAuth2/JWT.
- Notification Router queries Consent & Preference Manager via local method calls.
- Channel Adapter calls external providers (Twilio for SMS, SendGrid for Email) via HTTPS/SMTP over TLS 1.3.
- Delivery Status Tracker processes retries and Dead Letter Queues via CockroachDB and Redis.

## Technology Stack
- Java / Spring Boot: Core framework chosen for enterprise reliability and extensive security ecosystem.
- Redis & CockroachDB: Used for streams, consent caching, DLQ, and AES-256 encrypted data storage to ensure high availability and durability.
- Apache Camel: Integrates third-party messaging providers while decoupling external latency from core transactions.
- Resilience4j: Implements circuit breaking and fallbacks to handle external gateway outages.

## Rationale
This architecture uses active-active components and decoupling patterns to meet the stringent 99.99% uptime requirement. Enforcing strict PHI minimization, mTLS, and data masking ensures complete HIPAA and GDPR compliance.