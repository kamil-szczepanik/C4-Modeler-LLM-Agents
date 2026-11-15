## Overview
The Clinic Management System provides patient admissions, electronic medical records, scheduling, and billing for medium-sized hospitals and clinics. It operates via a hybrid cloud infrastructure across on-premise Kubernetes and `eu-central-1`.

## Key Elements
- **Primary Database (PostgreSQL with Citus)**: Core distributed relational database.
- **Coordinator Node**: Manages metadata, query routing, and distributed transactions.
- **Worker Nodes (Shard Replicas)**: Distributed PostgreSQL instances with synchronous replication.
- **Connection Pooling Proxy (PgBouncer)**: Handles connection spikes and query routing.
- **Analytical Read Replicas**: Asynchronous PostgreSQL read replicas for billing and reporting.
- **Upstream Containers**: Patient Intake, Scheduling Engine, EMR Workspace, and Billing & Claims.

## Relationships
- Upstream Containers -> PgBouncer: Queries and transactions [pgJDBC/libpq over mTLS]
- Coordinator Node -> Worker Nodes: Inter-node operations [PostgreSQL wire protocol over TLS]
- Coordinator Node -> Analytical Read Replicas: Data replication [PostgreSQL streaming protocol over TLS]
- Billing & Claims Container -> Analytical Read Replicas: Read-only queries [pgJDBC/libpq over mTLS]

## Technology Stack
- **PostgreSQL with Citus**: Distributed relational database chosen for horizontal scalability and high availability.
- **PgBouncer**: Connection pooling proxy selected to manage connection spikes and resource exhaustion.
- **Patroni with Consul/etcd**: Automated failover solution ensuring sub-30-second replica promotion for 99.99% uptime.
- **HashiCorp Vault**: Manages short-lived dynamic database credentials via mTLS client certificates.
- **Crunchy Data Operator**: Automates provisioning, scaling, and operational management of PostgreSQL instances.

## Rationale
This architecture ensures HIPAA and GDPR compliance through AES-256 encryption, mTLS, and RBAC while delivering 99.99% availability via automated Patroni failover. Read replicas and query offloading isolate heavy billing workloads to guarantee sub-second EMR screen loads.