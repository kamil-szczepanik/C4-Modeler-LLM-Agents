## Overview
• Manages patient admissions, EMR, scheduling, and billing for clinics.
• Ensures 99.99% availability and HIPAA/GDPR compliance via a hybrid architecture.

## Key Elements
• Clinicians, Doctors, Receptionists, Billing Specialists, Compliance Officers
• Nginx Web App, API Gateway (Kong/Envoy)
• Core Clinical & EMR Container, Billing & Claims Container
• HL7 FHIR Interoperability Container, Patient Portal Container
• Sync/Replication Container (Apache Kafka KRaft, Debezium CDC)
• Audit Sidecar Container (OpenTelemetry, HashiCorp Vault)
• Internal Components: Transactional Outbox Poller, Payload Encryption Interceptor, Conflict Resolution Engine, Quarantine & Audit Manager

## Relationships
• Core Clinical Database -> Transactional Outbox Poller: Logical Replication / JDBC
• Sync/Replication Container -> EU Central-1 Cloud: TLS-encrypted Kafka MirrorMaker 2 over VPN/DirectConnect
• Payload Encryption Interceptor -> HashiCorp Vault: REST / TLS 1.3
• Conflict Resolution Engine -> Audit Sidecar: gRPC over localhost

## Technology Stack
• Go / Java: High-performance backend processing and middleware
• Apache Kafka (KRaft mode): Low-latency event streaming and hybrid replication
• Debezium: Change Data Capture (CDC) for transactional outbox pattern
• HashiCorp Vault: Envelope encryption (AES-256) and DEK management
• OpenTelemetry & Prometheus: Observability, metrics, and lag monitoring

## Rationale
• Active-active hybrid deployment and Kafka KRaft replication ensure RPO = 0 and 99.99% availability during network partitions.
• Envelope encryption with Vault and secure quarantine topics satisfy strict HIPAA and GDPR data protection mandates.