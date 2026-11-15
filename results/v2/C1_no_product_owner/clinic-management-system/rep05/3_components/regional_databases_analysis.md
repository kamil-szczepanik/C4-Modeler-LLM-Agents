## Overview
The Clinic Management System manages patient admissions, EMRs, scheduling, and billing for healthcare facilities while ensuring HIPAA, GDPR, and 99.99% availability. It utilizes a hybrid cloud architecture spanning on-premise Kubernetes and AWS (eu-central-1).

## Key Elements
- Distributed SQL Engine (CockroachDB v23+)
- Connection Pooler & Routing Proxy (PgBouncer / built-in SQL proxy)
- Database Encryption Manager (Native KMS integration)
- Audit Log Exporter (Ring-buffer local spooling)
- Core Services (Node.js / Spring Boot)
- Enterprise KMS & SIEM & Audit Platform

## Relationships
- Core Services -> Connection Pooler & Routing Proxy: [Encrypted SQL over TLS via mTLS, Port 26257]
- Connection Pooler & Routing Proxy -> Distributed SQL Engine: [Local loopback / internal mTLS]
- Audit Log Exporter -> SIEM & Audit Platform: [Async TLS streaming]
- Database Encryption Manager -> Enterprise KMS: [Envelope encryption / TDE keys]

## Technology Stack
- CockroachDB v23+: Chosen for multi-active regional nodes, automatic sharding, ACID guarantees, and geo-partitioning.
- AES-256 TDE & Column-Level Encryption (CLE): Mandated for PHI security and compliance.
- mTLS & OAuth2/OIDC: Enforces zero-trust service communication and dynamic IAM token authentication.
- Prometheus: Tracks Raft consensus round-trips, replication lag, and connection pool metrics.

## Rationale
This architecture ensures strict regional data residency and low latency required for high-performance EMR access. Active-active distributed consensus guarantees high availability across hybrid cloud boundaries.