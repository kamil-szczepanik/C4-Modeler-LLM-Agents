## Overview
The Key Management Service provides secure cryptographic operations and key lifecycle management for the Clinic Management System. It ensures HIPAA and GDPR compliance while maintaining high availability across hybrid cloud environments.

## Key Elements
- KMS API Gateway Component: Standardized ingress interface for cryptographic requests.
- Crypto Engine: Executes envelope encryption primitives with in-process ephemeral memory.
- Key Lifecycle Manager: Manages automated key rotation, Master Keys (KEKs), and secure shredding.
- Audit & Access Control Enforcer: Validates mTLS identities and logs key access immutably.
- HSM Integration Layer: Abstracts hardware security module interactions for root keys.
- Key Replication Synchronizer: Handles secure cross-region and cross-cluster replication.

## Relationships
- Core Clinical Microservice invokes KMS API Gateway Component via gRPC over mTLS.
- KMS API Gateway Component delegates requests to Crypto Engine.
- Key Lifecycle Manager interacts with HSM Integration Layer via PKCS#11 / gRPC.
- Key Lifecycle Manager uses Key Replication Synchronizer via gRPC over mTLS.
- Key Lifecycle Manager reads/writes encrypted key material to CockroachDB (Encrypted) using SQL over TLS.
- Audit & Access Control Enforcer streams access logs to Audit Log Store via Kafka.

## Technology Stack
- Go: Used for Crypto Engine, Key Lifecycle Manager, and KMS API Gateway for performance and memory safety.
- HashiCorp Vault SDK / Raft: Implements key management lifecycle and consensus-based replication.
- PKCS#11: Standardizes Hardware Security Module (HSM) integration for FIPS 140-2 Level 3 compliance.
- Open Policy Agent (OPA) / Istio: Enforces access control and mTLS validation.
- Kafka: Transmits tamper-resistant audit logs to the Audit Log Store.

## Rationale
The six-component architecture separates cryptographic execution, lifecycle management, and hardware integration to satisfy strict HIPAA/GDPR data security mandates. Raft consensus and multi-region replication guarantee 99.99% availability across on-premises Kubernetes and AWS `eu-central-1`.