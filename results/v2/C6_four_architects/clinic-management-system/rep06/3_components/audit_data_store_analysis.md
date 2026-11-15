## Overview
The Audit Data Store container provides immutable, highly secure, and compliant log management for the Clinic Management System. It guarantees regulatory adherence, long-term data retention, and rapid audit query capabilities across hybrid cloud deployments.

## Key Elements
* Object Storage Engine (AWS S3 / MinIO WORM)
* Key Management Service (AWS KMS / HashiCorp Vault)
* Access Control Policy Enforcer
* Lifecycle Management Policy Engine
* Integrity Verification Monitor
* Audit Query & Export Gateway
* Audit Event Indexer / Metadata Catalog (OpenSearch)

## Relationships
* Audit & Compliance Log Shipper -> Object Storage Engine: Writes encrypted audit payloads via HTTPS [S3 API]
* Object Storage Engine -> Key Management Service: Requests envelope encryption keys via [gRPC/HTTPS]
* Lifecycle Management Policy Engine -> Object Storage Engine: Applies retention and tiering rules via [S3 Lifecycle API]
* Integrity Verification Monitor -> Object Storage Engine: Reads and validates block checksums via [S3 API]
* Regulatory/Audit Authority -> Audit Query & Export Gateway: Requests compliance reports and log exports via [HTTPS]
* Audit Query & Export Gateway -> Object Storage Engine: Retrieves verified audit objects via [HTTPS/S3 API]
* Object Storage Engine -> Audit Event Indexer: Streams new object creation events for indexing via [Kafka/Webhook]

## Technology Stack
* AWS S3 / MinIO Object Lock: Enforces WORM immutability for ≥ 10-year retention
* AWS KMS / HashiCorp Vault: Provides AES-256 encryption at rest with annual key rotation
* OpenSearch: Enables sub-second metadata indexing and searches without exposing raw PII
* HTTPS / S3 API: Secures data in transit and storage interactions

## Rationale
This architecture satisfies stringent HIPAA and GDPR compliance mandates through strict WORM immutability and robust encryption. It balances long-term data retention requirements with high-performance querying and cost-effective tiered storage.