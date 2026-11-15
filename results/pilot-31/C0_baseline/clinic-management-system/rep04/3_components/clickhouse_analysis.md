## Overview
The Clinic Management System is a hybrid-cloud platform designed for hospital administration, EMR management, and billing. It utilizes a dedicated ClickHouse-based analytical engine to provide long-term trend analysis and operational reporting without impacting transactional performance.

## Key Elements
*   **ClickHouse Cluster:** High-performance analytical database using `MergeTree` engines.
*   **Transformation Engine:** Go-based microservice for PII masking and pseudonymization.
*   **Query Proxy:** Go-based service enforcing row-level security and query validation.
*   **ClickHouse Keeper:** Coordination service for cross-region consensus.
*   **Audit Visualization Service:** Interface for administrative staff to access analytics.
*   **HashiCorp Vault:** Centralized secret management and encryption key provider.

## Relationships
*   **Debezium -> Transformation Engine:** Asynchronous data streaming via Kafka.
*   **Transformation Engine -> ClickHouse:** Pseudonymized data ingestion.
*   **Audit Visualization Service -> Query Proxy:** SQL-over-HTTP/gRPC requests.
*   **Query Proxy -> ClickHouse:** Enforced, validated analytical queries.
*   **ClickHouse -> S3-compatible Object Storage:** Tiered storage for archival data.

## Technology Stack
*   **ClickHouse:** Analytical database with `ReplacingMergeTree` for historical updates.
*   **Go:** Language for Transformation Engine and Query Proxy to ensure performance and memory safety.
*   **ClickHouse Keeper:** Coordination for cluster high availability.
*   **HashiCorp Vault:** AES-256 encryption at rest and salt management for pseudonymization.
*   **Prometheus:** Monitoring via sidecar exporters for query latency and OOM tracking.

## Rationale
Decoupling the analytical workload from the transactional PostgreSQL database ensures sub-second P95 performance for clinicians while supporting 10-year data retention. The transformation and proxy layers enforce strict HIPAA/GDPR compliance by sanitizing PII and validating queries before they reach the storage engine.