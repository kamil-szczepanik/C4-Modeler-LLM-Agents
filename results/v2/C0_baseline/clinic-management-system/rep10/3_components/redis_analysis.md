## Overview
[The Clinic Management System manages patient admissions, EMRs, scheduling, and billing for clinical environments. It utilizes Redis as an ephemeral caching layer to ensure high-performance appointment booking while maintaining strict HIPAA and GDPR compliance.]

## Key Elements
- In-Memory Data Store Component (Redis Enterprise / OSS)
- TLS Termination & Encryption Proxy Component (Redis Stunnel / Envoy sidecar)
- Scheduling Service
- PostgreSQL Database
- HashiCorp Vault

## Relationships
- Scheduling Service -> In-Memory Data Store: Checks and acquires resource locks [Redis Protocol over TLS, TCP 6379]
- In-Memory Data Store -> PostgreSQL: Cache-aside fallback for persistent scheduling misses [SQL/TCP]

## Technology Stack
- Redis (Sentinel/Cluster topology): Chosen for 99.99% availability and low-latency scheduling data.
- Redis Operator for Kubernetes: Automates failover and resource governance in hybrid cloud.
- HashiCorp Vault: Manages strong Redis AUTH passwords and encryption keys.
- Envoy sidecar: Enforces mTLS and AES-256 encryption in transit.

## Rationale
[This architecture satisfies the sub-second performance requirements for clinical workflows by leveraging an ephemeral, high-availability caching layer. Security constraints are strictly enforced through disabled disk persistence, mTLS, and RBAC to protect patient data.]