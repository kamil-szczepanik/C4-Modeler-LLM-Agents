## Overview
This system provides real-time fraud screening for card-not-present payment authorizations and case management for fraud analysts. It ensures sub-50ms latency, PCI-DSS Level 1 compliance, and 7-year tamper-evident auditability within a fixed 25,000 EUR/month budget.

## Key Elements
- API Gateway (AWS API Gateway REST)
- Network Load Balancer (AWS Network Load Balancer with TLS Termination and Health Check components)
- Fraud Scoring Engine (Go, Amazon ECS on EC2 c6i)
- Case Management Backend (Node.js / TypeScript, Amazon ECS Fargate)
- Fraud Analyst UI (React SPA, Amazon S3, Amazon CloudFront)
- Feature/Rule Store & Hot Case Data (Amazon DynamoDB)
- Audit Log Store (Amazon Aurora PostgreSQL with ledger tables)
- Analytics Store (Amazon S3 with Athena)
- Identity & Security Service (AWS Cognito, AWS Secrets Manager, AWS KMS, AWS Certificate Manager Private CA)
- Observability Service (Amazon CloudWatch, AWS X-Ray, AWS Container Insights)

## Relationships
- API Gateway -> Network Load Balancer: Routes incoming requests via `mTLS` (port 443)
- Network Load Balancer -> Fraud Scoring Engine: Forwards traffic via internal `TLS` (port 8443) with connection pooling
- Fraud Scoring Engine -> Feature/Rule Store: Fetches scoring rules and features via `HTTPS/TCP`
- Case Management Backend -> Audit Log Store: Persists immutable decisions via `PostgreSQL Protocol`
- Fraud Analyst UI -> API Gateway: Communicates case reviews via `HTTPS`

## Technology Stack
- AWS Network Load Balancer (NLB): Handles Layer 4/7 edge routing with TLS 1.3/1.2 ciphers and disabled cross-AZ transfer to control costs.
- Amazon ECS on EC2 (c6i): Hosts the Fraud Scoring Engine to guarantee sub-50ms P99 latency at 3,000 TPS.
- Amazon Aurora PostgreSQL: Uses ledger tables to satisfy the 7-year tamper-evident audit requirement.
- AWS Certificate Manager (ACM): Automates Private CA certificate lifecycles to reduce operational overhead for the 3-engineer team.

## Rationale
The architecture leverages managed AWS services to minimize operational burden for a three-engineer team while meeting strict PCI-DSS Level 1 security and performance constraints. Cost-optimized routing and containerized components ensure high availability and sub-50ms latency within the 25,000 EUR/month budget.