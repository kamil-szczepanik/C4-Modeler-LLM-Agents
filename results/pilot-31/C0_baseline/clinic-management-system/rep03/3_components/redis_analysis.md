## Overview
The Clinic Management System is a hybrid-cloud healthcare platform designed for high-availability patient record management and billing. It utilizes a caching layer to meet sub-second EMR latency requirements while maintaining strict HIPAA/GDPR compliance.

## Key Elements
*   **EMR Service:** Node.js/Fastify service managing clinical records.
*   **Redis Cluster:** Transient caching layer for EMR session states.
*   **PostgreSQL:** Primary system of record for audit trails and patient data.
*   **Infrastructure:** Hybrid deployment (on-prem K8s and AWS eu-central-1).
*   **Security:** SIEM integration, mTLS, and Client-side Field Level Encryption (FLE).

## Relationships
*   **EMR Service -> Redis:** Write-through caching pattern via Redis protocol; mTLS for authentication.
*   **EMR Service -> PostgreSQL:** Primary data persistence and audit trail verification.
*   **Redis Cluster (Cross-site):** Automated failover and synchronization via Redis Sentinel.
*   **Monitoring:** Prometheus exporters for cache health; SIEM for anomaly detection.

## Technology Stack
*   **Redis Sentinel:** Chosen for high-availability (99.99%) and automatic failover.
*   **mTLS & ACLs:** Enforced for secure, identity-based communication between services.
*   **Client-side FLE:** Ensures PHI is encrypted before cache storage to satisfy data-at-rest requirements.
*   **Volatile-LRU/TTL:** Policies to ensure Redis remains a transient cache, preventing PII persistence.
*   **Circuit Breakers:** Implemented in EMR service to handle cache latency or regional outages gracefully.

## Rationale
This architecture balances performance (R-07) with strict data governance by using Redis as a transient, encrypted, and ephemeral cache rather than a system of record. The hybrid-cloud deployment ensures 99.99% availability while maintaining the integrity of the 10-year audit trail via the PostgreSQL source of truth.