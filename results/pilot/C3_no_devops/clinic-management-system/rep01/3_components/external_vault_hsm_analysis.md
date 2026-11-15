## Overview
The External Vault/HSM secures encryption keys and sensitive secrets for the Clinic Management System. It ensures cryptographic protection and regulatory compliance across hybrid clinical deployments.

## Key Elements
- Transit Secrets Engine for envelope encryption
- KV Secret Engine for dynamic credential rotation
- Hardware Security Root of Trust (FIPS 140-2 Level 3 validated)
- HashiCorp Vault Enterprise (clustered)
- Thales Luna (on-prem-k8s) and AWS CloudHSM (eu-central-1)
- EMR Service and Billing Service

## Relationships
- EMR Service and Billing Service to External Vault/HSM via gRPC over mutual TLS (mTLS)
- Vault client integration via Vault Go SDK using AppRole authentication
- Endpoints accessed: `/v1/transit` API and `/v1/secret` API
- Cryptographic hardware operations via PKCS#11 interfaces

## Technology Stack
- HashiCorp Vault Enterprise: Selected for robust secret management and enterprise clustering.
- Thales Luna / AWS CloudHSM: Chosen for FIPS 140-2 Level 3 hardware security compliance.
- Vault Raft Storage Backend: Used for encrypted state replication across hybrid nodes.
- TLS 1.3 with mTLS: Enforced for secure transport-layer communication.

## Rationale
This architecture satisfies strict HIPAA and GDPR mandates through hardware-backed cryptographic controls and zero-knowledge storage. It delivers 99.99% availability via hybrid clustering and automated multi-party unsealing.