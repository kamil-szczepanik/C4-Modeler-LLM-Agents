## Overview
Real-time payment fraud screening engine for card-not-present transactions on AWS. Screens payment authorizations in under 50ms while maintaining PCI-DSS Level 1 compliance.

## Key Elements
* Fraud Analysts and Risk Managers
* Real-Time Scoring Engine (Go microservice on AWS ECS EC2)
* API Handler Component, Feature Evaluator Component, Rules Engine Core, Audit Logger Component, Shadow Evaluator Component, and Model Registry Loader
* Amazon API Gateway, Amazon DynamoDB, Amazon S3, Amazon SQS / Amazon Kinesis, AWS KMS, AWS Secrets Manager, and Amazon CloudWatch

## Relationships
* Amazon API Gateway -> API Handler Component: Forwards payment transactions [Internal gRPC over mTLS]
* Feature Evaluator Component -> Amazon DynamoDB: Performs feature lookups [AWS SDK over TLS 1.3]
* Audit Logger Component -> Amazon SQS / Kinesis: Publishes signed decision payloads [AWS SDK over TLS 1.3]
* Model Registry Loader -> Amazon S3: Polls for Wasm models [AWS SDK over TLS 1.3]
* Real-Time Scoring Engine -> AWS KMS & Secrets Manager: Requests keys and credentials [AWS SDK over TLS 1.3]
* Real-Time Scoring Engine -> Amazon CloudWatch: Sends metrics and logs [AWS SDK over TLS 1.3]

## Technology Stack
* Go (Gin/Goroutines): Chosen for high concurrency and low memory overhead to meet sub-50ms latency at 3,000 TPS.
* WebAssembly (Wasm): Enables secure sandboxing and hot-reloading of scoring models without downtime.
* Amazon DynamoDB: Provides single-digit millisecond feature lookups within budget constraints.
* AWS KMS: Ensures strict encryption, key rotation, and HMAC-SHA256 tamper-evident signing for audit compliance.

## Rationale
This architecture leverages asynchronous Go goroutines and zero-copy in-memory communication to achieve sub-50ms latency at 3,000 TPS. AWS managed services and secure Wasm sandboxing satisfy PCI-DSS compliance, 7-year auditability, and zero-downtime updates within the 25,000 EUR monthly budget for a 3-engineer team.