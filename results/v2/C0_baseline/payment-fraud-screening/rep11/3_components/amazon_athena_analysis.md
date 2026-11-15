## Overview
[Real-Time Payment Fraud Screening System processes card-not-present payment authorizations under 50 ms using AWS infrastructure to screen for fraud and manage analyst reviews.]

## Key Elements
* Fraud Analyst & Risk/Compliance Officer
* Amazon API Gateway / Ingress
* Fraud Screening Engine (Go/Rust on Amazon ECS on EC2)
* Case Management & Reporting Frontend (React SPA on CloudFront / S3)
* Case Management & Reporting Backend (Python FastAPI)
* Amazon ElastiCache for Redis
* Amazon Athena (Query Engine, AWS Glue Data Catalog, S3 Query Result Cache, Saved Queries & Templates)
* AWS S3 Object Lock & AWS KMS
* AWS Lake Formation & AWS Secrets Manager

## Relationships
* Case Management & Reporting Backend -> Amazon Athena: Queries historical audit logs for compliance using [HTTPS / Athena API / AWS SDK]
* Fraud Screening Engine -> Amazon ElastiCache for Redis: Fetches fraud rules and velocity counters using [Redis TCP Protocol]
* Case Management & Reporting Frontend -> Amazon API Gateway / Ingress: Routes user actions via [HTTPS / TLS 1.3]

## Technology Stack
* AWS: Target cloud provider in eu-west-1 meeting PCI-DSS Level 1 constraints
* Python FastAPI & Go/Rust: Backend services for rapid case management and low-latency fraud scoring
* Amazon Athena & AWS Glue: Serverless analytics and data catalog for 7-year audit queries within budget
* AWS S3 Object Lock & AWS KMS: Tamper-evident storage and encryption for strict auditability

## Rationale
[This serverless and containerized AWS architecture guarantees sub-50ms fraud scoring performance while strictly enforcing PCI-DSS Level 1 compliance and a 25,000 EUR monthly budget. It scales efficiently to support a three-person engineering team through automated infrastructure provisioning and managed services.]