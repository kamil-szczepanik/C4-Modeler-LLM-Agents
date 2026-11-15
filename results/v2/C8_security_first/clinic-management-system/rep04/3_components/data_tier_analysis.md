## Overview
The Data Tier for the Clinic Management System provides secure, highly available persistence for patient records, scheduling, and billing. It utilizes a distributed PostgreSQL architecture spanning hybrid on-premises and cloud environments to meet strict healthcare compliance standards.

## Key Elements
* Primary Write Instance (PostgreSQL Cluster)
* Local Synchronous & Cross-Region Read Replicas
* PgBouncer Connection Pooler
* PostgreSQL Audit Log (`pgAudit`) Collector
* CloudNativePG Operator
* WORM Storage / SIEM

## Relationships
* EMR & Scheduling Service -> Primary Write Instance: Writes transactional data [TCP/SQL via mTLS]
* EMR & Scheduling Service -> Read Replica Instances: Reads data with session consistency [TCP/SQL via mTLS]
* Billing & Claims Service -> Primary Write Instance: Writes financial data [TCP/SQL via mTLS]
* PostgreSQL Audit Log -> Event Broker (Kafka): Streams compliance audit events [Async / PubSub]

## Technology Stack
* **PostgreSQL:** Core relational database chosen for robust ACID compliance, RLS, and mature extensions.
* **PgBouncer:** Connection pooler to handle high concurrency and prevent connection saturation.
* **CloudNativePG:** Kubernetes operator managing automated failover and health checks.
* **TLS 1.3 / mTLS:** Mandatory transport security across the hybrid boundary.
* **`pgAudit`:** Native extension for comprehensive, tamper-evident data access logging.
* **Prometheus & Grafana:** Monitoring stack for tracking replication lag, connection saturation, and query performance.

## Rationale
This architecture ensures 99.99% uptime and low-latency EMR access (<1s P95) through local semi-synchronous replicas while meeting HIPAA/GDPR data protection mandates. Hybrid replication and immutable audit logging satisfy strict 10-year medical data retention and security compliance requirements.