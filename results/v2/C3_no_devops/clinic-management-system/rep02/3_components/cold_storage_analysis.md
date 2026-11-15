## Overview
[The Clinic Management System archives historical Electronic Medical Records to ensure strict 10-year data retention compliance. It securely stores, encrypts, and retrieves clinical audit data via tiered restoration workflows without impacting primary database performance.]

## Key Elements
* AWS S3 Glacier Flexible Retrieval / Ceph Object Storage
* Go-based Archival Worker Component
* Retrieval API Component
* Job Orchestration Component (AWS SQS / Redis)
* Data Transformation Component / Parser Module
* Audit & Compliance Daemon Container

## Relationships
* EMR Database -> Storage Engine: Asynchronously streams partitioned Parquet files via TLS 1.3
* Retrieval API -> Job Orchestration: Enqueues hydration tasks via Internal IPC / Redis
* Job Orchestration -> Storage Engine: Initiates restoration jobs via AWS SDK / S3 API over TLS 1.3
* Retrieval Engine -> Audit & Compliance Daemon: Delivers decrypted historical records via HTTPS / mTLS

## Technology Stack
* AWS S3 Glacier / Ceph Object Storage: Ensures secure, cost-effective long-term data retention with WORM immutability
* Go: Powers lightweight archival and background worker processes
* AES-256 with customer-managed keys: Satisfies strict encryption-at-rest mandates
* TLS 1.3 / mTLS: Secures all data in transit across system boundaries

## Rationale
[This architecture strictly enforces HIPAA and GDPR compliance through WORM storage and AES-256 encryption. Furthermore, the decoupled job orchestration and tiered retrieval mechanisms satisfy aggressive audit requirements while maintaining high system performance.]