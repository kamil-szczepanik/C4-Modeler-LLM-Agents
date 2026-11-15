## Overview
The system provides real-time payment fraud screening and case management for card-not-present transactions. It ensures sub-50ms authorization decisions while maintaining PCI-DSS Level 1 compliance and a 7-year audit trail.

## Key Elements
* Fraud Analysts
* Payment Gateway
* API Gateway / Payment Gateway Integration Container (AWS ECS / Fargate)
* Tokenization/Masking Proxy Container (AWS ECS / Fargate)
* Real-Time Scoring Engine Container (AWS ECS / Fargate)
* Case Management Container (AWS ECS / Fargate)
* Model & Rule Registry Service Container (AWS ECS / Fargate)
* Audit & Compliance Container (AWS ECS / Fargate)
* Amazon ElastiCache (Redis)
* Amazon Aurora
* Amazon SQS / SNS
* Amazon S3 Object Lock / Amazon S3 Glacier Flexible Retrieval

## Relationships
* Payment Gateway -> API Gateway / Payment Gateway Integration Container: Forwards payment authorizations [HTTPS/TLS 1.3, OpenAPI / AsyncAPI]
* API Gateway Integration Container -> Tokenization/Masking Proxy Container: Tokenizes card data [Internal API]
* API Gateway Integration Container -> Real-Time Scoring Engine Container: Requests transaction fraud score [gRPC / REST]
* Real-Time Scoring Engine Container -> Case Management Container: Routes suspicious transactions for review [Internal API]
* Model & Rule Registry Service Container -> Real-Time Scoring Engine Container: Broadcasts immutable models and rules [Amazon SNS/SQS, Internal API]
* Model & Rule Registry Service Container -> Case Management Container: Broadcasts rules and models [Amazon SNS/SQS, Internal API]
* Audit & Compliance Container -> Amazon S3 Object Lock: Stores tamper-evident decision logs [AWS SDK]

## Technology Stack
* AWS ECS with Fargate: Runs containerized services with minimal operational overhead
* Amazon Aurora: Stores relational metadata and append-only audit logs with IAM authentication
* Amazon S3 with Object Lock: Implements content-addressable storage (SHA-256) for immutable models, backed by S3 Glacier Flexible Retrieval for 7-year retention
* Amazon SNS / SQS: Powers asynchronous push-based model distribution to scoring engines
* AWS X-Ray & Structured JSON Logging: Provides distributed tracing and correlation IDs for auditability

## Rationale
This architecture uses serverless container infrastructure on AWS to meet a strict 25,000 EUR monthly budget while supporting a three-engineer team. Content-addressable storage combined with SNS/SQS push updates guarantees zero-downtime model deployments without risking the sub-50ms latency SLA.