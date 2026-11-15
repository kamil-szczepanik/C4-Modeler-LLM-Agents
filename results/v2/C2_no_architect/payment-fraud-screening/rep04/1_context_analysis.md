## Overview
The Real-Time Payment Fraud Screening system evaluates card-not-present payment authorizations for fraud, providing sub-50ms decisions and case management for analysts. It ensures PCI-DSS Level 1 compliance, 7-year tamper-evident auditability, and zero-downtime model updates within a 25k EUR monthly AWS budget.

## Key Elements
*   **Payment Gateway / Shoppers:** External systems and end-users sending transaction authorizations.
*   **Fraud Analysts & Risk Managers:** Human actors reviewing suspicious payments and managing rules.
*   **API Gateway & Ingestion Layer:** Handles incoming traffic using TLS 1.3 and mTLS.
*   **Scoring Service:** Evaluates transactions against fraud rules and ML models.
*   **Case Management UI:** Interface for analysts to review flagged transactions without raw PAN access.
*   **Audit & Storage Layer:** Amazon S3 Object Lock with WORM compliance for 7-year retention.

## Relationships
*   **Payment Gateway to API Gateway:** Sends authorization requests via REST API over TLS 1.3.
*   **Scoring Service to Amazon DynamoDB:** Retrieves lookup data and records decision metadata via AWS SDK.
*   **Fraud Analysts to Case Management UI:** Accesses case queues via HTTPS with strict RBAC enforcement.
*   **Scoring Service to S3 Object Lock:** Writes tamper-evident audit logs using AWS KMS encryption.

## Technology Stack
*   **AWS ECS Fargate / AWS Lambda:** Chosen for serverless container orchestration to maintain a lean infrastructure footprint and fit the 3-engineer team capacity.
*   **Amazon DynamoDB:** Provides low-latency key-value data access to meet the P99 < 50ms latency requirement.
*   **Amazon S3 Object Lock & Glacier:** Enforces 7-year WORM compliance while optimizing storage costs to stay within the 25k EUR budget.
*   **AWS SageMaker Serverless:** Runs pre-trained ML models without managing distributed training clusters.

## Rationale
This architecture uses managed AWS services to deliver high throughput and sub-50ms latency while keeping operational overhead low enough for a three-engineer team. Strict data minimization and WORM storage ensure PCI-DSS Level 1 compliance and 7-year auditability within the fixed budget.