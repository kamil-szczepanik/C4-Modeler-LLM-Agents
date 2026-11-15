## Overview
The Clinic Management System (CMS) is a hybrid cloud healthcare platform managing patient admissions, EMRs, scheduling, and billing. It provides high availability, stringent security, and interoperability for medium-sized hospitals and clinics.

## Key Elements
- Authorized Containers (Core Services, EMR Service, Database Layer)
- Client SDK Wrapper (Java/Node.js/Go)
- Access Control & Policy Enforcer (OPA/Vault ACLs)
- Key Manager Component (Java / Spring Vault SDK)
- Crypto-Worker Component (Go)
- Transit Secrets Engine Component (HashiCorp Vault Transit)
- Secrets Engine Component (HashiCorp Vault KV)
- Key Rotation Worker (Go / Cron)
- Key Expiry & Revocation Manager (Go)
- Key Sync & Replication Manager (Go)
- HSM Integration Layer (PKCS#11 wrapper)
- External KMS Interoperability Adapter (Go / AWS SDK)
- Key Health & Readiness Probe (Go)
- Backup & Recovery Agent (Python/Go)
- AWS KMS / Cloud Backup (AWS S3 Glacier)

## Relationships
- Authorized Containers (via Client SDK Wrapper) -> Access Control & Policy Enforcer: Accesses keys and policies [gRPC over TLS with mTLS]
- Key Manager Component -> HSM Integration Layer: Executes hardware-backed cryptographic operations [PKCS#11 / TLS 1.3]
- Key Manager Component -> Key Sync & Replication Manager: Replicates encrypted key metadata [Raft Consensus / TLS 1.3]
- External KMS Interoperability Adapter -> AWS KMS (`eu-central-1`): Synchronizes cloud-native cryptographic primitives [HTTPS/REST with SigV4 and TLS 1.3]
- Backup & Recovery Agent -> Cloud Backup (AWS S3 Glacier): Exports encrypted KMS snapshots and key metadata [HTTPS/REST with AWS SigV4]

## Technology Stack
- Java / Spring Boot & Node.js: Core and EMR service containers for business logic.
- HashiCorp Vault & AWS KMS: Cryptographic backbone for envelope encryption and key management.
- Go & Python: Lightweight micro-components for crypto-workers, synchronization, and backup agents.
- PKCS#11: Standard interface for hardware-backed key operations via HSM.
- gRPC over TLS with mTLS: Secure, low-latency transport protocol for zero-trust service communication.

## Rationale
The architecture enforces zero-trust boundaries by restricting direct KMS access to authorized data stores and core services via an Access Control and Policy Enforcer. Local DEK caching via the Client SDK Wrapper ensures EMR screen loads remain below the 1-second P95 performance requirement.