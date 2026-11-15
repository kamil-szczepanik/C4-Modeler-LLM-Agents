## Overview
The Clinic Management System is a hybrid-cloud platform designed for clinical operations, EMR management, and billing. It provides high-availability healthcare services while ensuring strict HIPAA/GDPR compliance and 10-year data retention.

## Key Elements
*   **Database:** PostgreSQL (CloudNativePG)
*   **Orchestration:** Kubernetes (On-prem & AWS eu-central-1)
*   **Security:** HashiCorp Vault, mTLS, `pgaudit`
*   **Integration:** Debezium (CDC), ClickHouse (Analytics)
*   **Services:** Core EMR Service (Spring Boot), Billing Service (Go)

## Relationships
*   **Core EMR Service → PostgreSQL:** Transactional SQL operations via mTLS.
*   **PostgreSQL → Debezium:** Transactional change streaming [CDC] for real-time analytics.
*   **PostgreSQL → HashiCorp Vault:** Dynamic secret retrieval and KMS-based cryptographic shredding.
*   **PostgreSQL → Prometheus/Grafana:** Metric export via sidecar for observability.

## Technology Stack
*   **PostgreSQL (CloudNativePG):** Chosen for high-availability, synchronous replication (RPO=0), and declarative partitioning.
*   **HashiCorp Vault:** Manages dynamic database roles and encryption keys to satisfy AES-256 and GDPR requirements.
*   **pgaudit:** Implements tamper-resistant logging for HIPAA/GDPR audit compliance.
*   **PostgreSQL Declarative Partitioning:** Maintains P95 latency for EMR records over a 10-year retention period.
*   **Row-Level Security (RLS) & Cryptographic Shredding:** Ensures GDPR "Right to be Forgotten" while maintaining referential integrity for billing.

## Rationale
This architecture ensures 99.99% availability through Kubernetes-native high-availability patterns and strict resource management. The combination of declarative partitioning and cryptographic shredding balances the conflicting requirements of long-term data retention, performance, and regulatory privacy mandates.