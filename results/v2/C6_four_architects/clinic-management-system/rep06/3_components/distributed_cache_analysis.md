## Overview
The Clinic Management System provides patient registration, EMR, scheduling, and billing for medium-sized clinics. It uses a distributed cache component to ensure sub-second EMR retrieval and high availability.

## Key Elements
- Client Connection Handler (Multiplexing I/O Engine)
- Cache Cluster Manager (Redis Sentinel / Cluster Coordinator)
- In-Memory Storage Engine (Redis Core)
- Data Encryption Module (TLS / AES-256 Module)
- Replication Agent (Redis Master-Replica Sync Engine)
- WAN Replication & Tunneling Module (Redis Enterprise Active-Active / Envoy Proxy)
- Cache Eviction & Expiry Manager

## Relationships
- EMR Service -> Client Connection Handler: Sends read/write commands via [TCP / Redis Protocol]
- Client Connection Handler -> Data Encryption Module: Decrypts incoming traffic via [In-Memory Processing]
- Cache Cluster Manager <-> In-Memory Storage Engine: Coordinates replication via [Internal Redis Cluster Bus]
- In-Memory Storage Engine -> Replication Agent: Streams write-ahead logs via [TCP / Redis Replication Protocol]
- Replication Agent -> WAN Replication & Tunneling Module: Forwards cross-site data via [TCP]
- WAN Replication & Tunneling Module -> WAN Replication & Tunneling Module (Remote): Synchronizes state via [mTLS]
- Cache Eviction & Expiry Manager -> In-Memory Storage Engine: Purges expired keys via [Internal Memory Access]

## Technology Stack
- Redis Core: In-memory storage for high-performance sub-second EMR retrieval
- Redis Sentinel / Cluster: High availability and automatic failover across hybrid nodes
- TLS 1.3 / AES-256: In-transit and at-rest security for HIPAA and GDPR compliance
- Envoy Proxy: Secure cross-site WAN tunneling via mTLS

## Rationale
This architecture delivers 99.99% uptime via active-active replication across on-prem-k8s and eu-central-1. It enforces strict HIPAA/GDPR security while maintaining sub-second P95 performance for clinical workflows.