## Overview
The Real-Time Payment Fraud Screening system screens card-not-present payment authorizations for fraud under 50 milliseconds while providing case management tools for fraud analysts. It ensures PCI-DSS compliance, 7-year tamper-evident auditability, and 99.99% availability within a strict monthly infrastructure budget.

## Key Elements
* AWS API Gateway / ALB
* Real-Time Scoring Engine (Go, AWS ECS Fargate)
  * API Handler Component (Go net/http)
  * Feature Aggregator Component
  * In-Memory Scoring Engine Component (with WASM models and Explainability Formatter)
  * Audit Publisher Component
  * Circuit Breaker Fallback Controller
* Case Management Backend (Node.js, TypeScript, AWS ECS Fargate)
* Case Management UI (React, Amazon S3, Amazon CloudFront)
* Redis Cache (Amazon ElastiCache (Redis) with TLS 1.3)
* Audit Storage (Amazon S3 with KMS envelope encryption and Object Lock)
* Messaging Bus (Amazon SQS / EventBridge)

## Relationships
* AWS API Gateway / ALB -> Real-Time Scoring Engine: Forwards authorization requests using mTLS with a local circuit breaker [mTLS]
* Real-Time Scoring Engine -> Redis Cache: Performs sub-millisecond feature lookups [Redis Protocol over TLS 1.3]
* Real-Time Scoring Engine -> Messaging Bus: Streams tamper-evident logs and telemetry [Amazon SQS / AMQP]
* Audit Publisher -> Audit Storage: Writes cryptographically signed, encrypted decision logs [AWS SDK / HTTPS]
* Case Management Backend -> PostgreSQL Database: Manages review cases and analyst workflows [PostgreSQL Protocol]

## Technology Stack
* Go: Selected for the Real-Time Scoring Engine to guarantee P99 latency below 50 ms at 3,000 TPS with minimal garbage collection overhead.
* AWS ECS Fargate: Provides container orchestration without the operational toil of bare EC2 and avoids cold-start latency risks of serverless functions.
* Amazon ElastiCache (Redis): Delivers sub-millisecond feature caching for real-time behavioral profiling.
* Amazon S3 with Object Lock and KMS: Ensures tamper-evident, encrypted 7-year audit storage compliant with R-06.
* React & Node.js (TypeScript): Powers the Case Management UI and Backend for efficient analyst case review workflows.

## Rationale
This architecture leverages containerized Go microservices on AWS ECS Fargate to strictly satisfy the sub-50ms P99 latency and high-throughput requirements within a 3-engineer team constraint. Security and compliance controls—such as tokenized payload stripping, local cryptographic signing, and S3 Object Lock—ensure PCI-DSS Level 1 compliance and 7-year auditability while staying safely within the 25,000 EUR monthly budget.