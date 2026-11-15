## Overview
[The Clinic Management System manages patient admissions, EMRs, scheduling, and billing for medium-sized healthcare facilities. It utilizes a Redis Enterprise tier to deliver high-availability caching, distributed locking, and sub-second performance.]

## Key Elements
* Redis Enterprise Container Tier
* In-Memory Data Store & Key-Space Partitioning Router
* Distributed Lock Manager & Redlock Algorithms
* Session State Engine & RBAC Enforcer
* Active-Active Conflict Resolution Engine (CRDTs)
* Persistence & Backup Coordinator (RDB/AOF)
* Encryption-At-Rest Manager (AES-256, PKCS#11)
* Pub/Sub Event Broker & Bulk Ingestion Pipeline
* Geo-Replication Tunnel Manager & Cluster Topology Manager
* Memory Eviction, TTL Policy Controller & Resource Quota Enforcer
* Telemetry Exporter & Audit Log Interceptor
* Dead Letter & Fallback Handler

## Relationships
* Patient & EMR Service -> Redis Enterprise: Executes distributed locking and caching [RESP3 over TLS]
* Scheduling Service -> Redis Enterprise: Validates appointment resource clashes [RESP3 over TLS]
* Redis Enterprise -> PostgreSQL Container Cluster: Fallback read/write operations during partitions [gRPC/SQL]
* Redis Enterprise -> Observability Collector Container: Exports metrics [Prometheus scrapers]
* Redis Enterprise -> Audit & Compliance Sidecar Container: Streams administrative audit logs [Structured Logs]

## Technology Stack
* Redis Enterprise: Active-active caching and distributed memory store for high availability
* RESP3 over TLS: Encrypted wire protocol for client-cache communication
* PKCS#11 & AES-256: Encryption standards for data at rest
* Conflict-Free Replicated Data Types (CRDTs): Ensures active-active multi-region state convergence
* Prometheus & OpenTelemetry: Metrics collection and observability

## Rationale
[This architecture satisfies HIPAA and GDPR compliance mandates through robust AES-256 encryption, TLS transport security, and comprehensive audit logging. The active-active CRDT configuration and hybrid geo-replication ensure the required 99.99% availability and low-latency EMR performance.]