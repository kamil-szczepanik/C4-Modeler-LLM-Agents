## Overview
The Immutable Audit Log component ensures HIPAA and GDPR compliance for the Clinic Management System by maintaining tamper-proof, cryptographically chained audit trails. It provides secure 10-year data retention while supporting high-availability clinical operations.

## Key Elements
- Compliance Officer (Persona)
- Audit Ingestion API (Java / Spring Boot)
- Cryptographic Signer Component (Java / Bouncy Castle)
- Ledger Storage Engine (AWS QLDB / Append-Only PostgreSQL)
- Compliance Export Service (Java / Spring Boot)
- AWS CloudHSM Cluster

## Relationships
- Core Clinical & EMR Service -> Audit Ingestion API: Appends event payloads via `gRPC / TLS 1.3`
- Audit Ingestion API -> Cryptographic Signer Component: Requests event signing via `In-Process Method Call`
- Cryptographic Signer Component -> AWS CloudHSM: Signs and chains log entries via `PKCS#11 / TLS`
- Cryptographic Signer Component -> Ledger Storage Engine: Commits verifiable blocks via `JDBC / TLS`
- Compliance Officer -> Compliance Export Service: Generates tamper-proof reports via `HTTPS / TLS 1.3`
- Compliance Export Service -> S3 Object Lock: Queries historical audit records via `AWS SDK / HTTPS`

## Technology Stack
- Java & Spring Boot: Ensures high-throughput, enterprise-grade reliability for ingestion and export APIs.
- AWS CloudHSM: Provides secure, dedicated key custody and cryptographic operations meeting strict compliance standards.
- AWS QLDB / Append-Only PostgreSQL: Enforces write-once-read-many (WORM) immutability semantics.
- S3 Object Lock (Compliance Mode): Cost-effectively stores historical logs for the mandatory 10-year retention period.
- Bouncy Castle: Implements cryptographic hashing and chaining algorithms.

## Rationale
This architecture isolates sensitive compliance workloads to prevent degradation of core EMR performance while strictly enforcing non-repudiation. Utilizing AWS cloud-native secure storage and HSM guarantees 99.99% availability and uncompromised regulatory compliance.