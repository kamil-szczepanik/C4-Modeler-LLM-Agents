## Overview
This system provides real-time fraud screening for card-not-present payment authorizations and case management for fraud analysts. It enforces PCI-DSS Level 1 compliance while maintaining sub-50ms P99 latencies within a fixed infrastructure budget.

## Key Elements
* Fraud Screening Engine (Go/Rust, Amazon ECS on EC2)
* Case Management Backend (Python FastAPI)
* AWS Secrets Manager (AWS Secrets Manager)
* Secrets Retrieval & Caching Library (In-Memory SDK component)
* Rotation Lambda Handler (AWS Lambda, Python)
* AWS EventBridge (AWS EventBridge)
* Audit Archive (AWS S3 Object Lock, AWS KMS)
* Amazon CloudWatch & CloudTrail (AWS CloudWatch, AWS CloudTrail)

## Relationships
* Fraud Screening Engine queries Secrets Retrieval & Caching Library via in-memory calls with a 15-minute TTL.
* Secrets Retrieval & Caching Library connects to AWS Secrets Manager over HTTPS/TLS 1.3 using AWS SDK.
* AWS EventBridge triggers Rotation Lambda Handler to update external credentials.
* Rotation Lambda Handler updates AWS Secrets Manager using AWSCURRENT and AWSPREVIOUS staging labels.
* AWS CloudTrail exports access logs to Audit Archive (AWS S3 Object Lock) over HTTPS.

## Technology Stack
* AWS Secrets Manager: Secures external partner keys, database credentials, and tokenization secrets with IAM ABAC least-privilege.
* AWS Lambda & EventBridge: Automates secret rotation with blue/green deployments to minimize operational overhead for a 3-engineer team.
* AWS KMS: Encrypts secrets at rest using a dedicated Customer Managed Key with automated annual rotation.
* AWS S3 Object Lock: Stores immutable access logs and decisions for the mandatory 7-year audit requirement.

## Rationale
This architecture uses local in-memory secret caching to prevent Secrets Manager API calls from violating the strict 50ms P99 latency threshold. Automated rotation via Lambda and EventBridge keeps operational maintenance minimal for a three-engineer team while satisfying strict PCI-DSS Level 1 audit and security constraints.