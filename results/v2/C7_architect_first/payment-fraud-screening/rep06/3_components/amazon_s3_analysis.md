## Overview
A real-time payment fraud screening system processes card-not-present payment authorizations to detect fraud and manage reviews. It ensures strict compliance and auditability within fixed infrastructure constraints.

## Key Elements
* Amazon S3 Standard Bucket (`Fraud-Audit-Active`)
* Amazon S3 Object Lock Configuration (`WORM-Policy`)
* Amazon S3 Lifecycle Management Engine
* Amazon Athena Query Layer
* AWS KMS Customer Managed Keys (CMK)
* Amazon MSK Serverless
* AWS Config

## Relationships
* Amazon MSK Serverless -> Amazon S3 Standard Bucket: Persists raw authorization inputs, model versions, and decisions via Amazon S3 Sink Connector (HTTPS/REST with TLS 1.3)
* Regulatory Auditors -> Amazon Athena / S3 Object Lock: Queries parquet-formatted audit logs in place for compliance reviews via Pre-signed URLs (HTTPS)

## Technology Stack
* Amazon S3 Object Lock (Compliance Mode): Enforces Write-Once-Read-Many (WORM) storage for 7-year tamper-evident audit retention (R-06).
* Amazon Athena: Provides low-cost, serverless querying over audit logs without dedicated database overhead.
* Apache Parquet: Optimizes long-term storage footprints and query performance for stored audit data.
* AWS KMS (SSE-KMS): Encrypts data at rest using Customer Managed Keys to meet PCI-DSS Level 1 standards (R-05).
* S3 Glacier Flexible Archive: Automates lifecycle transitions after 30 days to stay within the €25k/month budget.

## Rationale
The architecture satisfies PCI-DSS Level 1 and 7-year audit requirements using tamper-evident WORM storage while maintaining low query costs. Serverless components and intelligent tiering ensure the solution operates efficiently within the strict €25,000 monthly budget.