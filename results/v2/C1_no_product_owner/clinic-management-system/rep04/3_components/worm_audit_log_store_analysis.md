## Overview
• Component-level architecture for the WORM Audit Log Store in the Clinic Management System.
• Ensures tamper-proof 10-year audit retention, HIPAA/GDPR compliance, and cryptographic integrity.

## Key Elements
• Ingestion API Router (Go / Gin)
• Encryption & Hashing Engine (Tink / OpenSSL with PKCS#11)
• Immutability Enforcer (AWS Object Lock / MinIO WORM mode)
• Audit Query Service (Go / Elasticsearch with ILM tiers)
• Replication Synchronizer (MinIO / S3 Cross-Region Replication)

## Relationships
• Microservices -> Ingestion API Router: Stream audit logs [gRPC over mTLS / SPIFFE/SPIRE]
• Ingestion API Router -> Encryption & Hashing Engine: Passes payloads for cryptographic sealing [In-memory]
• Encryption & Hashing Engine -> Immutability Enforcer: Writes sealed logs [S3 API with Object Lock]
• Immutability Enforcer -> Replication Synchronizer: Replicates immutable objects [Encrypted IPsec/WireGuard tunnels]
• Audit Query Service -> Immutability Enforcer: Reads objects strictly via WORM-compliant APIs [GET/LIST]

## Technology Stack
• Go / Gin: High-performance routing and schema validation
• Tink / OpenSSL & HSM: AES-256 envelope encryption and Merkle tree generation
• AWS Object Lock / MinIO WORM: Enforces 10-year immutable storage retention
• Elasticsearch: Search indexing with hot-warm-cold-frozen ILM tiers
• SPIFFE/SPIRE & mTLS: Zero-trust workload identity and cross-region transport security

## Rationale
• Guarantees strict HIPAA/GDPR adherence and tamper-evidence through HSM-backed cryptographic sealing and WORM immutability.
• Balances rigorous compliance constraints with high-availability hybrid cloud replication and efficient long-term audit querying.