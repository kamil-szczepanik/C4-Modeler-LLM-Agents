## Overview
The Clinic Management System manages patient admissions, EMRs, scheduling, and billing for healthcare clinics. It provides secure, highly available clinical data storage adhering to HIPAA and GDPR regulations.

## Key Elements
* Primary Relational Store (PostgreSQL with Patroni and Citus sharding)
* Read Replica Cluster
* Audit & Compliance WORM Store (AWS S3 Object Lock / MinIO)
* Cold Data Archival Engine
* PgBouncer Connection Pooling Proxy
* Data Export Worker Component

## Relationships
* EMR Core Service -> Primary Relational Store: Reads and writes clinical data [SQL over TLS 1.3 with mTLS]
* Billing Integration Service -> Primary Relational Store: Reads and writes billing data [SQL over TLS 1.3 with mTLS]
* Audit & Compliance Daemon -> Audit & Compliance WORM Store: Records immutable audit logs [WORM Storage protocols]
* Data Export Worker -> Read Replica Cluster & Cold Archival Engine: Generates GDPR data portability bundles [Internal API / SQL]

## Technology Stack
* PostgreSQL: Relational database providing ACID compliance and Row-Level Security.
* Patroni: Automated high-availability and failover management.
* PgBouncer: Connection pooling to handle heavy hospital shift traffic spikes.
* HashiCorp Vault: Dynamic database credential injection and short-lived token rotation.
* AWS S3 Object Lock / MinIO: WORM storage implementation for 10-year audit and archival retention.

## Rationale
This architecture guarantees 99.99% availability and <1s EMR load times via read replicas and connection pooling. Strict schema isolation and WORM storage ensure full compliance with HIPAA and GDPR regulations.