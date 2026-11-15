## Overview
Real-Time Payment Fraud Screening system screens card-not-present payment authorizations for fraud before approval and provides case management for suspicious payment reviews. Built for a mid-size payment processor, it meets strict PCI-DSS Level 1 compliance requirements within a fixed budget and small engineering team.

## Key Elements
* Fraud Analyst & Risk/Compliance Officer
* Merchant / Operations Manager & System Integrator (Payment Gateway)
* Real-Time Scoring Engine (Go on Amazon ECS Fargate)
* Case Management App (Node.js/TypeScript on Amazon ECS Fargate)
* Feature Store & Cache (Amazon ElastiCache Redis)
* Database (Amazon Aurora PostgreSQL Serverless v2)
* Messaging & Audit Pipeline (Amazon SQS/SNS and Amazon S3 with Object Lock)
* Model Registry (Amazon SageMaker Model Registry)
* Network & Security (AWS WAF, Amazon API Gateway, Route 53, AWS Secrets Manager, AWS KMS)

## Relationships
* Payment Gateway invokes Real-Time Scoring Engine via HTTPS/REST with mTLS over Amazon API Gateway
* Scoring Engine reads features from Amazon ElastiCache Redis
* Scoring Engine publishes asynchronous events to Amazon SQS
* SQS writes compliance audit logs to Amazon S3 with Object Lock (Compliance Mode) using AWS KMS keys
* Fraud Analysts access Case Management App via HTTPS over Amazon API Gateway
* Case Management App reads/writes relational case data to Amazon Aurora PostgreSQL Serverless v2
* Route 53 and API Gateway provide circuit-breaker fallback mechanisms for R-07 fail-safe requirements

## Technology Stack
* Compute: Amazon ECS on AWS Fargate using Go and Node.js/TypeScript for predictable latency and zero cold starts
* Storage & Caching: Amazon Aurora PostgreSQL Serverless v2 for relational scaling; Amazon ElastiCache (Redis) for sub-millisecond feature lookups
* Compliance & Audit: Amazon S3 with Object Lock and AWS KMS for tamper-evident 7-year audit storage
* Messaging: Amazon SQS/SNS for decoupled, serverless asynchronous processing
* Security & Routing: AWS WAF, API Gateway, AWS Secrets Manager, and Route 53 for mTLS, credential rotation, and fail-safe routing

## Rationale
The serverless-adjacent container architecture maximizes managed AWS services to minimize operational toil for a 3-engineer team while strictly maintaining the 25k EUR monthly budget. Go on ECS Fargate combined with Redis caching guarantees sub-50ms P99 decision latency at 3,000 TPS, while S3 Object Lock and SQS ensure PCI-DSS compliance and tamper-evident auditability.