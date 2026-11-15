## Overview
The Real-Time Payment Fraud Screening system screens card-not-present payment authorizations for fraud and manages case reviews. It ensures high-throughput, low-latency decisions while maintaining strict PCI-DSS compliance and 7-year auditability.

## Key Elements
- Fraud Analysts (Users)
- Payment Gateway / Core Ledger, Identity Provider / IdP, Compliance Archive / AWS S3 Object Lock (External Systems)
- API Gateway / Envoy, Fraud Scoring Engine, Case Management Backend, Model & Rule Registry Service, Analyst UI, Asynchronous Audit Worker (Containers)
- Redis Cluster / Amazon ElastiCache, PostgreSQL / Amazon Aurora, Amazon SQS / SNS, AWS Secrets Manager / Parameter Store (Data & Infrastructure Containers)
- Amazon SNS Topic, Amazon SQS Queues, Audit Dead-Line Queue (DLQ) (Components)

## Relationships
- Payment Gateway -> API Gateway / Envoy: Forwards authorization requests [HTTPS / TLS]
- API Gateway / Envoy -> Fraud Scoring Engine: Routes scoring requests [gRPC]
- Fraud Scoring Engine -> Redis Cluster / Amazon ElastiCache: Fetches rule caches and sliding-window velocity counters [Redis TCP protocol]
- Fraud Scoring Engine -> Amazon SNS Topic: Publishes telemetry and audit events [HTTPS]
- Amazon SNS Topic -> Amazon SQS Queues: Delivers fan-out audit events [AWS SNS Subscription / SQS integration]
- Amazon SQS Queues -> Asynchronous Audit Worker: Buffers events for compliance processing [AWS internal polling]
- Amazon SQS Queues -> Audit Dead-Line Queue: Routes poisoned audit events after max receives [AWS internal]

## Technology Stack
- AWS (eu-west-1): Target cloud provider ensuring regional data residency and low latency.
- Go & Java (Spring Boot): Backend languages selected for high-performance concurrent processing and enterprise case management.
- Python & FastAPI: Powers the rule registry service for model updates.
- React, AWS S3, & CloudFront: Delivers a secure, static single-page application for fraud analysts.
- Amazon Aurora (PostgreSQL) & ElastiCache (Redis): Provides relational state storage and ultra-low latency caching.
- Amazon SQS / SNS & AWS KMS (SSE-KMS): Delivers scalable event-driven messaging with robust encryption at rest for PCI-DSS compliance.

## Rationale
This architecture uses decoupled, serverless-leaning AWS services to easily handle 3,000 requests per second under 50 ms while strictly enforcing a €25,000 monthly budget. Automated encryption, immutable storage, and robust queuing guarantee PCI-DSS Level 1 compliance and 7-year tamper-evident auditability for a three-engineer team.