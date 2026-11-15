## Overview
This system provides real-time payment fraud screening for card-not-present authorizations, returning approve, decline, or review decisions. It features case management for analysts, strict PCI-DSS Level 1 compliance, and 7-year tamper-evident auditability within a fixed AWS budget.

## Key Elements
- **Payers & Fraud Analysts**: End users submitting payments and reviewing flagged transactions.
- **AWS API Gateway / ALB**: Ingress routing and load balancing.
- **Real-Time Scoring Engine**: Go/Rust container on Amazon EC2 evaluating fraud rules.
- **Case Management Backend & UI**: Node.js/TypeScript on AWS ECS Fargate and React on S3/CloudFront.
- **Audit Storage**: Amazon S3 with KMS and Object Lock, backed by Amazon DynamoDB indexing.
- **Audit Sub-Components**: Audit Writer, Audit Query API, and Report Generator (Go, AWS Lambda).

## Relationships
- Payers -> AWS API Gateway / ALB: Submits authorization requests [HTTPS]
- Real-Time Scoring Engine -> Redis Cache: Retrieves rules and customer velocity data [Redis Protocol]
- Audit Writer -> Amazon S3: Persists immutable decision records [HTTPS / AWS SDK]
- Audit Query API -> Amazon DynamoDB: Queries indexed decision metadata [HTTPS]
- Report Generator -> Amazon S3 (Staging): Generates signed export packages [HTTPS / AWS SDK]

## Technology Stack
- **Compute**: Amazon EC2 (Scoring), AWS ECS Fargate (Case Management), AWS Lambda (Audit/Export APIs) for serverless scalability.
- **Storage/Database**: Amazon RDS (PostgreSQL) for transactional data, Amazon ElastiCache (Redis) for fast caching, Amazon S3 with KMS/Object Lock for immutable 7-year audit logs.
- **Infrastructure as Code**: Terraform / AWS CDK managed by a 3-engineer team within a 25,000 EUR/month budget.

## Rationale
The architecture combines low-latency EC2 scoring nodes with serverless AWS Lambda components to meet P99 performance targets under 50 ms. Leveraging managed AWS services (S3 Object Lock, DynamoDB, KMS) ensures PCI-DSS compliance and tamper-evident 7-year auditability while minimizing operational overhead for a three-engineer team.