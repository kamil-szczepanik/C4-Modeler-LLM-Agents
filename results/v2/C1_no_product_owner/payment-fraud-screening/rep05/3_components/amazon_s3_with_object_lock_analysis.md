## Overview
This architecture implements a tamper-evident, 7-year audit storage solution using AWS S3 for a real-time payment fraud screening system. It ensures PCI-DSS Level 1 compliance while maintaining cost-efficiency for a three-person engineering team.

## Key Elements
* **Amazon S3 Bucket**: Core storage configured in S3 Compliance Mode with Object Lock for unalterable 7-year retention.
* **AWS KMS**: Manages customer-managed encryption keys (CMK) for server-side encryption.
* **Amazon S3 Gateway VPC Endpoint**: Enforces private, zero-trust network routing from the Fraud Scoring Engine.
* **S3 Lifecycle Management Engine**: Automatically transitions aged audit records to S3 Glacier Flexible Archive.
* **Cross-Region Replication (CRR)**: Replicates encrypted audit payloads to a secondary region (`eu-central-1`) for disaster recovery.

## Relationships
* **Fraud Scoring Engine** *writes* audit payloads to **Amazon S3 Bucket** via **Amazon S3 Gateway VPC Endpoint** using HTTPS (TLS 1.3).
* **Amazon S3 Bucket** *uses* **AWS KMS** for encryption-at-rest.
* **S3 Lifecycle Management Engine** *transitions* aged audit objects to **S3 Glacier Flexible Archive**.
* **Amazon S3 Bucket** *replicates* encrypted data to the secondary region storage via **Cross-Region Replication (CRR)**.

## Technology Stack
* **Amazon S3 Object Lock (Compliance Mode)**: Enforces strict write-once-read-many (WORM) constraints for mandatory 7-year audit retention.
* **AWS KMS**: Provides customer-managed encryption keys to meet strict cardholder data protection mandates.
* **Amazon S3 Lifecycle Policies**: Optimizes storage costs by shifting high-volume 3,000 TPS logs to archival storage.
* **Amazon S3 Gateway VPC Endpoint**: Secures network transit without incurring NAT gateway costs or exposing data to the public internet.

## Rationale
This architecture guarantees PCI-DSS Level 1 compliance and unalterable auditability (R-06) through S3 Object Lock and KMS encryption. Automated lifecycle management and VPC endpoints balance strict security and disaster recovery requirements within the 25,000 EUR monthly budget.