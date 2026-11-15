## Overview
- This hybrid architecture implements an immutable, zero-coupling Audit Sidecar Container for the Clinic Management System to ensure HIPAA and GDPR compliance.
- It securely captures, encrypts, and cryptographically signs core clinical application telemetry and access logs to guarantee a 10-year audit trail.

## Key Elements
- Log Interceptor (Fluentbit / Envoy sidecar proxy)
- Cryptographic Signer (Go / Rust micro-service using Merkle trees)
- Vault Agent (HashiCorp Vault Agent)
- Compliance Query Proxy (Go REST API)
- Compliance Officer (User role)
- Central SIEM / Immutable Storage (External storage)

## Relationships
- Core Clinical & EMR Container -> Log Interceptor: Sends local access logs and traces via Shared Volume / Unix Socket (gRPC)
- Log Interceptor -> Local Disk Buffer: Stores backpressure spillover via AES-256-GCM encrypted volume
- Cryptographic Signer -> Central SIEM / Immutable Storage: Streams signed audit bundles asynchronously via HTTPS (TLS 1.3)
- Compliance Officer -> Compliance Query Proxy: Queries audit integrity and proof-of-custody reports via HTTPS (TLS 1.3) with OAuth2/JWT

## Technology Stack
- Fluentbit / Envoy: Selected for lightweight local IPC log interception and low overhead.
- Go / Rust: Chosen for high-performance cryptographic hash-chaining and memory safety.
- HashiCorp Vault Agent: Implemented for dynamic secret injection and AES-256-GCM encryption key management.
- Unix Domain Sockets & gRPC: Utilized for high-throughput, low-latency local inter-container communication.

## Rationale
- Decouples audit logging from business logic to eliminate impact on core EMR screen load performance while guaranteeing zero audit loss.
- Enforces strict cryptographic immutability, mTLS, and encryption at rest to satisfy stringent healthcare security and regulatory mandates.