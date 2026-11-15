## Overview
- The Real-Time Payment Fraud Screening system evaluates card-not-present payment authorizations for fraud to approve, decline, or flag them.
- It provides case management for fraud analysts while maintaining PCI-DSS Level 1 compliance and 7-year auditability.

## Key Elements
- Model Registry Component (Amazon S3 with Object Lock in Compliance Mode)
- Model Metadata Store (Amazon DynamoDB)
- Model Validation Function (AWS Lambda)
- Model Sync Agent (Background thread within Scoring Engine)
- Security & Secrets (AWS Secrets Manager & AWS KMS Customer Managed Keys)

## Relationships
- Model Validation Function -> Model Registry: Validates and stores binaries [HTTPS via AWS PrivateLink]
- Model Validation Function -> Model Metadata Store: Updates deployment state [HTTPS via AWS PrivateLink]
- Model Sync Agent -> Model Metadata Store: Polls active model pointers [HTTPS via AWS PrivateLink]
- Model Sync Agent -> Model Registry: Fetches immutable model binaries into local memory [HTTPS via VPC Gateway Endpoints]

## Technology Stack
- Amazon S3 with Object Lock: Ensures write-once immutability for 7-year audit compliance (R-06)
- Amazon DynamoDB: Maintains atomic state tracking for zero-downtime model promotion (R-03)
- AWS Lambda: Automates schema validation and baseline checks without infrastructure bloat
- AWS KMS: Encrypts model artifacts and metadata with strict IAM role bindings

## Rationale
- This architecture maintains sub-50ms P99 latency by utilizing local in-memory caching populated by the Model Sync Agent, avoiding runtime retrieval overhead. It preserves lean operations for a three-engineer team within a 25,000 EUR monthly budget.