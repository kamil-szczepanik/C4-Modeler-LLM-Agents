## Overview
The Read-Only Analytics Service provides high-level operational insights for hospital leadership while offloading complex reporting from the transactional EMR. It ensures HIPAA/GDPR compliance and 99.99% availability through asynchronous data processing and strict access controls.

## Key Elements
*   **Aggregation Controller (Spring Boot):** Handles RESTful reporting requests.
*   **Query Orchestrator (Spring Integration):** Manages asynchronous data fetching from ClickHouse.
*   **Privacy Proxy (Spring Security/Sidecar):** Enforces ABAC, dynamic data masking, and egress filtering.
*   **Audit Interceptor:** Logs query context and access metadata to an immutable store.
*   **Metadata Service:** Monitors Debezium replication lag for data freshness transparency.
*   **ClickHouse:** Analytical data store for historical trends.
*   **HashiCorp Vault:** Manages secrets and field-level encryption keys.

## Relationships
*   **Debezium:** Streams transactional data from PostgreSQL to ClickHouse.
*   **Istio Service Mesh:** Manages mTLS, traffic routing, and policy enforcement across hybrid environments.
*   **REST/HTTPS:** Protocol for client queries and inter-service communication.
*   **Vault API:** Used for dynamic credential rotation and cryptographic key retrieval.

## Technology Stack
*   **Java/Spring Boot:** Core application framework for high-performance service logic.
*   **ClickHouse:** Chosen for high-speed analytical query performance.
*   **Istio:** Implements sidecar pattern for consistent security and traffic management.
*   **Debezium:** Enables reliable Change Data Capture (CDC) for near real-time data sync.
*   **HashiCorp Vault:** Ensures secure key management and field-level encryption for PII.

## Rationale
This architecture decouples heavy analytical workloads from the EMR to maintain sub-second transactional performance. The use of a Privacy Proxy and Audit Interceptor ensures strict regulatory compliance while providing the transparency required for clinical decision-making.