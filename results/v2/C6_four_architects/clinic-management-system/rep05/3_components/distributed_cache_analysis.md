## Overview
The Clinic Management System is a clinical IT platform that handles patient admissions, EMRs, scheduling, and billing. It utilizes a hybrid cloud architecture to ensure strict regulatory compliance, high availability, and rapid data access.

## Key Elements
- Redis Proxy (Envoy/Redis Cluster Proxy)
- In-Memory Data Nodes (Redis Core)
- Persistence Engine (AOF/RDB)
- Data Encryption & Tokenization Component
- Cluster Management & Replication Daemon
- Cache Invalidation & TTL Manager
- Telemetry & Metrics Exporter

## Relationships
- Patient, EMR, and Billing Services -> Redis Proxy [RESP protocol over TCP]
- Redis Proxy <-> In-Memory Data Nodes [Redis Cluster Bus]
- In-Memory Data Nodes -> Data Encryption Component [Internal Memory Hooks]
- In-Memory Data Nodes <-> Cluster Management & Replication Daemon [TLS/TCP]
- Message Broker (Apache Kafka) -> Cache Invalidation & TTL Manager [Kafka Protocol/TCP]
- Telemetry & Metrics Exporter -> Observability Agent [HTTP/Prometheus]

## Technology Stack
- Redis Enterprise: Provides distributed, low-latency caching for sub-second EMR performance.
- Apache Kafka: Enables event-driven cache invalidation to prevent stale PHI reads.
- AES-256: Enforces data encryption at rest for HIPAA and GDPR compliance.
- Prometheus/Grafana: Scrapes cluster health and replication metrics for high availability monitoring.

## Rationale
This component architecture meets strict sub-second performance (R-07) and active-active 99.99% availability (R-06) targets across hybrid regions (`on-prem-k8s` and `eu-central-1`). Furthermore, it enforces robust security and compliance mandates (R-05) via dedicated encryption and event-driven invalidation patterns.