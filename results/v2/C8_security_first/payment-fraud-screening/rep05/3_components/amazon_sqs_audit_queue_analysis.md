## Overview
Real-Time Payment Fraud Screening system evaluates card-not-present payment authorizations for fraud, while providing case management tools for analysts. It ensures sub-50ms P99 decisions at 3,000 TPS within a strict €25,000 monthly budget while maintaining PCI-DSS Level 1 compliance.

## Key Elements
- Fraud Analysts & Risk Managers
- AWS API Gateway & Internal Network Load Balancer (NLB)
- Scoring Engine Container (Rust or Go)
- Case Management API Container (Node.js or Python)
- Fraud Analyst SPA
- S3 Model Registry & S3 Object Lock (AWS S3)
- Amazon SQS (Audit Queue) (`audit-events-queue` and `audit-events-dlq`)
- AWS QLDB
- AWS KMS & Secrets Manager
- AWS Lambda Consumer

## Relationships
- Scoring Engine Container -> `audit-events-queue`: Pushes audit payloads asynchronously [HTTPS / AWS SDK, TLS 1.3 via VPC Endpoint]
- `audit-events-queue` -> AWS Lambda Consumer: Triggers batch ingestion [SQS Event Source Mapping]
- AWS Lambda Consumer -> AWS QLDB: Persists immutable records [QLDB Driver API]
- Scoring Engine Container -> S3 Model Registry: Fetches scoring models [HTTPS / AWS SDK]

## Technology Stack
- AWS (eu-west-1): Target cloud provider for managed scalability and compliance
- Rust or Go: Selected for the Scoring Engine Container to guarantee sub-50ms P99 latency
- Amazon SQS: Cost-effective asynchronous buffering supporting 3,000 TPS within budget
- AWS QLDB & S3 Object Lock: Provides tamper-evident 7-year audit retention (R-06)
- AWS KMS & Secrets Manager: Encrypts card data and audit payloads at rest (CMK)
- Terraform / AWS CDK: Infrastructure as Code for a 3-engineer team

## Rationale
Asynchronous SQS buffering decouples compliance auditing from the critical payment path, ensuring sub-50ms P99 decision latency. Standard AWS managed services minimize operational toil for a three-engineer team while satisfying PCI-DSS Level 1 constraints and the €25,000 budget.