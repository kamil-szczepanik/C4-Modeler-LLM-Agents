## Overview
The State Caching Layer provides distributed, low-latency caching for patient state and electronic medical records across hybrid environments. It guarantees sub-second P95 performance and 99.99% availability while maintaining HIPAA and GDPR compliance.

## Key Elements
* Cache Router / Proxy: Envoy Proxy (sidecar)
* In-Memory Store: Redis Enterprise Core
* At-Rest Encryption Engine: Custom module with AES-256
* Replication & Sync Manager: Redis Enterprise Active-Active CRDT Modules
* Audit & TTL Enforcer: Redis Functions / Lua Scripting
* Cache Warmup & Hydration Worker: Go background worker

## Relationships
* Core Clinical, Scheduling, and Billing Microservices -> Cache Router: Queries and invalidates session & EMR cache [TLS / RESP]
* In-Memory Store -> At-Rest Encryption Engine: Secures sensitive PHI before persistence [Internal API]
* In-Memory Store -> Replication & Sync Manager: Replicates state changes across hybrid regions [TLS / Redis Cluster Bus]
* At-Rest Encryption Engine -> Key Management Service (Vault / Cloud KMS): Retrieves and rotates data encryption keys [gRPC / TLS]
* Cache Router -> Audit & TTL Enforcer: Triggers audit logging for sensitive PHI cache accesses [Internal Function Call]
* Audit & TTL Enforcer -> Audit Log Store (Elasticsearch): Streams compliance events [gRPC / TLS]
* Cache Warmup Worker -> Distributed Relational Database (CockroachDB): Fetches baseline clinical state [SQL / TLS]
* Cache Warmup Worker -> In-Memory Store: Populates initial cache keys [TCP / RESP]

## Technology Stack
* Redis Enterprise: Core in-memory storage for sub-second P95 performance
* Envoy Proxy: Secures TCP/RESP traffic and enforces TLS termination
* Redis Active-Active CRDTs: Enables WAN-optimized multi-region synchronization for 99.99% availability
* Vault / Cloud KMS: Manages AES-256 keys for strict HIPAA/GDPR encryption
* Elasticsearch: Immutable storage for compliance and audit logging

## Rationale
This architecture uses active-active CRDT replication and persistent caching to satisfy 99.99% uptime across hybrid cloud boundaries. Integrated encryption and automated auditing ensure strict HIPAA and GDPR compliance without impacting sub-second performance.