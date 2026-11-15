## Overview
The Billing Service is a core component of the Clinic Management System designed to handle clinical financial transactions, insurance claims, and audit-compliant reporting. It ensures high-availability billing operations while maintaining strict HIPAA/GDPR compliance for long-term financial data.

## Key Elements
*   **Billing Service (Go):** Primary container comprising the Invoice Orchestrator, Claim Processor, and Payment Gateway Adapter.
*   **Reporting & Reconciliation Engine:** Dedicated component for analytical queries and financial snapshots.
*   **Audit Log Aggregator:** Sidecar/service for capturing, signing, and streaming immutable financial audit trails.
*   **PostgreSQL:** Primary transactional database with read-replicas.
*   **NATS JetStream:** Message broker for asynchronous claim processing.
*   **Immutable Event Store:** Encrypted, long-term storage for audit logs (S3 Glacier).

## Relationships
*   **Billing Service ↔ EMR Service:** Saga pattern for distributed transactions; mTLS/gRPC for secure communication.
*   **Billing Service ↔ Payment Gateway:** Outbound traffic via egress proxy with domain whitelisting and `gobreaker` circuit breakers.
*   **Billing Service ↔ PostgreSQL:** Parameterized SQL queries with TDE and CMK encryption.
*   **Billing Service ↔ Audit Log Aggregator:** gRPC interface with certificate pinning and cryptographic event signing.
*   **Reporting Engine ↔ PostgreSQL Read-Replica:** Read-only access via database proxies with Row-Level Security (RLS).

## Technology Stack
*   **Language:** Go (High-performance concurrency for billing logic).
*   **Messaging:** NATS JetStream (Reliable asynchronous message delivery).
*   **Resiliency:** `gobreaker` (Circuit breaking for external API calls).
*   **Security:** mTLS, ABAC, TDE with CMK (Key management via HSM/Cloud KMS).
*   **Observability:** Synthetic monitoring and DLQ depth tracking.

## Rationale
This architecture uses the Saga pattern and asynchronous processing to ensure 99.99% availability and transactional integrity across hybrid environments. Decoupling audit and reporting components ensures regulatory compliance and performance without impacting core financial throughput.