## Overview
[The Real-Time Payment Fraud Screening system evaluates card-not-present payment authorizations for fraud within strict latency constraints, providing case management tools for fraud analysts. It operates on AWS to meet PCI-DSS Level 1 compliance while maintaining a fixed infrastructure budget.]

## Key Elements
- [API Gateway / Tokenization Proxy (Envoy / AWS API Gateway)]
- [Real-Time Scoring Engine (Go / AWS ECS on Fargate, Redis)]
- [Rule & Model Distribution Service (Python / FastAPI + S3)]
- [Event Broker (AWS MSK / Managed Kafka)]
- [Fraud Analyst]

## Relationships
- [API Gateway / Tokenization Proxy -> Real-Time Scoring Engine: Routes requests for scoring using gRPC over AWS VPC private subnets with mTLS]
- [Real-Time Scoring Engine <-> Redis Cluster: Fetches sliding-window velocity counters using Redis RESP protocol over TLS]
- [Real-Time Scoring Engine -> Event Broker (AWS MSK): Publishes cryptographically signed scoring events using Kafka protocol over TLS with SASL/IAM]
- [Rule & Model Distribution Service -> Real-Time Scoring Engine: Delivers rules and models via S3 with cryptographic verification]

## Technology Stack
- [Go: Powers the Real-Time Scoring Engine for ultra-low latency and zero-allocation parsing]
- [AWS ECS on Fargate: Runs containerized services with auto-scaling to satisfy performance and budget constraints]
- [Redis Cluster: Provides high-throughput, in-memory state management for velocity checks]
- [AWS MSK (Managed Kafka): Handles asynchronous event streaming for audit logs and telemetry]
- [AWS S3 & KMS: Stores encrypted models and rules with cryptographic signature verification]

## Rationale
[This architecture utilizes Go on AWS Fargate with Redis to achieve sub-50ms P99 latency at 3,000 TPS within a strict 25,000 EUR monthly budget. Security and auditability requirements (PCI-DSS Level 1, cryptographic signing) are met through mTLS, IAM policies, and tamper-evident event logging.]