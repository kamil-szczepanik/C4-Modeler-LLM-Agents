## Overview
The Clinic Management System manages patient admissions, EMRs, scheduling, and billing for clinics. The Notification Container handles system alerts while ensuring HIPAA and GDPR compliance.

## Key Elements
- Notification Router Component (Go)
- Channel Dispatcher Components (Go, Twilio API, SMTP, Firebase/APNS)
- Preference & Consent Manager Component (Go)
- Apache Kafka & PostgreSQL Database
- External Providers (Twilio, SMTP, APNS, IdP, HashiCorp Vault)

## Relationships
- API Gateway -> Preference & Consent Manager Component: Routes user preference updates [gRPC/HTTPS]
- Notification Router Component -> Apache Kafka: Consumes inbound notification events [Kafka protocol, TLS + SASL]
- Preference & Consent Manager -> PostgreSQL Database: Queries consent records [SQL/TLS]
- Channel Dispatcher Components -> External SMS/Email/Push Providers: Dispatches alerts [HTTPS/SMTP, TLS 1.3]
- Notification Container -> Audit & Compliance Container: Streams audit events [Kafka, TLS + SASL]

## Technology Stack
- Go: Chosen for optimal concurrency, low memory footprint, and worker pool efficiency.
- TLS 1.3 & AES-256: Mandatory for data in transit and encrypted storage to meet HIPAA and GDPR standards.
- HashiCorp Vault: Secure runtime injection of third-party API keys and credentials.
- Apache Kafka: Asynchronous event ingestion with TLS + SASL for reliable messaging.

## Rationale
This architecture ensures 99.99% availability and high throughput for time-sensitive clinical communications. Strict PII/PHI sanitization, encryption, and consent management fulfill all healthcare regulatory constraints.