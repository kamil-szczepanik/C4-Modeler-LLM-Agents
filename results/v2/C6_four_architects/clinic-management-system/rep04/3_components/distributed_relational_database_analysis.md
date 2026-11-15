## Overview
The Clinic Management System manages patient admissions, electronic medical records, scheduling, and billing for medium-sized hospitals and clinics. It utilizes a hybrid-cloud, high-availability architecture to ensure strict compliance with healthcare regulations.

## Key Elements
- **SQL Layer (Distributed Query Engine)**: CockroachDB SQL Parser / Optimizer
- **Transaction Coordinator / Raft Consensus Engine**: CockroachDB Raft / Multi-Raft
- **Storage Engine (RocksDB)**: RocksDB via Go wrapper
- **Encryption & Key Management Subsystem**: CockroachDB Enterprise Security / OpenSSL
- **Change-Data-Capture (CDC) Streamer**: CockroachDB Changefeeds / gRPC
- **Connection & Pool Manager**: Built-in SQL Proxy / PgBouncer

## Relationships
- **Microservices -> Connection & Pool Manager**: Persists data [PostgreSQL wire protocol over TLS 1.3]
- **Encryption & Key Management Subsystem -> Key Management Service (Vault / Cloud KMS)**: Fetches and rotates encryption keys [HTTPS / REST over TLS 1.3]
- **Change-Data-Capture (CDC) Streamer -> Message Broker (Apache Kafka)**: Publishes transactional change feeds [gRPC / Kafka Protocol over TLS 1.3]
- **Connection & Pool Manager -> SQL Layer**: Forwards authenticated queries [In-memory function calls]
- **SQL Layer -> Transaction Coordinator / Raft Consensus Engine**: Coordinates reads and writes [Multi-Raft]
- **Transaction Coordinator / Raft Consensus Engine <-> Storage Engine**: Persists key-value ranges locally [RocksDB API via CGO]

## Technology Stack
- **CockroachDB**: Selected for distributed SQL capabilities, active-active multi-region replication, and high availability.
- **RocksDB**: Provides low-latency LSM-tree based local data persistence.
- **TLS 1.3 & AES-256**: Ensures secure data transmission and encryption at rest for HIPAA and GDPR compliance.
- **Apache Kafka & HashiCorp Vault**: Used for real-time CDC event streaming and secure key management.

## Rationale
This architecture guarantees 99.99% uptime through active-active multi-region replication while meeting stringent HIPAA and GDPR security mandates via AES-256 encryption. The distributed relational design ensures robust data consistency, high performance, and long-term data retention across hybrid environments.