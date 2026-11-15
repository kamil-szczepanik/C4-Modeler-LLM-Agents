## Overview
AWS-hosted real-time payment fraud screening system processing card-not-present authorizations with a tamper-evident 7-year audit sidecar. Designed for a 3-engineer team under a €25,000 monthly budget.

## Key Elements
- Real-Time Scoring Engine (AWS ECS Fargate)
- Audit & Cryptographic Sidecar (AWS ECS Fargate, local encrypted tmpfs/EBS buffer)
- AWS KMS (Asymmetric signing and envelope encryption)
- Amazon S3 WORM Bucket with S3 Glacier Flexible Retrieval and Object Lock

## Relationships
- Real-Time Scoring Engine -> Audit Sidecar: Sends logs [Local gRPC over mTLS]
- Audit Sidecar -> AWS KMS: Generates cryptographic signatures and seals log batches [AWS SDK (HTTPS)]
- Audit Sidecar -> Amazon S3 WORM Bucket: Stores immutable audit logs [AWS SDK (HTTPS)]

## Technology Stack
- AWS ECS Fargate: Container orchestration within the €25,000 budget
- AWS KMS: Fully managed cryptographic signing replacing AWS CloudHSM to reduce operational toil
- Amazon S3 Object Lock & Glacier Flexible Retrieval: Cost-effective 7-year immutable retention
- Local encrypted tmpfs/EBS: Secure buffering for the 1-minute failover window (R-07)

## Rationale
AWS KMS and S3 WORM eliminate operational overhead while enforcing PCI-DSS Level 1 compliance and 7-year tamper-evident auditability. Encrypted local buffering protects P99 latency SLAs under 50 ms at 3,000 TPS.