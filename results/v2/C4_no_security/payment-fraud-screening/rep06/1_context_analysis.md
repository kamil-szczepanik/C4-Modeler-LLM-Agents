## Overview
The Real-Time Payment Fraud Screening system evaluates card-not-present payment authorizations to detect fraud and provides case management tools for analysts. It processes 3,000 transactions per second for a mid-size payment processor in AWS eu-west-1.

## Key Elements
* Shopper / Cardholder and Merchant / Payment Gateway (External entities)
* Fraud Analyst (Internal user)
* API Gateway / Load Balancer (AWS ALB)
* Fraud Scoring Service (AWS ECS Fargate containers)
* Case Management UI & Service (AWS ECS Fargate containers)
* In-Memory Feature Cache & Model Store (AWS ElastiCache Redis)
* Audit Pipeline (Amazon Kinesis Data Streams and AWS S3 with Object Lock)
* Identity and Access Management (AWS Cognito)

## Relationships
* Merchants connect to API Gateway via gRPC/TLS for real-time scoring.
* Fraud Analysts access Case Management UI via HTTPS/TLS authenticated by AWS Cognito.
* Fraud Scoring Service queries local in-memory features and AWS ElastiCache Redis over TCP.
* Fraud Scoring Service publishes audit events asynchronously to Amazon Kinesis.
* Amazon Kinesis persists audit logs to AWS S3 Object Lock.

## Technology Stack
* AWS ECS Fargate: Container orchestration chosen for blue/green zero-downtime deployments without operational overhead.
* AWS ElastiCache Redis: Low-latency caching for real-time feature lookup meeting <50ms P99 SLA.
* Amazon Kinesis & S3: Asynchronous decoupling for tamper-evident 7-year audit retention within budget.
* AWS Cognito: Managed authentication supporting PCI-DSS Level 1 compliance.

## Rationale
This architecture uses managed AWS services to remain maintainable by a three-engineer team within a 25,000 EUR monthly budget. Asynchronous logging and local caching isolate critical scoring paths to reliably achieve sub-50ms latency at 3,000 TPS.