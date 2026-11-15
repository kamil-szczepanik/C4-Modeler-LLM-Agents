## Overview
The Clinic Management System provides patient admissions, electronic medical records, scheduling, and billing for medium-sized hospitals and clinics. It ensures HIPAA/GDPR compliance, high availability, and secure hybrid-cloud data storage.

## Key Elements
- PostgreSQL Databases: Patroni/etcd clustered relational storage with PgBouncer connection pooling
- HashiCorp Vault: Dynamic secrets management and AES-256 encryption key provider
- Immutable Audit Storage Sink: Secure storage for compliance logs and archived data
- Microservices: EMR, Scheduling, and Billing containers communicating via REST/gRPC
- Hybrid Infrastructure: On-premise Kubernetes (`on-prem-k8s`) and AWS (`eu-central-1`)

## Relationships
- EMR Container -> PostgreSQL Databases: Reads/writes clinical data via TLS 1.3/mTLS, SQL
- Scheduling Container -> PostgreSQL Databases: Reads/writes scheduling data via TLS 1.3/mTLS, SQL
- Billing Container -> PostgreSQL Databases: Reads/writes financial data via TLS 1.3/mTLS, SQL
- PostgreSQL Databases -> Immutable Audit Storage Sink: Streams `pgaudit` logs and archives data securely
- PostgreSQL Databases (on-prem) -> PostgreSQL Databases (cloud): Asynchronous cross-site replication via WireGuard/IPsec tunnel

## Technology Stack
- PostgreSQL & Patroni: High-availability active-passive clustering with automated failover
- PgBouncer: Connection pooling to prevent starvation under heavy concurrent clinical usage
- HashiCorp Vault: Dynamic database credential provisioning and AES-256 encryption management
- pgaudit: Tamper-evident logging capturing DDL/DML operations on PHI tables
- WireGuard / IPsec: Encrypted overlay network for cross-site hybrid cloud replication

## Rationale
This architecture ensures 99.99% uptime and sub-second EMR performance via robust connection pooling, date partitioning, and active-passive clustering. Strict security controls, mTLS, dynamic credentials, and automated PITR guarantee HIPAA/GDPR compliance across hybrid environments.