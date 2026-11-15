## Overview
Real-Time Payment Fraud Screening screens card-not-present payment authorizations for fraud before approval and manages suspicious payment reviews. It utilizes AWS eu-west-1, AWS ECS Fargate, and Amazon ElastiCache Redis to meet PCI-DSS Level 1 compliance under a 25,000 EUR monthly budget.

## Key Elements
- **Users**: Fraud Analyst, Risk Manager, Compliance Auditor
- **External Systems**: Payment Gateway, Tokenization / Vault Service, AWS CloudWatch, PagerDuty
- **Containers**: AWS ALB, Scoring Engine Container (Go / Rust, AWS ECS Fargate), Case Management & Reporting Container (Node.js, AWS ECS Fargate), ElastiCache Redis (Amazon ElastiCache Redis), Amazon SQS / Kinesis Data Firehose, Amazon S3 Object Lock, Amazon Athena
- **Redis Components**: Redis Engine OSS 7.x, Multi-AZ Group with Read Replica, Redis Pub/Sub Channel, Redis AUTH / IAM Authentication, Cluster Parameter Group (`volatile-lru`), Slow Log Export

## Relationships
- Scoring Engine Container -> ElastiCache Redis Engine: Fetches cached rules, feature states, and publishes metrics via [Redis Protocol over TLS / TCP port 6379, Redis AUTH]
- ElastiCache Redis Engine -> AWS CloudWatch & PagerDuty: Exports slow logs and CloudWatch metrics (`CPUUtilization`, `SwapUsage`, `CurrConnections`) via [AWS CloudWatch API]

## Technology Stack
- **Amazon ElastiCache Redis (`cache.m6g.large`)**: In-memory cache for ultra-low latency rules evaluation and zero-downtime hot-reloads via pub/sub within budget.
- **AWS ElastiCache Multi-AZ with Automatic Failover**: Ensures high availability and failover within seconds to satisfy R-07.
- **In-Transit and At-Rest Encryption (AWS KMS / TLS)**: Protects cardholder data to meet PCI-DSS Level 1 compliance.
- **In-Process LRU Cache / Fail-Open Mode**: Resilient fallback mechanism in Scoring Engine for transient Redis timeouts.

## Rationale
The architecture guarantees sub-50ms P99 latency at 3,000 TPS while maintaining PCI-DSS Level 1 compliance. ElastiCache Redis combined with ECS Fargate and automated operational controls optimizes cost within the 25,000 EUR budget for a three-engineer team.