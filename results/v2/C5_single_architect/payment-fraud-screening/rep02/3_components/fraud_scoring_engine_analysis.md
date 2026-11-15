## Overview
The Real-Time Payment Fraud Screening system screens card-not-present payment authorizations in AWS eu-west-1 for fraud under 50ms P99 latency. It provides real-time scoring and case management for analysts while maintaining PCI-DSS Level 1 compliance and 7-year auditability.

## Key Elements
- Fraud Analyst (User)
- AWS API Gateway / ALB (External System/Load Balancer)
- Fraud Scoring Engine (AWS ECS Fargate Container, Rust)
- API Handler Component (Tonic gRPC framework)
- Scoring Engine Core Component (Native Rust async tasks)
- Feature Aggregator Component (Tokio async I/O with Redis-rs)
- Data Access Component
- Audit Logger Component (AWS SDK for Rust / aws-sdk-sqs)
- Amazon ElastiCache Redis
- Amazon Aurora PostgreSQL
- Amazon S3 Immutable Vault (with Object Lock)
- Amazon SQS / SNS

## Relationships
- AWS API Gateway / ALB -> API Handler Component: Ingests authorization requests [gRPC over HTTP/2]
- API Handler -> Scoring Engine Core: Executes scoring logic [In-memory function call]
- Feature Aggregator -> Amazon ElastiCache Redis: Fetches velocity features [Redis Protocol via TLS]
- Data Access Component -> Amazon Aurora PostgreSQL: Queries reference data [PostgreSQL Wire Protocol]
- Audit Logger Component -> Amazon SQS: Dispatches tamper-evident payloads [AWS SDK / SQS API]

## Technology Stack
- Rust: Chosen for the Fraud Scoring Engine to guarantee predictable low-latency execution without Garbage Collection pauses and fit the 3-engineer team constraint.
- Tonic (gRPC): High-performance gRPC framework for the API Handler to process high throughput efficiently.
- Tokio & Redis-rs: Async runtime and connection pooling for concurrent feature retrieval within the latency budget.
- AWS ECS Fargate: Managed container orchestration matching the fixed 25,000 EUR monthly budget.
- Amazon S3 Object Lock: Ensures tamper-evident audit data storage for 7-year regulatory compliance.

## Rationale
This architecture uses Rust and asynchronous I/O on ECS Fargate to reliably process 3,000 requests per second under 50ms P99 latency. It strictly adheres to PCI-DSS Level 1 compliance, immutable 7-year auditability, and AWS budget constraints while maintaining a manageable footprint for a 3-engineer team.