## Overview
The Library Management System is a comprehensive solution for public and academic libraries to catalogue physical and digital items, manage circulation, and provide self-service portals with strict EU data residency compliance. The PostgreSQL database architecture provides robust transactional storage, automated failover, and workload isolation to meet sub-800ms performance requirements.

## Key Elements
- PostgreSQL Storage: Relational database engine managing ACID transactions
- PgBouncer: Connection pooler preventing resource exhaustion
- Patroni with etcd: Consensus-based automated failover manager
- Read-Only Replica Router: Logical routing layer for administrative traffic
- PostgreSQL Read Replica: Asynchronous replica for reporting workloads
- Prometheus Exporter: Metrics sidecar for operational observability
- pgaudit: Audit logging extension for compliance monitoring

## Relationships
- Core Domain Service -> PgBouncer: SQL queries [TCP/IP over mTLS 1.3]
- PgBouncer -> PostgreSQL Storage: SQL queries [TCP/IP over mTLS 1.3]
- Library Staff -> Read-Only Replica Router: SQL queries [TCP/IP over TLS 1.3]
- Read-Only Replica Router -> PostgreSQL Replica: SQL queries [TCP/IP over mTLS 1.3]
- PostgreSQL Storage -> Volume Mount: Encrypted persistence [LUKS/AES-256]

## Technology Stack
- PostgreSQL: Core relational database for robust ACID transaction handling
- PgBouncer: Connection pooling to handle heavy concurrency and prevent exhaustion
- Patroni & etcd: High availability orchestration ensuring zero single points of failure
- LUKS/AES-256: Volume-level storage encryption ensuring EU data residency compliance
- Prometheus & Grafana: Telemetry and alerting stack monitoring replication lag and connection saturation
- pg_backrest / WAL-G: Point-in-time recovery targeting geo-redundant EU object storage

## Rationale
This architecture ensures strict EU-only data residency via encrypted storage while maintaining high availability and predictable sub-800ms response times for patrons. Isolating reporting traffic onto a read-only replica protects operational performance under heavy academic traffic.