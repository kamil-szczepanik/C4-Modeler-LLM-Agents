## Overview
Real-Time Payment Fraud Screening screens card-not-present payment authorizations for fraud and manages case reviews for suspicious transactions. The system ensures PCI-DSS Level 1 compliance, sub-50ms P99 decision latency, and 7-year auditability on AWS.

## Key Elements
*   **Payment Gateway**: External system submitting payment authorizations.
*   **Tokenization / Vault Service**: External system handling card data encryption and tokenization.
*   **AWS Application Load Balancer (ALB)**: Entry point routing incoming payment requests.
*   **Scoring Engine Container**: Go / Rust application running on AWS ECS Fargate for real-time risk scoring.
*   **Case Management & Reporting Container**: Node.js application on AWS ECS Fargate for analyst case reviews.
*   **Amazon ElastiCache Redis**: In-memory data store for real-time rules and feature caching.
*   **Amazon S3 Object Lock**: Tamper-evident storage for 7-year audit logs and compliance data.
*   **Amazon Athena**: Query service for analyzing audit logs in S3.
*   **AWS CloudWatch & PagerDuty**: Monitoring, composite alarms, log exports, and on-call alerting.

## Relationships
*   **Payment Gateway to AWS ALB**: Forwards authorization requests via HTTPS REST API.
*   **AWS ALB to Scoring Engine Container**: Routes payment screening requests via HTTP/2 and gRPC.
*   **Scoring Engine Container to Amazon ElastiCache Redis**: Fetches rules and caches features via RESP (Redis Serialization Protocol).
*   **Scoring Engine Container to Tokenization / Vault Service**: Resolves card tokens via HTTPS REST API.
*   **Containers to Amazon S3 Object Lock**: Exports audit logs and compliance data via internal AWS S3 APIs.
*   **AWS CloudWatch to PagerDuty**: Publishes infrastructure alarms and health status via Amazon SNS and HTTPS webhooks.

## Technology Stack
*   **AWS ECS Fargate**: Serverless container orchestration to minimize infrastructure management for a 3-engineer team.
*   **Go / Rust**: High-performance languages for the Scoring Engine to guarantee <50ms P99 latency.
*   **Node.js**: Rapid development framework for the Case Management container.
*   **Amazon ElastiCache Redis**: Low-latency in-memory data store for rule evaluation.
*   **Amazon S3 Object Lock**: Immutable object storage ensuring tamper-evident 7-year audit retention.
*   **AWS CloudWatch & PagerDuty**: Integrated monitoring and automated alerting to meet strict availability SLAs within budget.

## Rationale
The serverless and managed AWS architecture minimizes operational overhead for a three-engineer team while easily scaling to meet high throughput demands. Strict cost controls and managed services ensure compliance with the 25,000 EUR monthly budget and PCI-DSS Level 1 mandates.