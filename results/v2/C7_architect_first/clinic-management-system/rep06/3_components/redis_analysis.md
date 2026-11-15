## Overview
The Clinic Management System is a clinical IT platform that handles patient admissions, EMRs, scheduling, and billing. It utilizes a Redis-based in-memory caching and locking layer to ensure high availability, fast response times, and strict regulatory compliance.

## Key Elements
- Redis Enterprise Cluster Engine (Multi-master, multi-replica in-memory store)
- Distributed Lock Manager (Redlock algorithm for appointment scheduling)
- Session & Token Cache (Ephemeral user sessions and OAuth2 tokens)
- EMR Read-Through Cache (Hot patient demographic and scheduling records)
- Persistence & Encryption Engine (AES-256 RDB/AOF snapshots)
- API Gateway & Core Business Services (Upstream clients)

## Relationships
- API Gateway -> Session & Token Cache: Validates ephemeral auth tokens [RESP over mTLS]
- Core Business Services -> Distributed Lock Manager: Coordinates scheduling locks via Redlock [RESP over mTLS]
- Core Business Services -> EMR Read-Through Cache: Reads/writes cached patient state [RESP over mTLS]

## Technology Stack
- Redis Cluster Mode: Provides high availability (99.99%) and horizontal scalability.
- Redis ACLs & mTLS: Secures internal transport and restricts administrative commands.
- HashiCorp Vault: Manages dynamic secret rotation for passwords and certificates.
- AES-256 Encryption: Secures persistence snapshots for HIPAA/GDPR compliance.

## Rationale
This architecture ensures high availability and low latency (<1s P95) for critical clinical workflows while strictly enforcing HIPAA and GDPR security controls. The multi-master Redis design prevents appointment scheduling conflicts through robust distributed locking.