## Overview
The WORM-compliant S3 / MinIO container provides secure, highly available, and immutable object storage for electronic medical records and medical imaging files. It supports hybrid multi-site deployments while ensuring compliance with 10-year data retention and healthcare privacy regulations.

## Key Elements
- Object Storage Engine (MinIO Server in Erasure Coding mode)
- Object Locking & Retention Manager (AWS-compatible Object Lock in `COMPLIANCE` mode)
- IAM & Policy Enforcer (MinIO IAM / Open Policy Agent with HashiCorp Vault)
- Replication & Tiering Controller (MinIO Replication & Lifecycle Engine)
- External AWS S3 (`eu-central-1`) and HashiCorp Vault

## Relationships
- EMR Core Service -> Object Locking & Retention Manager: Uploads and reads encrypted medical objects via S3 API over TLS 1.3
- Object Storage Engine <-> AWS S3: Replicates immutable payloads via S3 API over TLS 1.3 (Cross-Site Replication)
- IAM & Policy Enforcer -> HashiCorp Vault: Fetches dynamic KMS keys via Vault Transit Secrets Engine API over HTTPS

## Technology Stack
- MinIO (Erasure Coding mode): Chosen for high-throughput binary storage and S3 API compatibility
- MinIO Object Lock (`COMPLIANCE` mode): Enforces immutable 10-year data retention to prevent deletion or tampering
- HashiCorp Vault (Transit Secrets Engine): Provides Server-Side Encryption with Customer-Managed Keys (SSE-CMEK) using AES-256
- Istio Service Mesh: Enforces mutual TLS (mTLS 1.3) for secure service-to-service communication
- Prometheus: Scrapes MinIO metrics for real-time storage and replication health monitoring

## Rationale
This architecture ensures 99.99% availability through hybrid active-active replication between on-premise infrastructure and AWS `eu-central-1`. Strict cryptographic controls and WORM compliance satisfy HIPAA, GDPR, and long-term audit mandates.