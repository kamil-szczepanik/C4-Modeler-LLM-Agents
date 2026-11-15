## Overview
The Notification Worker is a Go-based microservice responsible for asynchronous, multi-channel (SMS, Email, Push) delivery of patient and staff communications within the Clinic Management System. It ensures secure, HIPAA-compliant messaging with dynamic templating, dead-letter queue persistence, and strict PHI payload sanitization.

## Key Elements
- **Notification Worker (Go)**: Container service handling event consumption, preference routing, and dispatching.
- **Kafka Event Consumer**: Subscribes to input event streams.
- **Preference & Routing Engine**: Enforces PHI redaction and maps user preferences.
- **Template Engine Component**: Renders localized templates using dynamic object storage.
- **Channel Dispatcher Adapters**: Interfaces for SMTP and Twilio/APNS SDKs.
- **DLQ & Audit Router**: Manages retry logic and failed message persistence.

## Relationships
- **Notification Worker -> Apache Kafka**: Consumes raw notification events and routes failed deliveries [TCP].
- **Notification Worker -> PostgreSQL**: Persists permanently failed notifications for administrative review [TCP/5432].
- **Notification Worker -> S3-compatible Storage**: Fetches dynamic message templates [HTTPS/443].
- **Notification Worker -> SMTP Server**: Sends email notifications [TLS / TCP/587].
- **Notification Worker -> Twilio/APNS APIs**: Delivers SMS and mobile push notifications [HTTPS / REST/443].

## Technology Stack
- **Go**: Chosen for high-throughput concurrency and low memory footprint in worker processes.
- **Apache Kafka**: Event streaming backbone ensuring decoupled, scalable message ingestion.
- **PostgreSQL**: Relational storage for permanent dead-letter queue (DLQ) auditing and administrative review.
- **S3-compatible Storage**: External storage for dynamic message templates enabling non-code updates.
- **Kubernetes**: Orchestration platform utilizing Horizontal Pod Autoscalers driven by Kafka consumer lag.

## Rationale
This architecture fits requirements by decoupling asynchronous communications via Kafka to guarantee 99.99% availability without blocking primary clinical workflows. Furthermore, it enforces HIPAA and GDPR compliance through strict PHI payload sanitization, local template caching, and persistent DLQ auditing.