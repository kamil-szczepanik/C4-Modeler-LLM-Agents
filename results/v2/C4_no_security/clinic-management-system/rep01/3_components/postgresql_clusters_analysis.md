## Overview
The Clinic Management System is a hybrid cloud platform managing patient records, scheduling, and billing for healthcare providers. It ensures high availability, 10-year data retention, and HIPAA/GDPR compliance.

## Key Elements
- PostgreSQL 16 Primary Database Engine
- PostgreSQL 16 Read Replica Engine
- PgBouncer Connection Pooler
- Distributed Consensus / Fencing Manager (etcd / Raft)
- WAL Archiver (pgBackRest)
- Kubernetes Operator (CloudNativePG / Crunchy Data)

## Relationships
- Microservices -> PgBouncer: TCP / TLS 1.3
- PgBouncer -> Primary Database Engine (Writes): TCP
- PgBouncer -> Read Replica Engine (Reads): TCP
- Primary Database Engine -> Read Replica Engine: Synchronous (on-prem) / Asynchronous (cross-region to eu-central-1)
- Primary Database Engine -> WAL Archiver: FileSystem / S3 API

## Technology Stack
- PostgreSQL 16: Primary database engine for relational clinical and billing data
- PgBouncer: Connection pooling and smart read/write routing to reduce latency
- etcd / Raft: Distributed consensus and automated leader election for zero data loss
- pgBackRest: Continuous backup and recovery supporting 10-year retention
- CloudNativePG: Kubernetes operator managing hybrid database lifecycle and automated fencing

## Rationale
Active-passive synchronous replication guarantees an RPO of zero to protect critical patient medical records and billing integrity. Hybrid replication balances local high availability with disaster recovery without violating the sub-second EMR load performance SLA.