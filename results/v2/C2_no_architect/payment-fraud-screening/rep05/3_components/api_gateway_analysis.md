## Overview
The Real-Time Payment Fraud Screening system evaluates card-not-present payment authorizations in real-time to prevent fraud while ensuring strict PCI-DSS compliance. It provides low-latency fraud scoring and an analyst case management interface within a fixed budget of €25,000 per month.

## Key Elements
- Payment Gateway (External System)
- Fraud Analyst (Person)
- API Gateway (AWS API Gateway HTTP API with AWS WAF)
- Scoring Engine Container (AWS ECS Fargate)
- Case Management Container (AWS ECS Fargate)
- Cache & Storage (AWS ElastiCache Redis, AWS S3 Glacier with Object Lock, AWS KMS)
- Security & IAM (AWS Cognito, AWS IAM, AWS X-Ray)

## Relationships
- Payment Gateway -> API Gateway: Sends payment authorization requests [HTTPS, mTLS, TLS 1.3]
- API Gateway -> Scoring Engine Container: Routes scoring requests [Internal VPC Networking, AWS VPC Security Groups]
- API Gateway -> Case Management Container: Routes analyst review requests [HTTPS, JWT validation, AWS Cognito]
- Scoring Engine Container -> AWS ElastiCache Redis: Retrieves rule caches and rate-limiting counters [Internal VPC]
- System Containers -> AWS S3 Glacier: Stores tamper-evident audit logs and decisions [AWS KMS, Object Lock]

## Technology Stack
- Ingress: AWS API Gateway (HTTP API) chosen for native auto-scaling and low operational overhead for a 3-engineer team.
- Compute: AWS ECS (Fargate) selected for containerized workloads to eliminate server management.
- Security & Compliance: AWS WAF and AWS KMS chosen for PCI-DSS Level 1 tokenization, rate limiting, and data encryption.
- Caching: AWS ElastiCache (Redis) utilized for distributed rate limiting and low-latency feature lookups.
- Audit & Storage: AWS S3 Glacier with Object Lock configured to meet the 7-year tamper-evident audit requirement.

## Rationale
This architecture uses fully managed AWS serverless and container services to meet strict performance (<50ms P99 latency at 3,000 TPS) and compliance (PCI-DSS Level 1) requirements within a fixed €25,000 monthly budget. Offloading infrastructure management to managed services enables a three-engineer team to operate the platform reliably with zero downtime.