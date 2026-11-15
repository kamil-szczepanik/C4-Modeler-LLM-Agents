## Overview
- Real-Time Payment Fraud Screening system screens card-not-present payment authorizations for fraud and manages analyst reviews.
- Operates under strict PCI-DSS Level 1 compliance and a 7-year tamper-evident auditability constraint.

## Key Elements
- Fraud Analyst / Risk Manager
- Compliance Officer / Internal Auditor
- Regulator / Card Scheme Investigator
- API Gateway (Nginx / AWS ALB)
- Fraud Scoring Engine (Go with embedded ONNX Runtime)
- Case Management Service (Node.js / TypeScript)
- Audit & Compliance Ledger (Rust)
  - Ledger Ingestion Component
  - Cryptographic Sealer Component
  - Storage & Export Component
  - Compliance Query & Export Component
- Analytics Export Stream (Fluent Bit sidecar)
- Data Store (AWS Aurora PostgreSQL & Amazon Redis)
- Secure Audit Archive (Amazon S3 Object Lock)
- Identity Provider
- Payment Gateway / Processing Engine
- Payment Card Network / Tokenization Vault
- AWS KMS

## Relationships
- Payment Gateway / Processing Engine -> API Gateway: Submits authorization requests [HTTPS (TLS)]
- API Gateway -> Fraud Scoring Engine: Routes scoring requests [gRPC / HTTP/2]
- Fraud Scoring Engine -> Audit & Compliance Ledger: Sends decision payloads [gRPC via mTLS]
- Audit & Compliance Ledger -> Secure Audit Archive: Stores raw payloads and writes daily Merkle roots [HTTPS (TLS) / S3 API]
- Audit & Compliance Ledger -> AWS KMS: Signs Merkle root hashes [AWS KMS API]
- Compliance Officer / Regulator -> Audit & Compliance Ledger: Queries and exports audit bundles [HTTPS (TLS) via OAuth2/OIDC]
- Audit & Compliance Ledger -> AWS Aurora PostgreSQL: Persists metadata and Merkle blocks [PostgreSQL Wire Protocol (TLS)]

## Technology Stack
- Rust: Chosen for the Audit & Compliance Ledger for memory safety and minimal operational overhead for a 3-person team.
- AWS Aurora PostgreSQL: Stores immutable append-only ledgers and Merkle metadata.
- Amazon S3 Object Lock: WORM storage for cost-effective 7-year raw payload retention.
- AWS KMS: Secures cryptographic non-repudiation via digital signing of Merkle tree roots.
- Go & Node.js: Utilized for high-performance scoring and case management containers.

## Rationale
- The architecture meets sub-50ms latency and strict 25,000 EUR monthly budget constraints through efficient Merkle tree batching and S3 offloading.
- It guarantees PCI-DSS Level 1 compliance and 7-year tamper-evident auditability without exceeding the operational capacity of a three-engineer team.