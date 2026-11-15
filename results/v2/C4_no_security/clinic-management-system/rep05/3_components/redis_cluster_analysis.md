## Overview
The Clinic Management System provides patient admissions, electronic medical records, scheduling, and billing for medium-sized hospitals and clinics. It ensures high availability, strict security, and compliance with healthcare regulations.

## Key Elements
- **Redis Cluster**: In-memory data store for EMR caching, session management, and appointment locking.
- **Redis Master Nodes**: Redis 7.x instances handling write operations via Raft-based consensus.
- **Redis Replica Nodes / Cluster Replicas**: Instances providing synchronous/asynchronous replication for failover.
- **EMR Core Service**: Spring Boot application interacting with the Redis Cluster.
- **DevOps Monitoring**: Prometheus exporters and PagerDuty alerting.

## Relationships
- **EMR Core Service -> Redis Cluster**: Caches EMR data, session states, and distributed locks using RESP3 protocol over TCP with TLS 1.3 encryption.
- **Redis Master Nodes -> Redis Replica Nodes**: Replicates data via internal cluster replication protocols to ensure zero data loss.

## Technology Stack
- **Redis 7.x**: Selected for native TLS 1.3 support, performance, and low-latency EMR requirements.
- **Redis Active-Active (CRDT)**: Implemented for multi-master replication across the hybrid topology.
- **Kubernetes**: Deployed with anti-affinity rules, volume persistence (RDB snapshots and AOF `appendfsync everysec`), and memory resource limits.
- **Prometheus & PagerDuty**: Used for operational monitoring, tracking memory usage, and alerting on failover events.

## Rationale
This architecture ensures sub-second EMR screen load times while meeting strict 99.99% availability and HIPAA/GDPR compliance mandates. Segregating caching and locking mechanisms protects data integrity and prevents system failures during high-concurrency clinical workflows.