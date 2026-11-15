## Overview
The Real-Time Payment Fraud Screening system screens card-not-present payment authorizations at 3,000 TPS to protect a mid-size payment processor against fraud. It provides sub-50ms automated scoring and case management for human analysts while strictly enforcing PCI-DSS Level 1 compliance and 7-year auditability.

## Key Elements
*   **Cardholder / End Customer & Fraud Operations Analyst**: External users interacting via payment gateways and the case management UI.
*   **AWS ALB**: Entry point routing traffic to containerized services.
*   **Scoring Container & Case Management Container**: AWS ECS Fargate containers processing real-time fraud scores and analyst reviews.
*   **Amazon Aurora Serverless**: Relational database storing application state and case data.
*   **Amazon S3 with Object Lock**: Storage tier holding immutable, tamper-evident decision logs for 7-year auditability.
*   **AWS KMS**: Provides Customer-Managed Keys (CMKs) and Multi-Region Keys (MRKs) for encryption at rest.
*   **AWS IAM Identity Center**: Manages user authentication and role-based access.

## Relationships
*   **Client to AWS ALB**: HTTPS via TLS 1.3 for incoming authorization requests and analyst traffic.
*   **AWS ALB to ECS Fargate Containers**: Internal VPC routing for scoring and case management workloads.
*   **ECS Fargate to Amazon Aurora & S3**: TLS-secured database and object storage queries.
*   **ECS Fargate to AWS KMS**: API calls protected by envelope encryption and VPC endpoints for cryptographic operations.

## Technology Stack
*   **AWS ECS Fargate**: Serverless container orchestration to maintain a fixed infrastructure budget under 25,000 EUR/month.
*   **AWS KMS with Multi-Region Keys**: Ensures cryptographic availability and compliance across regions.
*   **Amazon S3 Object Lock**: Provides write-once-read-many (WORM) storage to satisfy 7-year tamper-evident audit requirements.
*   **Envelope Encryption**: Caches data-encryption keys locally in memory to maintain P99 decision latency below 50 ms.

## Rationale
This architecture uses serverless and managed AWS services to keep operational overhead minimal for a three-engineer team within a fixed budget. Envelope encryption and Multi-Region Keys ensure strict PCI-DSS Level 1 security and high availability without compromising the sub-50ms performance requirement.