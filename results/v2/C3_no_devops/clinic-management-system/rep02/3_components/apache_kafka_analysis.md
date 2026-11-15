## Overview
- Event-driven backbone for the Clinic Management System managing asynchronous audit streaming, billing, and patient registration.
- Ensures HIPAA/GDPR compliance, 99.99% availability, and 10-year data retention across hybrid environments.

## Key Elements
- Kafka Brokers (Apache Kafka Core / KRaft mode)
- Schema Registry (Confluent Schema Registry)
- Kafka Connect (Confluent Kafka Connect)
- Kafka Monitoring & Metrics Exporter (JMX Exporter / Prometheus Operator)

## Relationships
- EMR Backend Container -> Kafka Brokers: Streams immutable audit logs [Binary Kafka Wire Protocol over TLS 1.3, mTLS, SASL/SCRAM]
- Patient Self-Service Container -> Kafka Brokers: Publishes patient registration and demographic events [Binary Kafka Wire Protocol over TLS 1.3]
- Billing Container -> Kafka Brokers: Decouples insurance claim submissions [Binary Kafka Wire Protocol over TLS 1.3]
- Kafka Connect -> Cold Storage: Sinks compliance logs for $\ge$ 10-year retention [WORM storage policies]
- Kafka Monitoring -> Prometheus/Monitoring Stack: Scrapes broker metrics and consumer lag [HTTP over TLS]

## Technology Stack
- Apache Kafka (KRaft mode): Chosen for zero-downtime event streaming and active-active hybrid replication.
- Confluent Schema Registry: Enforces Avro schemas for backward/forward data compatibility.
- Confluent Kafka Connect: Integrates directly with Cold Storage for compliance archiving.
- HashiCorp Vault: Automates mTLS certificate rotation and credential management.
- JMX Exporter / Prometheus: Enables real-time consumer lag monitoring for billing pipelines.

## Rationale
- This architecture decouples high-throughput components to guarantee EMR and registration UI performance under 1 second.
- Strict security controls, encryption, and WORM-configured cold storage satisfy rigorous HIPAA and GDPR compliance mandates.