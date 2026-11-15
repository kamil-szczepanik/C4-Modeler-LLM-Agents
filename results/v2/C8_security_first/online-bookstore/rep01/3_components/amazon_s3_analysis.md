## Overview
- Secure, scalable object storage architecture utilizing Amazon S3 for an e-commerce online bookstore.
- Designed to handle static frontend assets, digital e-book downloads, and multi-region system backups while maintaining GDPR/CCPA compliance and high availability across three AWS regions.

## Key Elements
- **S3 Buckets**: Logically separated into `bookstore-assets-prod`, `bookstore-digital-products-prod`, and `bookstore-backups-prod`.
- **Amazon S3 Event Notifications**: Integrates with Amazon EventBridge for asynchronous event-driven workflows.
- **AWS Key Management Service (KMS)**: Manages encryption keys with automated rotation.
- **Amazon CloudFront / OAC**: Delivers static assets and routes accelerated uploads.
- **AWS Lambda & Amazon Macie**: Executes asynchronous malware and PII scanning on uploaded objects.

## Relationships
- **End-Users / CloudFront to S3**: Serves public frontend assets via Amazon CloudFront Origin Access Control (OAC) using HTTPS/TLS 1.2+.
- **Catalog/Order Service to S3 Digital Bucket**: Generates 15-minute Amazon S3 Presigned URLs via HTTPS for secure e-book delivery.
- **S3 to EventBridge / Admin Service**: Emits `ObjectCreated` HTTPS events upon author uploads to trigger virus and PII scans.
- **S3 to S3 (CRR)**: Asynchronously replicates critical backup and digital asset buckets across `us-east-1`, `eu-west-1`, and `ap-southeast-1`.

## Technology Stack
- **Amazon S3**: Object storage chosen for durability, scalability, and built-in replication.
- **AWS KMS**: Server-side encryption with customer-managed keys (CMKs) to satisfy compliance.
- **Terraform / AWS CDK**: Infrastructure as Code for repeatable provisioning and drift detection.
- **Amazon S3 Glacier**: Cost-optimization tiering for archived digital assets and backups.

## Rationale
- Enforces strict deny-by-default security, TLS 1.3/1.2, and KMS encryption to ensure GDPR/CCPA compliance and protect intellectual property.
- Leverages cross-region replication, S3 Transfer Acceleration, and lifecycle policies to achieve 99.95% availability, sub-2-second performance, and cost-effective scalability for 1M MAU.