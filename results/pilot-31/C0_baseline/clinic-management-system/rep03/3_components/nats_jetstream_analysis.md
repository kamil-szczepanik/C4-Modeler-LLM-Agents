## Overview
The Clinic Management System is a hybrid-cloud platform designed for clinical operations, EMR management, and billing. It ensures high availability and regulatory compliance through a secure, event-driven architecture.

## Key Elements
*   **Services:** Patient, EMR, Billing, Patient Portal, FHIR Integration Gateway
*   **Infrastructure:** NATS JetStream (Event Bus), PostgreSQL (Read-optimized audit/data), Redis (Caching)
*   **Security:** Identity Provider (IdP), HSM/KMS (Key Management)
*   **External:** Payment Gateway, Diagnostic Systems (HL7 FHIR)

## Relationships
*   **Services to NATS:** Asynchronous communication via NATS JetStream (Pub/Sub) using TLS/mTLS and User JWTs.
*   **NATS to Storage:** File-backed persistent volumes with Envelope Encryption for PHI.
*   **NATS to Cold Storage:** Asynchronous archival via dedicated sidecar to S3/GCS with Object Lock.
*   **NATS to Audit View:** Projection service populates PostgreSQL for administrator reporting.
*   **System to External:** HL7 FHIR APIs for interoperability with diagnostic systems.

## Technology Stack
*   **NATS JetStream:** Clustered (3-5 nodes) with RAFT consensus for 99.99% availability.
*   **Envelope Encryption:** AES-256 for PHI field-level protection via KMS.
*   **NATS Leaf Nodes:** Bridge on-prem and cloud sites to mitigate WAN latency.
*   **NATS Account/JWT Auth:** Enforces granular, cryptographically verifiable multi-tenancy.
*   **Prometheus/Grafana:** Observability for cluster health, consumer lag, and storage metrics.

## Rationale
This architecture uses NATS JetStream with RAFT consensus and leaf nodes to meet 99.99% availability and hybrid-cloud latency requirements. Envelope encryption and immutable audit streams ensure HIPAA/GDPR compliance while maintaining system performance for clinical staff.