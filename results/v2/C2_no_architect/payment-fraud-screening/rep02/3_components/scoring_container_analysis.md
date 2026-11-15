## Overview
The Real-Time Payment Fraud Screening system evaluates card-not-present payment authorizations to detect fraud and manage analyst reviews. It ensures sub-50ms P99 latency at 3,000 TPS while maintaining strict PCI-DSS Level 1 compliance.

## Key Elements
- AWS Application Load Balancer (ALB)
- Scoring Container (AWS ECS Fargate)
- Amazon Aurora Serverless
- Amazon S3 with Object Lock
- AWS KMS, AWS Secrets Manager, and AWS IAM
- AWS CloudWatch and AWS Signer

## Relationships
- AWS ALB -> Scoring Container: Routes payment authorization traffic via mTLS and ECS Service Connect.
- Scoring Container -> Amazon Aurora Serverless: Queries transaction context via internal TCP/TLS.
- Scoring Container -> Amazon S3 with Object Lock: Streams cryptographically signed decision logs via AWS SDK and AWS KMS.

## Technology Stack
- AWS ECS Fargate: Chosen to balance automated scaling with minimal operational overhead for a three-engineer team.
- Local Container Memory Caching: Caches model weights locally to meet the strict sub-50ms latency requirement.
- AWS KMS & AWS Secrets Manager: Enforces AES-256 encryption at rest and secure secret injection for PCI-DSS compliance.
- AWS Signer: Ensures runtime integrity via container image signature verification at task launch.

## Rationale
This architecture leverages serverless containers and local caching to achieve high-throughput, low-latency payment screening within a fixed budget. Security and auditability controls ensure full compliance with PCI-DSS Level 1 and 7-year regulatory mandates.