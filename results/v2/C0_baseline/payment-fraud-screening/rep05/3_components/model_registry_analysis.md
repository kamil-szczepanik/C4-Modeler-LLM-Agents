## Overview
[The system is a real-time payment fraud screening platform that evaluates card-not-present authorizations against compliance and performance SLAs. It ensures secure case management, tamper-evident audit trails, and zero-downtime fraud model updates.]

## Key Elements
- Data Scientist / ML Engineer
- Risk / Compliance Officer
- Real-Time Scoring Engine
- Case Management App
- Amazon SageMaker Model Registry
- Model Governance API
- Artifact Cryptographic Signer (AWS Lambda)
- Model Event Dispatcher (Amazon SNS)
- Amazon S3 with Object Lock

## Relationships
- Data Scientist registers models via Model Governance API using HTTPS.
- Risk Officer approves models in Amazon SageMaker Model Registry via IAM/ABAC.
- Model Governance API triggers Amazon EventBridge on state transition.
- Artifact Cryptographic Signer uses AWS KMS to sign artifacts stored in Amazon S3.
- Model Event Dispatcher notifies Real-Time Scoring Engine via authenticated HTTPS.

## Technology Stack
- Amazon SageMaker Model Registry: Managed service for model lifecycle management within a 3-engineer team constraint.
- AWS Lambda & KMS: Serverless compute and key management for automated cryptographic artifact signing.
- Amazon S3 with Object Lock: Secure storage enforcing 7-year tamper-evident retention.
- Amazon EventBridge & SNS: Event-driven pub/sub messaging for zero-downtime model distribution.

## Rationale
[This architecture meets strict PCI-DSS Level 1 compliance and 7-year audit requirements using managed AWS services. It stays within the €25k monthly budget and operational capacity of a three-engineer team.]