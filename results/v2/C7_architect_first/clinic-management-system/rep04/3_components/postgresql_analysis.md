## Overview
The Clinic Management System provides patient admissions, electronic medical records, scheduling, and billing for medium-sized hospitals and clinics. It ensures HIPAA/GDPR compliance, 99.99% availability, and long-term data retention.

## Key Elements
- PostgreSQL (Primary database with RLS and encryption)
- Patroni & etcd (HA and automated failover)
- PgBouncer (Connection pooling)
- `pgaudit` Compliance Module (Audit trail logging)
- Core Clinical & EMR Service (Java / Spring Boot)
- Scheduling & Billing Service (Node.js / NestJS)
- On-Premises HSM (Cryptographic key management)
- HashiCorp Vault (Dynamic secret generation)

## Relationships
- Core Clinical & EMR Service -> PgBouncer: Database queries via [JDBC / TLS 1.3 with mTLS]
- PgBouncer -> PostgreSQL: Connection proxy via [TCP / TLS 1.3]
- PostgreSQL (`pgaudit`) -> Immutable Audit Log: Streams audit records via [Syslog / TLS]
- Row-Level Security & Encryption Manager -> On-Premises HSM: Requests cryptographic keys via [PKCS#11 / gRPC over TLS]
- Core Clinical & Scheduling Services -> HashiCorp Vault: Requests dynamic credentials via [HTTPS / REST]

## Technology Stack
- PostgreSQL: Relational and JSONB document storage for clinical records
- Patroni: Active-passive HA and automated failover for 99.99% uptime
- PgBouncer: Connection pooling to prevent process exhaustion during high concurrency
- `pgaudit`: Captures immutable DDL/DML audit trails for compliance
- HashiCorp Vault: Eliminates static credentials using dynamic secrets

## Rationale
This architecture balances strict healthcare regulatory compliance (HIPAA/GDPR) with sub-second EMR load performance. Active-passive replication via Patroni ensures data integrity while meeting high availability and 10-year retention targets.