## Overview
The system provides real-time payment fraud screening for card-not-present transactions, evaluating authorizations and managing review cases for fraud analysts. It utilizes Amazon ElastiCache (Redis) as an in-memory feature store to deliver low-latency velocity metrics for fraud rule evaluation.

## Key Elements
- Feature Store Engine (Redis OSS): In-memory key-value store holding pre-computed user/device velocity metrics.
- Replication Manager: Handles asynchronous replication across Multi-AZ nodes for high availability.
- Write-Through Ingestion Handler: Manages asynchronous updates to feature states without blocking scoring.
- Real-Time Scoring Engine: Reads velocity features via RESP protocol over TCP.
- Ingestion Pipeline / SQS: Sends asynchronous update events to refresh feature metrics.

## Relationships
- Real-Time Scoring Engine -> Feature Store Engine (Redis OSS): Retrieves features [RESP Protocol over TCP with TLS]
- Ingestion Pipeline / SQS -> Write-Through Ingestion Handler: Updates feature metrics [RESP Protocol over TCP with TLS]
- Feature Store Engine (Redis OSS) -> Amazon S3 / Aurora PostgreSQL: Performs periodic persistence for disaster recovery

## Technology Stack
- Amazon ElastiCache (Redis): In-memory data store using `cache.m6g` instances for sub-50ms P99 latency within budget.
- Redis Cluster & Multi-AZ: Ensures high availability and automatic failover under 3,000 req/sec traffic.
- Redis AUTH / RBAC & Command Whitelisting: Restricts access and disables administrative commands like `FLUSHALL` for PCI-DSS compliance.
- AWS CloudWatch: Monitors `EngineCPUUtilization`, slow logs, and memory metrics for operational visibility.

## Rationale
This architecture decouples the high-throughput read path from the ingestion write path, guaranteeing P99 decision latencies below 50 ms. Using a fully managed AWS ElastiCache service minimizes operational overhead for a three-engineer team while satisfying strict PCI-DSS Level 1 security and budget constraints.