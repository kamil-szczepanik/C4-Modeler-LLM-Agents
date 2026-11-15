## Overview
The system is an Amazon ElastiCache component architecture for an online bookstore providing low-latency caching and state management. Its core purpose is to guarantee sub-2-second page loads and high availability for 1M MAU.

## Key Elements
* Redis Primary Node (Redis Engine / Amazon ElastiCache)
* Redis Read Replica Nodes (Redis Engine)
* ElastiCache Cluster Manager (AWS Managed Control Plane)
* Redis Cluster Proxy (AWS ElastiCache Data Tiering / OSS Cluster API)
* In-Memory Eviction Manager (Redis LRU/LFU Engine)
* Backup & Snapshot Manager (AWS Automated Backup / Amazon S3)
* ElastiCache Cluster Node-to-Node Encryption & Auth Engine (Redis TLS/AUTH)

## Relationships
* BFF Container & Core E-Commerce Service -> Redis Cluster Proxy: Routes session, cart, and catalogue queries [RESP over TLS with AUTH]
* Redis Cluster Proxy -> Redis Primary Node / Read Replicas: Enforces secure command routing [RESP over TLS with AUTH]
* Redis Primary Node -> Backup & Snapshot Manager: Exports periodic RDB snapshots [Internal AWS API]

## Technology Stack
* Redis OSS / Amazon ElastiCache: In-memory store for low-latency session and cart caching
* AWS ElastiCache Multi-AZ with Auto-Failover: Ensures 99.95% uptime and automatic recovery
* Redis `volatile-lru`: Eviction policy preventing Out-Of-Memory crashes under peak load
* Redis TLS 1.3 & AUTH: Secures internal node communication for OWASP compliance

## Rationale
This component architecture fulfills stringent performance and availability targets by offloading read traffic to replicas and isolating application containers behind a secure cluster proxy. It successfully balances low latency, secure multi-region scaling, and robust disaster recovery.