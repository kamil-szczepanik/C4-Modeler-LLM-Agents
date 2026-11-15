## Overview
The Cache / State Store container provides ultra-low latency caching, distributed locking, and session management for the Clinic Management System. It ensures high availability and performance across hybrid cloud environments.

## Key Elements
- Cache / State Store (Redis Cluster / Redis Enterprise)
- TLS Termination Proxy
- Access Control & RBAC Enforcer
- In-Memory Data Engine
- Cluster Topology Manager
- Encryption & Key Management Module

## Relationships
- Core Services & EMR Service -> TLS Termination Proxy: TCP/TLS (RESP)
- TLS Termination Proxy -> Access Control & RBAC Enforcer: Internal routing of authenticated commands
- Access Control & RBAC Enforcer -> In-Memory Data Engine: Authorized keyspace operations
- In-Memory Data Engine -> Cluster Topology Manager: Internal IPC for node state monitoring
- In-Memory Data Engine -> Encryption & Key Management Module: Internal crypto operations for disk persistence
- Cache / State Store -> Cache / State Store (Active-Active Sync): Encrypted WAN replication link (`on-prem-k8s` to `eu-central-1`)
- Cache / State Store -> Message Broker: TCP/TLS (AMQP/Kafka) for state-eviction events

## Technology Stack
- Redis Cluster / Redis Enterprise: Selected for high-throughput, sub-second EMR performance and active-active multi-region replication.
- TLS 1.3: Enforces in-transit encryption for all client connections.
- AES-256: Provides transparent data encryption at rest for disk persistence.
- Redlock algorithm: Implements distributed locking for appointment scheduling clash checks.

## Rationale
This architecture delivers 99.99% active-active availability and sub-second EMR screen load times across hybrid cloud regions. It strictly enforces HIPAA and GDPR compliance mandates via robust encryption, RBAC, and secure cross-region synchronization.