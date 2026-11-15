## Overview
Distributed clinical management system providing patient care, scheduling, EMR, and billing across a hybrid cloud topology. Core purpose is ensuring high availability, strict HIPAA/GDPR compliance, and low-latency clinical operations.

## Key Elements
- **SQL Layer**: Go-based parser, planner, and executor for distributed SQL.
- **Transaction Engine**: ACID transaction manager using Multi-Version Concurrency Control (MVCC) and Raft consensus.
- **Storage Engine**: RocksDB managing local disk key-value storage.
- **Dist_SQL**: Distributed execution engine for parallelized queries.
- **Supporting Containers**: EMR Service, Billing Service, Scheduling Service, OpenTelemetry Collector, HashiCorp Vault.

## Relationships
- **Application Services** connect to the **SQL Layer** via PostgreSQL wire protocol over TLS 1.3.
- **Internal Nodes** communicate via gRPC with strict mutual TLS (mTLS) across `on-prem-k8s` and `eu-central-1`.
- **OpenTelemetry Collector** scrapes metrics and audit logs from CockroachDB.
- **HashiCorp Vault** integrates via PKI engine for automated certificate rotation and AES-256 key management.

## Technology Stack
- **CockroachDB**: Distributed SQL database chosen for active-active multi-region replication and 99.99% availability.
- **RocksDB**: Embedded key-value store for local persistence.
- **gRPC & TLS 1.3**: Protocols for secure, high-performance node-to-node and client-database communication.
- **HashiCorp Vault**: Secrets management and PKI for AES-256 encryption-at-rest and mTLS.
- **OpenTelemetry**: Observability and audit log streaming for HIPAA compliance.

## Rationale
Locality-aware placement and range leaseholder routing minimize cross-region latency between `on-prem-k8s` and `eu-central-1` to meet the <1s P95 EMR load time. Enforced mTLS, AES-256 encryption, and automated audit logging satisfy strict HIPAA and GDPR data protection mandates.