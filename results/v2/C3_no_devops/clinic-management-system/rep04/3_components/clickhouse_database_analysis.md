## Overview
The Clinic Management System is a hybrid cloud platform providing patient admissions, electronic medical records (EMR), scheduling, and billing. It ensures HIPAA and GDPR compliance, high availability (99.99%), and a 10-year data retention policy.

## Key Elements
- ClickHouse Database: Analytical database for real-time operational analytics and reporting.
- Storage Engine (MergeTree Family): Uses `ReplacingMergeTree` and `ReplicatedMergeTree` on NVMe storage.
- Security & Encryption Module: Enforces AES-256, column-level masking, RLS, and OIDC RBAC.
- Ingestion & Materialization Worker: Consumes streams from Apache Kafka.
- Distributed Query Processor: Vectorized query engine for sub-second responses.
- Materialized View & Aggregation Engine: Pre-aggregates patient throughput and billing metrics.

## Relationships
- Core Services Container interacts with ClickHouse Database via HTTPS (Port 8443) using mTLS.
- Audit & Compliance Container interacts with ClickHouse Database via ClickHouse Native Protocol / HTTPS (Port 9000/8443) using mTLS.
- Apache Kafka streams data to Ingestion & Materialization Worker via ClickHouse Native Protocol.

## Technology Stack
- ClickHouse: Chosen for high-throughput analytical ingestion and sub-second aggregations.
- Istio Service Mesh: Provides mTLS transport security between containers and database.
- Apache Kafka: Used for streaming audit logs and clinical metrics with TLS and SASL.
- HashiCorp Vault / Cloud HSM: Manages AES-256 keys and TLS certificates with 90-day rotation.

## Rationale
This architecture uses ClickHouse to offload complex analytical queries from transactional stores, maintaining sub-second performance. Strict RBAC, mTLS, and AES-256 encryption satisfy HIPAA and GDPR security constraints.