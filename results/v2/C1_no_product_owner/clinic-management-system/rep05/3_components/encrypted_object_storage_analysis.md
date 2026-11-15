## Overview
The Encrypted Object Storage container provides secure, highly available, and compliant storage for medical documents, images, and audit trails within the Clinic Management System. It implements robust cryptographic controls, strict access policies, and automated lifecycle management to meet healthcare regulatory mandates.

## Key Elements
- S3 API Gateway Layer: MinIO/Ceph gateway handling HTTPS/S3 requests and TLS 1.3.
- Key Management & Envelope Encryption Engine: Manages per-object AES-256-GCM data encryption keys via Enterprise KMS.
- Replication & Erasure Coding Manager: Handles localized active-active replication, asynchronous geo-replication, Reed-Solomon erasure coding, and tiered storage.
- Audit Logging Interceptor: Captures metadata access events and streams them via gRPC.
- Policy & WORM Enforcer: Evaluates fine-grained access policies and enforces 10-year immutable WORM retention.

## Relationships
- Core Services -> S3 API Gateway Layer: Uploads and downloads encrypted blobs via HTTPS / S3 API.
- S3 API Gateway Layer -> Policy & WORM Enforcer: Validates request authorization and retention policies via in-process gRPC.
- Key Management Engine -> Enterprise KMS: Fetches Key Encryption Keys via gRPC / mTLS.
- Audit Logging Interceptor -> SIEM & Audit Platform: Emits access audit trails via Syslog / Kafka.

## Technology Stack
- MinIO / S3: Provides core object storage infrastructure and S3-compatible APIs.
- AES-256-GCM & Enterprise KMS: Delivers robust envelope encryption and key lifecycle management.
- TLS 1.3 & gRPC / mTLS: Secures transport layers and internal service communication.
- Object Lock (WORM): Enforces tamper-proof, 10-year medical data retention.

## Rationale
This architecture ensures strict HIPAA and GDPR compliance through envelope encryption, Zero-Trust authorization, and immutable WORM storage. It achieves the 99.99% availability requirement using localized active-active replication while balancing operational costs with automated tiered storage.