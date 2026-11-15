## Overview
[The system is a Real-Time Payment Fraud Screening platform that screens card-not-present payment authorizations and manages suspicious fraud cases. It provides sub-50ms fraud decisions, 7-year auditability, and PCI-DSS Level 1 compliance within a 25,000 EUR monthly budget on AWS eu-west-1.]

## Key Elements
* Fraud Analyst & Risk Manager
* Payment Gateway / Acquirer & Merchant Platforms
* Identity Provider (IdP)
* Regulatory & Notification Sink
* API Gateway (AWS API Gateway / ALB)
* Scoring Engine Container (Go/Rust on Amazon ECS)
* Case Management Container (Node.js/Python Monolith on Amazon ECS)
* Data Layer (Amazon DynamoDB & Amazon ElastiCache Redis)
* Event & Compliance Infrastructure (Amazon EventBridge/SNS, Go-based Audit Logger, Compliance Vault S3 Writer with S3 Object Lock, Alerting & Dead-Letter Monitor)
* AWS KMS (Key Management Service)

## Relationships
* Payment Gateway / Acquirer & Merchant Platforms -> API Gateway (AWS API Gateway / ALB): Submits payment authorization requests [HTTPS/JSON]
* API Gateway -> Scoring Engine Container: Routes requests for real-time scoring [gRPC / REST]
* Scoring Engine Container -> Data Layer: Fetches rules, models, and caches states [Redis/DynamoDB protocol]
* Scoring Engine Container -> Case Management Container: Routes suspicious transactions requiring review [HTTPS/JSON]
* Data Layer -> Event & Compliance Infrastructure: Exports tamper-evident audit logs and tracking events [AWS SQS/SNS / AWS CloudTrail]
* Event & Compliance Infrastructure -> Regulatory & Notification Sink: Exports audit logs and failure alerts asynchronously [AWS SQS/SNS events / HTTPS]

## Technology Stack
* Cloud Provider: AWS (eu-west-1) for scalable, compliant infrastructure
* Compute: Amazon ECS (Go/Rust for Scoring, Node.js/Python for Case Management) to meet sub-50ms latency at 3,000 TPS
* Data & Caching: Amazon DynamoDB and Amazon ElastiCache (Redis) for low-latency decision storage and state management
* Event Bus & Messaging: Amazon SQS, Amazon SNS, and Amazon EventBridge for asynchronous decoupling and DLQ backpressure management
* Storage & Compliance: Amazon S3 with Object Lock (Compliance Mode) and S3 Glacier Flexible/Deep Archive for tamper-evident 7-year retention within budget
* Security & Cryptography: AWS KMS with automated key rotation and envelope/asymmetric signing for cryptographic non-repudiation

## Rationale
[This architecture enforces strict PCI-DSS compliance and 7-year tamper-evident auditability using AWS S3 Object Lock and KMS while maintaining a sub-50ms P99 latency at 3,000 TPS. The lean containerized setup on ECS and S3 storage tiering strictly constrain operations to a 3-engineer team and a 25,000 EUR monthly budget.]