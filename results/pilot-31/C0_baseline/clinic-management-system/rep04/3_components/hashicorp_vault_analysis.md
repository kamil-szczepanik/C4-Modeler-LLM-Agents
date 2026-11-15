## Overview
The Clinic Management System is a hybrid-cloud healthcare platform designed for managing patient records, scheduling, and billing. It ensures high availability and strict regulatory compliance (HIPAA/GDPR) for sensitive medical data.

## Key Elements
*   **Vault Cluster:** Multi-node Raft-integrated cluster (primary on-prem, secondary in `eu-central-1`).
*   **Core EMR Service:** Spring Boot application consuming secrets and PHI encryption.
*   **Vault Agent Sidecar:** Local cache and secret injector for microservices.
*   **Vault Secret Operator:** Kubernetes CRD-based management for developer workflows.
*   **WORM Storage:** Immutable destination for audit logs.
*   **Transit Secret Engine:** Centralized cryptographic offloading for PHI.

## Relationships
*   **Core EMR Service -> Vault Agent:** Local shared memory volume access (no blocking API calls).
*   **Vault Cluster -> Vault Cluster:** Performance Replication via Raft protocol.
*   **Vault Audit Device -> WORM Storage:** Log streaming via FluentBit sidecar.
*   **Workloads -> Vault:** mTLS-encrypted communication using SPIFFE IDs.
*   **Vault -> Cloud KMS/HSM:** Seal Wrapping for master key protection.

## Technology Stack
*   **HashiCorp Vault:** Centralized secret management and Transit Engine for AES-256 encryption.
*   **Kubernetes Auth Method:** Identity-based access control binding service accounts to policies.
*   **FluentBit:** Log forwarding for immutable audit trails.
*   **Prometheus/Grafana:** Monitoring for unseal status and Transit API throughput.
*   **KMS/HSM:** Hardware-backed protection for master keys (AWS KMS and on-prem HSM).

## Rationale
This architecture utilizes a hybrid Raft-replicated cluster to meet 99.99% availability while minimizing latency for the EMR service. Centralizing encryption via the Transit Engine and enforcing identity-based access ensures rigorous compliance with HIPAA and GDPR requirements.