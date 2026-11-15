## Overview
The Real-Time Payment Fraud Screening system screens card-not-present payment authorizations in AWS (`eu-west-1`) to prevent fraud while maintaining high availability and strict PCI-DSS compliance. It provides real-time scoring, auditability, and case management for fraud analysts within a fixed budget and small engineering team.

## Key Elements
* **Payment Gateway**: External system initiating payment authorization requests via HTTPS.
* **Tokenization / Vault Service**: External system handling card data encryption and tokenization.
* **AWS ALB**: Ingress layer with circuit breaker logic and AWS X-Ray distributed tracing.
* **Scoring Engine Container**: Go application running on AWS ECS Fargate processing real-time scoring.
* **Case Management & Reporting Container**: Node.js application on AWS ECS Fargate for fraud analysts and risk managers.
* **ElastiCache Redis**: In-memory cache for ultra-low latency rules evaluation and zero-downtime hot-reloads via pub/sub.
* **Amazon SQS / Kinesis Data Firehose**: Buffering service for batching high-throughput audit events.
* **Amazon S3 Object Lock**: WORM-compliant tamper-evident storage for 7-year audit retention.
* **Amazon Athena**: Query engine for analyzing audit logs in S3.
* **AWS CloudWatch & PagerDuty**: Monitoring, composite alarms, and alerting for scoring outages.

## Relationships
* **Payment Gateway to AWS ALB**: Routes authorization requests via HTTPS.
* **AWS ALB to Scoring Engine Container**: Forwards requests using HTTP/gRPC while applying circuit breaker fallback.
* **Scoring Engine Container to Tokenization / Vault Service**: Requests tokenized card references via secure APIs.
* **Scoring Engine Container to ElastiCache Redis**: Fetches cached rules and scoring models in-memory.
* **Scoring Engine Container to Amazon SQS / Kinesis Data Firehose**: Streams transaction inputs, model versions, and explanations asynchronously via HTTP.
* **Amazon SQS / Kinesis Data Firehose to Amazon S3 Object Lock**: Batches and persists tamper-evident audit records.
* **Fraud Analyst to Case Management & Reporting Container**: Reviews suspicious payments and monitors false positive rates via HTTPS UI.
* **Amazon Athena to Amazon S3 Object Lock**: Queries historical audit data for compliance audits.

## Technology Stack
* **Go / Rust**: Powers the Scoring Engine Container for maximum performance and memory efficiency.
* **Node.js**: Powers the Case Management & Reporting Container for rapid feature delivery.
* **AWS ECS Fargate**: Serverless container orchestration minimizing operational overhead for a three-engineer team.
* **ElastiCache Redis**: Delivers sub-millisecond rule lookups to meet the <50ms P99 latency SLA.
* **Amazon S3 Object Lock**: Ensures cost-effective, tamper-evident 7-year auditability meeting regulatory constraints.
* **Amazon SQS / Kinesis Data Firehose**: Prevents S3 throttling by batching 3,000 TPS audit write payloads.

## Rationale
The architecture decouples the high-throughput, stateless Scoring Engine from the Case Management UI to ensure strict PCI-DSS compliance and fault isolation. Using managed serverless AWS services like ECS Fargate, S3, and SQS satisfies strict performance, auditability, and 25,000 EUR monthly budget constraints while remaining operable by a three-engineer team.