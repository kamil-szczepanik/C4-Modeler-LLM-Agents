## Overview
[The WORM Audit Logging Service provides immutable, secure log storage for the Clinic Management System to ensure HIPAA, GDPR, and 10-year data retention compliance. It processes asynchronous logs from clinical and billing workflows using encrypted queuing, cryptographic signing, and object-lock storage.]

## Key Elements
- Compliance Officers / Auditors [person, context]
- Ingestion API Component [component, Go, REST/gRPC]
- Secure Message Broker [component, Apache Kafka, TLS 1.3]
- Cryptographic Signing & Verifier Component [component, Rust, OpenSSL]
- WORM Storage Writer Component [component, Go, AWS S3 Object Lock / MinIO]
- Audit Query & Export Component [component, Go, GraphQL]

## Relationships
- Clinical Workspace -> Ingestion API Component (gRPC over mTLS, SPIFFE/SPIRE)
- Billing & Admin Suite -> Ingestion API Component (gRPC over mTLS, SPIFFE/SPIRE)
- Ingestion API Component -> Secure Message Broker (Encrypted Apache Kafka / TLS 1.3)
- Secure Message Broker -> Cryptographic Signing & Verifier Component (Internal gRPC)
- Cryptographic Signing & Verifier Component -> Hardware Security Module (HSM) (FIPS 140-2 / PKCS#11)
- Cryptographic Signing & Verifier Component -> WORM Storage Writer Component (Internal gRPC)
- WORM Storage Writer Component -> WORM Object Storage (AWS S3 Object Lock / MinIO)
- Compliance Officers / Auditors -> Audit Query & Export Component (HTTPS / TLS 1.3, OAuth 2.0 / OIDC, MFA)

## Technology Stack
- Go & Rust: Chosen for high performance and memory safety in core processing and cryptography.
- Apache Kafka: Provides durable, encrypted message brokering to prevent log loss during network partitions.
- AWS S3 Object Lock & MinIO: Enforces Write-Once-Read-Many (WORM) compliance across hybrid cloud storage.
- Hardware Security Module (HSM): Delivers FIPS 140-2 validated cryptographic key management and digital signing.

## Rationale
[This component architecture ensures non-repudiation, high availability, and hybrid cloud resilience for critical healthcare compliance mandates. Strict separation of concerns between ingestion, signing, storage, and querying guarantees data immutability and regulatory audit readiness.]