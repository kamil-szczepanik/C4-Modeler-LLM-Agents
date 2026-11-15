## Overview
The Audit Log Store container manages tamper-evident, highly available logging for the Clinic Management System to ensure HIPAA, GDPR, and 10-year retention compliance. It provides secure ingestion, active-active replication, background archival, and continuous integrity verification of all clinical audit data.

## Key Elements
- **Audit Ingestor**: Node.js/TypeScript component processing asynchronous log events.
- **Immutable Storage Engine**: PostgreSQL append-only tables utilizing SHA-256 cryptographic chaining.
- **Archival Worker**: Python component handling batch offloads to long-term storage.
- **Audit Query API**: Node.js/TypeScript component providing secure, read-only compliance access.
- **Replication Manager**: Go component managing multi-region active-active synchronization.
- **Integrity Verifier**: Go component performing routine hash-chain verification and alerting.

## Relationships
- **Event Broker (Apache Kafka)** -> **Audit Ingestor**: Consumes log events [Kafka Protocol over TLS]
- **Audit Ingestor** -> **Immutable Storage Engine**: Writes audit records [SQL/TCP with TLS]
- **API Gateway / Core Services** -> **Audit Query API**: Forwards search and compliance requests [gRPC over mTLS]
- **Audit Query API** -> **Immutable Storage Engine**: Reads verified audit records [SQL/TCP with TLS]
- **Immutable Storage Engine** -> **Replication Manager**: Streams Write-Ahead Logs [TCP with TLS]
- **Archival Worker & Replication Manager** -> **Cloud Backup (AWS S3 Glacier)**: Exports batch archives [HTTPS / Encrypted Storage API]
- **Integrity Verifier** -> **Observability & Monitoring Collector**: Emits compliance alert metrics [gRPC/OTLP over TLS]
- **Immutable Storage Engine** -> **Key Management Service (KMS)**: Requests envelope encryption keys [HTTPS/REST]

## Technology Stack
- **Node.js / TypeScript**: Used for the Audit Ingestor and Audit Query API for efficient asynchronous I/O handling.
- **PostgreSQL (Append-Only / WORM)**: Powers the Immutable Storage Engine to guarantee data immutability and SQL-based querying.
- **Python**: Powers the Archival Worker for efficient data batching and S3 Glacier offloading.
- **Go**: Used for the Replication Manager and Integrity Verifier to ensure high performance and concurrency in data sync and verification.
- **Apache Kafka**: Used for reliable message streaming during event ingestion.
- **AWS S3 Glacier**: Provides secure, cost-effective long-term data retention for $\ge$ 10 years.

## Rationale
This architecture uses append-only cryptographic chaining and dedicated verification components to strictly satisfy HIPAA and GDPR tamper-evidence mandates. Active-active replication via WAL streaming and multi-component isolation ensure 99.99% availability and adherence to the 10-year data retention constraint.