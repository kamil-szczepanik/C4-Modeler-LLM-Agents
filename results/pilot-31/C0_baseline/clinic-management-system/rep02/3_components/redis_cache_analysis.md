## Overview
The Clinic Management System is a hybrid-cloud platform providing clinical staff with high-availability access to patient records and scheduling. It utilizes a secure, high-performance caching layer to ensure sub-second EMR retrieval while maintaining strict HIPAA/GDPR compliance.

## Key Elements
*   **Clinical Staff:** Primary users requiring sub-second EMR access.
*   **EMR/Scheduling Services:** Java/Spring Boot services managing core clinical logic.
*   **Redis Cluster:** In-memory store for performance optimization.
*   **Envoy Sidecar Proxy:** Manages mTLS termination and connection pooling.
*   **Debezium CDC:** Captures PostgreSQL changes for cache invalidation.
*   **PostgreSQL Cluster:** The primary system of record.

## Relationships
*   **EMR Services -> Redis:** Retrieves/updates data via TCP with TLS 1.3.
*   **Envoy Sidecar -> Redis:** Manages mTLS-authenticated connections and circuit breaking.
*   **PostgreSQL -> Debezium -> Redis:** Pub/Sub mechanism for real-time cache invalidation.
*   **Java Services -> KMS/HSM:** Fetches keys for application-layer encryption of PHI.

## Technology Stack
*   **Redis Cluster:** High-availability configuration for active-active cross-zone replication.
*   **TLS 1.3:** Mandatory encryption for all data in transit.
*   **Application-Layer Encryption:** PHI encrypted before caching to ensure data remains opaque.
*   **Debezium:** Change Data Capture for immediate cache invalidation.
*   **Envoy Proxy:** Sidecar pattern to abstract infrastructure concerns.
*   **Redis ACLs:** Granular control to restrict key access and disable dangerous commands.

## Rationale
This architecture ensures 99.99% availability through active-active replication and sidecar-based failover management. By combining application-layer encryption with CDC-driven invalidation, the system guarantees both clinical data accuracy and rigorous HIPAA/GDPR compliance.