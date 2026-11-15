## Overview
The Billing Service is a containerized Go-based system designed to manage financial transactions, insurance claims, and revenue cycle reporting for the Clinic Management System. It ensures HIPAA/GDPR compliance and 99.99% availability through a hybrid-cloud, event-driven architecture.

## Key Elements
*   **Billing Service (Go):** Core container managing financial state.
    *   *Invoice Manager:* Handles billing cycle state transitions.
    *   *Payment Processor:* Manages external gateway interactions.
    *   *Clearinghouse Integration Gateway:* Handles asynchronous claim submissions.
    *   *Dispute & Reconciliation Engine:* Manages collection pauses and audits.
    *   *Event-Driven Reporting Projection:* CQRS-based read-optimized aggregator.
*   **Infrastructure:** PostgreSQL (CloudNativePG), NATS (Message Queue), HashiCorp Vault, Service Mesh (Sidecar pattern).

## Relationships
*   **Spring Cloud Gateway -> Billing Service:** Request forwarding via mTLS.
*   **Billing Service -> NATS:** Asynchronous claim submission and event streaming.
*   **Billing Service -> External Billing Gateway:** Outbound API calls via Egress Proxy with circuit breakers.
*   **Billing Service -> PostgreSQL:** Data persistence with field-level encryption and Row-Level Security (RLS).
*   **Service Mesh Sidecar:** Handles mTLS termination, retries, and rate-limiting.

## Technology Stack
*   **Language:** Go (High-performance billing logic).
*   **Communication:** NATS (Decoupling/Asynchronous processing), mTLS/gRPC (Internal service communication).
*   **Persistence:** PostgreSQL with CloudNativePG (Active-active failover/High availability).
*   **Security:** HashiCorp Vault (Dynamic secret injection), AES-256 (At-rest encryption).
*   **Pattern:** CQRS (Separation of transactional and analytical reporting workloads).

## Rationale
The CQRS pattern and event-driven architecture decouple high-throughput transaction processing from analytical reporting, ensuring sub-second performance for financial dashboards. The hybrid-cloud deployment with CloudNativePG and sidecar-managed mTLS satisfies the 99.99% availability and strict security requirements for PHI/PII data.