## Overview
- Real-time payment fraud screening system for a mid-size payment processor.
- Screens card-not-present transactions and provides case management for fraud analysts.

## Key Elements
- Fraud Analyst & Risk / Compliance Officer
- Case Management & Reporting Frontend (React SPA, Amazon CloudFront, Amazon S3)
- Case Management & Reporting Backend (Python FastAPI)
- Fraud Screening Engine (Go/Rust, Amazon ECS on EC2)
- Supporting Infrastructure (AWS API Gateway, Amazon ElastiCache for Redis, AWS S3 Object Lock, Amazon Athena, AWS Secrets Manager, Amazon ECR)

## Relationships
- Fraud Analyst / Risk Officer -> Case Management & Reporting Frontend: User interactions [HTTPS]
- Case Management & Reporting Frontend -> Case Management & Reporting Backend: REST/JSON API calls [HTTPS/REST]
- Case Management & Reporting Backend -> Amazon ElastiCache for Redis: Caching & state management [RESP]
- Fraud Screening Engine -> AWS S3 Object Lock: Tamper-evident audit storage [HTTPS/S3 API]

## Technology Stack
- AWS: Target cloud provider in eu-west-1 for regional compliance.
- Go/Rust: Used for the Fraud Screening Engine to achieve P99 latency below 50 ms.
- Python FastAPI: Backend framework for case management APIs.
- React SPA: Frontend UI hosted on Amazon S3 and delivered via Amazon CloudFront with strict CSP and Subresource Integrity.
- Amazon S3 Object Lock: Provides tamper-evident storage for 7-year audit retention.

## Rationale
- Meets PCI-DSS Level 1 compliance and a 7-year audit requirement using encrypted, immutable storage.
- Operates within a €25,000 monthly budget and supports maintenance by a 3-engineer team.