## Overview
The Reporting & Compliance Service is a specialized component of the Clinic Management System designed to generate audit-ready regulatory reports and operational KPIs. It ensures HIPAA/GDPR compliance through automated, immutable data exports and proactive risk monitoring.

## Key Elements
*   **Query Orchestrator:** Manages read-only data retrieval from PostgreSQL replicas.
*   **Data Masking Engine:** Applies dynamic ABAC-based PII/PHI obfuscation.
*   **Report Generator:** Creates digitally signed, immutable compliance documents.
*   **Query Builder/DSL Engine:** Facilitates self-service KPI generation with whitelist validation.
*   **Anomaly Detection Service:** Monitors audit logs for regulatory gaps and security threats.
*   **Query Governor:** Enforces resource quotas, timeouts, and rate-limiting.
*   **WORM Storage:** Provides immutable, S3-compatible long-term document retention.

## Relationships
*   **Auditors/Managers -> Query Builder:** HTTPS interface for dashboard and report requests.
*   **Query Orchestrator -> PostgreSQL:** Read-only SQL queries via mTLS.
*   **Report Generator -> WORM Storage:** S3-compatible API for immutable document storage.
*   **Anomaly Detection -> Audit Logs:** Asynchronous log stream via NATS/Kafka.
*   **Reporting Service -> KMS/HSM:** Digital signature generation for non-repudiation.

## Technology Stack
*   **Language:** Java/Spring Boot for core service logic.
*   **Data Access:** PostgreSQL (Patroni-managed replicas) for read-heavy operations.
*   **Caching:** Redis for result-set optimization of frequent KPIs.
*   **Messaging:** NATS/Kafka for asynchronous anomaly detection streams.
*   **Security:** mTLS for service communication, KMS/HSM for document signing, and ABAC for data access.
*   **Infrastructure:** IaC-managed immutable WORM storage buckets.

## Rationale
This architecture decouples heavy analytical workloads from clinical operations to maintain 99.99% availability. It enforces strict security boundaries and non-repudiation, ensuring compliance requirements are met without impacting system performance.