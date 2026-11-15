## Overview
The system provides real-time fraud screening for payment authorizations while maintaining tamper-evident compliance records. It processes transactions securely, isolates cardholder data, and ensures auditable decision histories.

## Key Elements
* AWS QLDB (Quantum Ledger Database)
* Amazon SQS (Audit Queue)
* AWS Lambda (Export Worker & Audit Ingestion Service)
* Amazon EventBridge (Scheduler)
* AWS S3 Object Lock (Journal S3 Export Bucket)
* AWS KMS & AWS Secrets Manager
* Scoring Engine Container (Rust or Go)

## Relationships
* Amazon SQS (Audit Queue) -> AWS QLDB: Commits batched cryptographic records via QLDB Driver [HTTPS/TLS 1.3, AWS SDK]
* Amazon EventBridge (Scheduler) -> AWS Lambda (Export Worker): Triggers periodic ledger exports [Cron/HTTPS]
* AWS Lambda (Export Worker) -> AWS QLDB: Exports historical journal blocks using `ExportJournalToS3` [AWS SDK/HTTPS]
* AWS QLDB (Journal S3 Export Bucket) -> AWS S3 Object Lock: Stores long-term archival data [S3 API]

## Technology Stack
* AWS QLDB: Immutable ledger for 7-year regulatory compliance records
* Amazon SQS: Asynchronous batching to optimize transaction I/O costs and prevent rate-limiting
* AWS S3 Object Lock: Compliance Mode storage for cost-effective 7-year data archiving
* AWS KMS: Customer Managed Keys (CMK) with annual rotation for encrypted data at rest
* TLS 1.3: Enforces secure data in transit across all component boundaries

## Rationale
Decoupled asynchronous batching prevents QLDB I/O overhead from violating the strict sub-50ms fraud screening latency constraint. Serverless S3 archiving and optimized batching keep infrastructure costs safely within the fixed 25,000 EUR monthly budget for a three-engineer team.