## Overview
The Tokenization Proxy Container provides hardware-isolated card data tokenization within an AWS Nitro Enclave to ensure PCI-DSS Level 1 compliance. It securely processes payment payloads while maintaining sub-50ms P99 latency and a stateless memory footprint.

## Key Elements
- API Router: Rust (Hyper/Tokio) component handling gRPC request termination over vsock.
- Tokenization Core: Rust component managing ephemeral AES-GCM DEKs, `moka` in-memory LRU cache, and AWS KMS integration.
- Audit Logger: Rust component generating and forwarding cryptographic hashes for tamper-evident logging.
- Health & Attestation Monitor: Rust component managing cryptographic attestation and vsock health checks.
- Parent ECS Task: Orchestrator managing network and storage handoffs.

## Relationships
- Scoring Engine Container -> `gRPC over VSOCK` -> API Router: Sends cleartext PAN for tokenization/detokenization.
- Tokenization Core -> `HTTPS (TLS 1.3)` -> AWS KMS: Performs envelope encryption via parent VPC endpoint.
- Audit Logger -> `gRPC over VSOCK` -> Parent ECS Task: Streams tamper-evident audit hashes for S3 Object Lock ingestion.

## Technology Stack
- Rust (Hyper/Tokio): Chosen for memory safety and high-throughput concurrency within a small engineering team.
- AWS Nitro Enclaves: Selected for hardware-level isolation to satisfy PCI-DSS Level 1 requirements.
- VSOCK / gRPC: Used for internal secure communication, eliminating network attack surfaces.
- `moka` LRU Cache: Provides volatile memory caching for sub-millisecond data retrieval to meet the 50ms P99 latency budget.

## Rationale
This architecture enforces strict hardware isolation and zero disk persistence to meet compliance mandates within a fixed budget. Utilizing a unified Rust technology stack and in-memory caching ensures low latency while minimizing maintenance overhead for a three-person engineering team.