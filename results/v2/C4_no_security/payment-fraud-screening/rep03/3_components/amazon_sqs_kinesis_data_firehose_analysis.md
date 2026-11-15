## Overview
[A real-time payment fraud screening system that evaluates card-not-present transactions for a mid-size payment processor. It provides sub-50ms authorization decisions while maintaining secure case management for fraud analysts.]

## Key Elements
- **AWS Application Load Balancer (ALB)**: Ingress routing for external payment and analyst traffic
- **Scoring Engine Container**: Go / Rust application running on AWS ECS Fargate for low-latency fraud evaluation
- **Case Management Container**: Node.js application running on AWS ECS Fargate for analyst review workflows
- **Amazon ElastiCache Redis**: In-memory data store for fast rule and profile lookups
- **Amazon SQS Standard Queue**: Asynchronous decoupling buffer for audit and transaction events
- **Amazon Kinesis Data Firehose**: Streaming delivery service for batching and routing audit payloads
- **Amazon S3 Object Lock**: Tamper-evident, WORM-compliant storage for 7-year audit retention
- **Amazon Athena**: Serverless query engine for analyzing audit and transaction records
- **AWS CloudWatch & PagerDuty**: Centralized logging, metrics, and incident alerting

## Relationships
- **Payment Gateway -> AWS ALB**: Forwards credit card authorization requests [HTTPS / REST]
- **AWS ALB -> Scoring Engine Container**: Routes real-time authorization traffic [HTTP / gRPC]
- **Scoring Engine Container -> Amazon ElastiCache Redis**: Queries tokenized user profiles and rules [RESP / TCP]
- **Scoring Engine Container -> Amazon SQS Standard Queue**: Streams asynchronous audit payloads [AWS SDK / HTTPS]
- **Amazon SQS Standard Queue -> Amazon Kinesis Data Firehose**: Batches and forwards event streams [AWS Internal API / HTTPS]
- **Amazon Kinesis Data Firehose -> Amazon S3 Object Lock**: Persists compressed audit records [AWS API / HTTPS]
- **Fraud Analyst -> AWS ALB**: Accesses case management UI [HTTPS]

## Technology Stack
- **Compute**: AWS ECS Fargate for serverless container execution with minimal operational overhead
- **Languages**: Go and Rust for the high-performance Scoring Engine; Node.js for Case Management
- **Buffering & Streaming**: Amazon SQS and Amazon Kinesis Data Firehose for reliable, asynchronous event delivery
- **Storage**: Amazon S3 Object Lock for immutable 7-year compliance storage; Amazon ElastiCache Redis for ultra-low latency caching
- **Analytics & Observability**: Amazon Athena for compliance auditing; AWS CloudWatch and PagerDuty for monitoring and incident response

## Rationale
[This architecture uses serverless containers and managed AWS services to meet strict PCI-DSS Level 1 and 7-year audit requirements within a 25,000 EUR monthly budget. Decoupling real-time scoring from asynchronous logging via SQS and Firehose ensures P99 latency remains below 50ms while supporting a 3-person engineering team.]