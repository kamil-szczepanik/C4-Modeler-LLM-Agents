## Overview
[The PostgreSQL Cluster manages secure, high-availability transactional storage for the Clinic Management System to ensure HIPAA and GDPR compliance. It delivers reliable persistence for patient records, scheduling, and audit logs across hybrid cloud deployments.]

## Key Elements
- Primary Write Node
- Synchronous Standby Nodes
- Read-Only Replica Nodes
- PgBouncer Connection Pooler
- pgaudit Extension
- HashiCorp Vault Secrets Manager
- Patroni / CloudNativePG Orchestrator

## Relationships
- Go EMR Service -> Primary Write Node: Persists transactional data via PostgreSQL Wire Protocol over TCP/IP port 5432 with TLS 1.3 and SCRAM-SHA-256
- Node.js Scheduling Service -> Primary Write Node: Manages appointment data via PostgreSQL Wire Protocol over TCP/IP port 5432 with TLS 1.3
- Reporting Container -> Read-Only Replica Nodes: Executes analytical queries using PostgreSQL protocol
- Primary Write Node -> Synchronous Standby Nodes: Replicates data using native PostgreSQL streaming replication

## Technology Stack
- PostgreSQL: Core relational database chosen for robust ACID compliance and complex clinical querying
- AES-256 (TDE): Enforced on storage volumes for HIPAA/GDPR data-at-rest security
- PgBouncer: Manages client connection pools efficiently to maintain low latency
- Patroni / CloudNativePG: Orchestrates high availability and automated failover across hybrid Kubernetes environments
- HashiCorp Vault: Secures and rotates database superuser and replication credentials

## Rationale
[This architecture guarantees the required 99.99% uptime and zero-data-loss failover for critical clinical operations. Furthermore, it enforces strict multi-layered security, encryption, and auditability to comply with HIPAA and GDPR mandates.]