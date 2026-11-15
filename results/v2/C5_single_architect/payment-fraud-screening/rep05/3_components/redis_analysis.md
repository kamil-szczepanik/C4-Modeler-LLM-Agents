## Overview
The Redis container provides ultra-low-latency feature lookups and sliding-window velocity metrics for the Real-Time Payment Fraud Screening system. It ensures sub-50ms decision latency and automated failover within AWS.

## Key Elements
* **Redis Primary Node**: Amazon ElastiCache instance handling real-time feature writes and fast reads.
* **Redis Replica Node**: Amazon ElastiCache instance providing automatic failover.
* **In-Memory Feature Cache Store**: Redis Hashes and Sorted Sets storing sliding-window velocity metrics using tokenized identifiers.

## Relationships
* **Fraud Scoring Engine -> Redis Primary**: Fetches features and executes Lua scripts for atomic rate-limiting and feature retrieval via RESP protocol [TCP].
* **Redis Primary -> Redis Replica**: Synchronizes state via asynchronous replication [RESP protocol via TCP].

## Technology Stack
* **Amazon ElastiCache (Redis OSS)**: Managed service chosen to minimize operational overhead for a three-engineer team.
* **Redis RESP Protocol / TCP**: High-performance network protocol ensuring decision latency remains below 50 ms at P99.
* **AWS KMS**: Provides encryption-at-rest for PCI-DSS Level 1 compliance.
* **TLS**: Ensures encryption-in-transit across private VPC subnets.

## Rationale
This architecture meets strict performance and availability constraints by utilizing fully managed in-memory replication. It guarantees compliance and security requirements while remaining operable by a small engineering team within a fixed budget.