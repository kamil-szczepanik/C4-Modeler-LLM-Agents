## Overview
The Clinic Management System is a hybrid-cloud platform designed to manage patient records, scheduling, and billing. It utilizes a real-time CDC pipeline to decouple clinical operations from analytics while ensuring strict regulatory compliance.

## Key Elements
*   **Debezium (PostgreSQL Connector):** Captures WAL events for real-time streaming.
*   **Apache Kafka:** Acts as the message broker and buffer for change events.
*   **Kafka Connect Workers:** Distributed processing nodes for streaming tasks.
*   **ClickHouse:** Analytics store for clinical insights and reporting.
*   **HashiCorp Vault:** Manages dynamic credentials and encryption keys.
*   **Audit Visualization Service:** Consumes event streams for regulatory reporting.
*   **Schema Registry:** Enforces structural consistency for streaming data.

## Relationships
*   **PostgreSQL → Debezium:** CDC via WAL streaming (mTLS encrypted).
*   **Debezium → Kafka:** Publishes change events using Kafka Connect.
*   **Kafka → ClickHouse:** Sinks events via Kafka Connect for analytics.
*   **Debezium → HashiCorp Vault:** Fetches credentials and performs Field-Level Encryption (FLE).
*   **Kafka → S3 (Tiered Storage):** Archives historical events for 10-year retention.

## Technology Stack
*   **Debezium & Kafka Connect:** Chosen for low-latency, reliable CDC and integration with Kafka.
*   **HashiCorp Vault (Transit Engine):** Implements FLE and dynamic secrets for HIPAA/GDPR compliance.
*   **Kafka Tiered Storage:** Manages long-term data retention without impacting broker performance.
*   **Java-based SMTs:** Minimizes CPU overhead during pseudonymization compared to script-based transforms.
*   **Prometheus/Grafana:** Monitors connector lag and WAL growth to maintain 99.99% availability.

## Rationale
This architecture decouples the primary EMR database from analytical workloads to meet sub-second P95 performance requirements. It ensures HIPAA/GDPR compliance through field-level encryption, pseudonymization, and immutable audit trails via Kafka-based event streaming.