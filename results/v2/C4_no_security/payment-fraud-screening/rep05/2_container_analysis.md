## Overview
The Real-Time Payment Fraud Screening system evaluates card-not-present payment authorizations to detect fraud prior to approval while providing case management tools for fraud analysts. It ensures high availability, strict compliance, and low-latency decision-making under a fixed budget.

## Key Elements
*   Fraud Analysts and Compliance Officers
*   Auditors and Regulators
*   Merchant Risk Managers
*   AWS API Gateway
*   Fraud Scoring Engine (Go/Rust)
*   Case Management & Rules Service (Node.js/Go)
*   Audit & Evidence Worker (Go)
*   AWS ElastiCache (Redis)
*   Amazon SQS
*   AWS S3 with Object Lock

## Relationships
*   Payment Gateway / Merchants interact with AWS API Gateway via HTTPS/JSON.
*   AWS API Gateway communicates with the Fraud Scoring Engine via gRPC.
*   Fraud Scoring Engine queries AWS ElastiCache (Redis) for real-time feature lookups.
*   Fraud Scoring Engine publishes decision events to Amazon SQS.
*   Audit & Evidence Worker consumes from Amazon SQS and writes to AWS S3 with Object Lock.
*   Fraud Analysts and Risk Managers access the Case Management & Rules Service via HTTPS.

## Technology Stack
*   **Compute:** AWS ECS on Fargate for container orchestration.
*   **Languages:** Go or Rust for high-throughput, low-latency scoring; Node.js or Go for case management.
*   **Caching:** AWS ElastiCache (Redis) for sub-millisecond feature retrieval.
*   **Messaging:** Amazon SQS for asynchronous audit logging.
*   **Storage:** AWS S3 with Object Lock for tamper-evident 7-year audit retention.
*   **Networking:** AWS API Gateway for ingress and TLS termination.

## Rationale
This architecture uses pure AWS Fargate and managed services to minimize operational toil for a three-engineer team within a €25k monthly budget. Decoupling the high-throughput scoring engine via gRPC and asynchronous audit logging guarantees sub-50ms P99 latency while satisfying PCI-DSS Level 1 boundaries and strict auditability.