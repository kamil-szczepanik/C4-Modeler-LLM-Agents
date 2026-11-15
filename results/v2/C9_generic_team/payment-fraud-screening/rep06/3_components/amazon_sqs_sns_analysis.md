## Overview
This system provides real-time fraud screening for card-not-present payment authorizations within a strict PCI-DSS Level 1 compliant financial framework. It evaluates transactions under strict latency constraints while maintaining a secure, immutable audit trail.

## Key Elements
- Fraud Analysts
- Payment Gateway
- API Gateway / Payment Gateway Integration Container (AWS ECS with Fargate)
- Tokenization/Masking Proxy Container (AWS ECS with Fargate)
- Real-Time Scoring Engine Container (AWS ECS with Fargate)
- Case Management Container (AWS ECS with Fargate)
- Model & Rule Registry Service Container (AWS ECS with Fargate)
- Audit & Compliance Container (AWS ECS with Fargate)
- Amazon SQS / SNS
- Amazon ElastiCache (Redis)
- Amazon Aurora
- Amazon S3 Object Lock

## Relationships
- Payment Gateway -> API Gateway / Payment Gateway Integration Container: Forwards authorization requests via HTTPS/TLS 1.3
- API Gateway / Payment Gateway Integration Container -> Tokenization/Masking Proxy Container: Sends raw card data for tokenization via gRPC/REST
- Tokenization/Masking Proxy Container -> Real-Time Scoring Engine Container: Passes tokenized payloads for fraud evaluation via gRPC/REST
- Real-Time Scoring Engine Container -> Amazon SQS / SNS: Publishes scoring decisions asynchronously using AWS SDK
- Amazon SQS / SNS -> Audit & Compliance Container: Supplies decoupled audit messages via SQS Consumer
- Fraud Analysts -> Case Management Container: Reviews flagged transactions via HTTPS/TLS 1.3

## Technology Stack
- AWS ECS with Fargate: Runs containerized services ensuring container isolation and elastic scalability without managing underlying servers.
- Amazon SQS / SNS: Decouples the asynchronous audit trail from the synchronous payment path using FIFO queues, DLQs, and KMS encryption.
- Amazon S3 Object Lock: Provides immutable, tamper-evident long-term storage to satisfy the 7-year audit retention requirement.
- Amazon Aurora: Relational database for transactional data storage and case management persistence.
- Amazon ElastiCache (Redis): In-memory data store for low-latency rule caching and rate limiting.

## Rationale
The architecture combines event-driven asynchronous messaging with high-performance containerized services to guarantee P99 decision latency under 50 ms. Leveraging managed AWS services minimizes operational overhead, allowing a three-engineer team to maintain PCI-DSS compliance within budget.